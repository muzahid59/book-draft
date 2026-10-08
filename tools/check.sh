#!/bin/sh
# Usage: tools/check.sh <chapter.md>...  — Vale style rules + Hunspell bn_BD spelling.
# Run from the repo root. Spelling needs ~/Library/Spelling/bn_BD.{aff,dic} (see docs/style-guide.md).
cd "$(dirname "$0")/.." || exit 1
status=0
vale --no-exit --output=line "$@" | grep . && status=1
dict="$HOME/Library/Spelling/bn_BD"
if [ -f "$dict.dic" ]; then
  tmp=$(mktemp)
  for f in "$@"; do
    # The dictionary uses precomposed য় ড় ঢ় and no ZWJ (as in র‍্যাপ); the manuscript uses decomposed forms.
    python3 -c "import sys;print(open(sys.argv[1]).read().replace('য়','য়').replace('ড়','ড়').replace('ঢ়','ঢ়').replace('‍',''))" "$f" > "$tmp"
    words=$(hunspell -d "$dict" -p tools/wordlist.txt -l "$tmp" | LC_ALL=C grep -v '[A-Za-z0-9]' | LC_ALL=C sort -u | tr '\n' ' ')
    [ -n "$words" ] && echo "$f: spelling? $words" && status=1
  done
  rm -f "$tmp"
fi
exit $status
