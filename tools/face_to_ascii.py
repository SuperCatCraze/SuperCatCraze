from PIL import Image
import sys, json
CW,CH  = int(sys.argv[1]), int(sys.argv[2])
PCT    = float(sys.argv[3])      # percentile of cell darkness -> keeps thin strokes alive
FLOOR  = float(sys.argv[4])      # raw darkness below this is paper, not pencil
GAMMA  = float(sys.argv[5])      # <1 lifts faint strokes AFTER the floor cut

import os
IMG = sys.argv[6] if len(sys.argv)>6 else "avatar.jpg"
src = Image.open(IMG).convert('L').crop((0,0,460,398))
p = src.load(); W,H = src.size
xs=[x for x in range(W) if any(p[x,y]<190 for y in range(H))]
ys=[y for y in range(H) if any(p[x,y]<190 for x in range(W))]
m=4
im = src.crop((max(0,min(xs)-m), max(0,min(ys)-m), min(W,max(xs)+m), min(H,max(ys)+m)))
w,h = im.size; px = im.load()
RAMP = ".:-=+*#%@"
rows=[]; grid=[]
for gy in range(CH):
    line=""; g=[]
    for gx in range(CW):
        x0,x1 = int(gx*w/CW), int((gx+1)*w/CW)
        y0,y1 = int(gy*h/CH), int((gy+1)*h/CH)
        v = sorted(px[x,y] for y in range(y0,y1) for x in range(x0,x1))
        s = v[max(0,int(len(v)*PCT/100))]
        raw = max(0.0, min(1.0, (248.0-s)/110.0))
        if raw < FLOOR:
            ch, cls = ' ', None
        else:
            d = raw ** GAMMA
            ch  = RAMP[min(len(RAMP)-1, int(d*len(RAMP)))]
            cls = 'ink' if raw > 0.34 else 'soft'
        line += ch; g.append([ch, cls])
    rows.append(line.rstrip()); grid.append(g)
json.dump(grid, open('face.json','w'))
if '-q' not in sys.argv: print("\n".join(rows))
ink=sum(1 for r in grid for c in r if c[1]=='ink'); soft=sum(1 for r in grid for c in r if c[1]=='soft')
print(f"[crop {im.size}  ink {ink}  soft {soft}  blank {CW*CH-ink-soft}]")
