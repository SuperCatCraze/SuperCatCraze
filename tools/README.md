two scripts here.

face_to_ascii.py turns avatar.jpg into face.json, a 80x55 grid of [char, weight]
where weight is ink, soft or null. it samples a dark percentile per cell instead
of averaging, because averaging erases pencil lines this thin. args:

    python3 tools/face_to_ascii.py 80 55 4 0.15 0.6 tools/avatar.jpg

    80 55   grid, sized so cell aspect matches the font advance / line height
    4       percentile of cell darkness to sample
    0.15    floor. below this its paper, not pencil. applied BEFORE gamma or
            the paper texture lifts into visible noise
    0.6     gamma, lifts faint strokes

gen_card.py reads face.json and writes assets/card-dark.svg + card-light.svg:

    python3 tools/gen_card.py

numbers live in the constants at the top (BLURB, STATS, LANGS).

two things that will bite you:

keyTimes on every <animate> has to end at 1. if it doesnt the browser throws the
whole animation away and you get a static card with no warning.

the card animates in from opacity 0, so anything that screenshots an svg at t=0
sees an empty box. thats why headless chrome needs setCurrentTime to render it.

bump the ?v= in README.md after editing the svgs or github keeps serving the old
one from its image cache.

gen_stats.py writes the two bottom cards:

    python3 tools/gen_stats.py

assets/stats-{dark,light}.svg and assets/langs-{dark,light}.svg. same keyTimes
rule applies. the ring is 25 private of 28 repos, so if that changes edit ROWS
and the frac in stats_card.
