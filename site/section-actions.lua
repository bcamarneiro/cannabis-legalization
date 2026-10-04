local repo = ""
local map = {}

local function urlencode(s)
  return (s:gsub("[^A-Za-z0-9%-%._~]", function(c)
    return string.format("%%%02X", string.byte(c))
  end))
end

local function read_meta(meta)
  repo = pandoc.utils.stringify(meta.repo or "")
  map = {}
  for id, file in pairs(meta.sectionmap or {}) do
    map[id] = pandoc.utils.stringify(file)
  end
end

local function add_actions(h)
  if h.level > 3 or h.identifier == "" then
    return nil
  end
  local id = h.identifier
  local enc = urlencode(id)
  local function issue(template, label)
    return string.format(
      '<a href="https://github.com/%s/issues/new?template=%s&section=%s">%s</a>',
      repo, template, enc, label)
  end
  local links = {
    string.format('<a class="permalink" href="#%s">Ligação</a>', id),
    '<span class="issue-label">Levantar questão:</span>',
    issue("corrigir-erro-ou-fonte.yml", "Corrigir erro"),
    issue("propor-alteracao.yml", "Propor alteração"),
    issue("contestar-argumento.yml", "Contestar"),
  }
  if map[id] then
    table.insert(links, string.format(
      '<a href="https://github.com/%s/edit/main/%s">Sugerir alteração</a>', repo, map[id]))
  end
  local block = pandoc.RawBlock("html", '<p class="section-actions">' .. table.concat(links, "") .. "</p>")
  return { h, block }
end

return { { Meta = read_meta }, { Header = add_actions } }
