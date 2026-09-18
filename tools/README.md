Regenerating the card

    python3 tools/gen_card.py

Writes assets/card-dark.svg and assets/card-light.svg. Numbers live in the
constants at the top of gen_card.py (FACTS, PROJECTS, STATS, LANGS). ascii.json
is the gorilla logo sampled to a 42x25 character grid, one [char, class] pair per
cell, where class is g (head), os (the letters) or rim (the sticker outline).

If you edit the SVGs, bump the ?v= number in README.md. GitHub caches images
through its camo proxy and will keep serving the old one otherwise.
