#!/usr/bin/env python3
"""IDs estáveis de secção: gerar, verificar, bloquear e exportar."""
import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_DIR / "chapters"
LOCK_FILE = PROJECT_DIR / "docs" / "heading-ids.lock"
REQUIRED_MAX_LEVEL = 3

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ATTR_RE = re.compile(r"\s*\{([^}]*)\}\s*$")
ID_IN_ATTR_RE = re.compile(r"(?:^|\s)#([^\s}]+)")
ANCHOR_RE = re.compile(r'<(?:span|a)\s[^>]*\bid="([^"]+)"')
LINK_RE = re.compile(r"\]\(#([^)\s]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


@dataclass
class Heading:
    file: Path
    line: int
    level: int
    text: str
    id: "str | None"


def slugify(text):
    """Mesmo algoritmo que o Pandoc usa para identificadores automáticos."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[\^[^\]]*\]", "", text)
    text = re.sub(r"[*`~]", "", text)
    words = (re.sub(r"[^\w.\-]", "", w) for w in text.lower().split())
    text = "-".join(w for w in words if w)
    first_letter = re.search(r"[^\W\d_]", text)
    return text[first_letter.start():] if first_letter else "section"


def chapter_files(chapters_dir):
    return sorted(Path(chapters_dir).glob("[0-9]*.md"))


def scan(chapters_dir):
    headings, anchors, links = [], set(), []
    for path in chapter_files(chapters_dir):
        in_fence = False
        for i, raw in enumerate(path.read_text(encoding="utf-8").split("\n")):
            if FENCE_RE.match(raw):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            anchors.update(ANCHOR_RE.findall(raw))
            links.extend((path, i, target) for target in LINK_RE.findall(raw))
            match = HEADING_RE.match(raw)
            if not match:
                continue
            level, body, hid = len(match.group(1)), match.group(2), None
            attrs = ATTR_RE.search(body)
            if attrs:
                id_match = ID_IN_ATTR_RE.search(attrs.group(1))
                if not id_match:
                    raise ValueError(f"{path.name}:{i + 1}: bloco de atributos sem ID não suportado: {raw}")
                hid = id_match.group(1)
                body = body[: attrs.start()]
            headings.append(Heading(path, i, level, body.strip(), hid))
    return headings, anchors, links


def assign_missing(headings, anchors):
    """Devolve {índice do título: novo ID} só para títulos de nível <= 3 sem ID."""
    used = {h.id for h in headings if h.id} | set(anchors)
    new = {}
    for idx, h in enumerate(headings):
        if h.id:
            continue
        base = slugify(h.text)
        candidate, n = base, 0
        while candidate in used:
            n += 1
            candidate = f"{base}-{n}"
        used.add(candidate)
        if h.level <= REQUIRED_MAX_LEVEL:
            new[idx] = candidate
    return new


def present_ids(headings, anchors):
    ids = {h.id for h in headings if h.id} | set(anchors)
    ids |= {slugify(h.text) for h in headings if not h.id}
    return ids


def fix(chapters_dir):
    headings, anchors, _ = scan(chapters_dir)
    new = assign_missing(headings, anchors)
    by_file = {}
    for idx, hid in new.items():
        by_file.setdefault(headings[idx].file, {})[headings[idx].line] = hid
    for path, edits in by_file.items():
        lines = path.read_text(encoding="utf-8").split("\n")
        for line_no, hid in edits.items():
            lines[line_no] = f"{lines[line_no].rstrip()} {{#{hid}}}"
        path.write_text("\n".join(lines), encoding="utf-8")
    return len(new)


def check(chapters_dir, lock_file):
    headings, anchors, links = scan(chapters_dir)
    problems = []
    seen = set()
    for h in headings:
        if h.level <= REQUIRED_MAX_LEVEL and not h.id:
            problems.append(f"{h.file.name}:{h.line + 1}: título sem ID: {h.text}")
        if h.id:
            if h.id in seen:
                problems.append(f"{h.file.name}:{h.line + 1}: ID duplicado: {h.id}")
            seen.add(h.id)
    present = present_ids(headings, anchors)
    for path, i, target in links:
        if target not in present:
            problems.append(f"{path.name}:{i + 1}: ligação interna quebrada: #{target}")
    lock_file = Path(lock_file)
    if lock_file.exists():
        for locked in lock_file.read_text(encoding="utf-8").split():
            if locked not in present:
                problems.append(
                    f'ID publicado desapareceu: {locked} (mantém <span id="{locked}"></span> junto do novo título)'
                )
    return problems


def lock(chapters_dir, lock_file):
    headings, anchors, _ = scan(chapters_dir)
    ids = sorted({h.id for h in headings if h.id} | set(anchors))
    Path(lock_file).write_text("\n".join(ids) + "\n", encoding="utf-8")
    return len(ids)


def meta(chapters_dir, repo):
    headings, _, _ = scan(chapters_dir)
    root = Path(chapters_dir).parent
    sectionmap = {
        h.id: h.file.relative_to(root).as_posix()
        for h in headings
        if h.id and h.level <= REQUIRED_MAX_LEVEL
    }
    return {"repo": repo, "sectionmap": sectionmap}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("fix")
    sub.add_parser("lock")
    meta_parser = sub.add_parser("meta")
    meta_parser.add_argument("--repo", default="bcamarneiro/cannabis-legalization")
    meta_parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    if args.cmd == "check":
        problems = check(CHAPTERS_DIR, LOCK_FILE)
        for p in problems:
            print(p)
        print(f"{len(problems)} problema(s)")
        return 1 if problems else 0
    if args.cmd == "fix":
        print(f"{fix(CHAPTERS_DIR)} ID(s) acrescentados")
    elif args.cmd == "lock":
        print(f"{lock(CHAPTERS_DIR, LOCK_FILE)} ID(s) bloqueados em {LOCK_FILE}")
    elif args.cmd == "meta":
        Path(args.out).write_text(
            json.dumps(meta(CHAPTERS_DIR, args.repo), ensure_ascii=False, indent=1), encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
