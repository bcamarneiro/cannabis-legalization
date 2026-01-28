#!/bin/bash
# Bump version number in VERSION file
# Usage: ./bump-version.sh [major|minor|patch]

set -e

VERSION_FILE="VERSION"
BUMP_TYPE="${1:-patch}"

if [[ ! -f "$VERSION_FILE" ]]; then
    echo "1.0.0" > "$VERSION_FILE"
fi

CURRENT_VERSION=$(cat "$VERSION_FILE")

# Parse current version
IFS='.' read -r -a parts <<< "$CURRENT_VERSION"
MAJOR="${parts[0]}"
MINOR="${parts[1]}"
PATCH="${parts[2]}"

# Bump version based on type
case "$BUMP_TYPE" in
    major)
        MAJOR=$((MAJOR + 1))
        MINOR=0
        PATCH=0
        ;;
    minor)
        MINOR=$((MINOR + 1))
        PATCH=0
        ;;
    patch)
        PATCH=$((PATCH + 1))
        ;;
    *)
        echo "Invalid bump type: $BUMP_TYPE (use major, minor, or patch)"
        exit 1
        ;;
esac

NEW_VERSION="${MAJOR}.${MINOR}.${PATCH}"
echo "$NEW_VERSION" > "$VERSION_FILE"
echo "$NEW_VERSION"
