import json, html
ART = json.load(open('tools/ascii.json'))
AW, LH, FS = 8.1, 13.7, 13.5
AX, AY = 24, 78
RX, KW = 388, 104
W, H = 900, 486
T = 2.4                                   # master timeline (s)

LANGS=[("C#",71.4,"#178600","#178600"),("JavaScript",9.6,"#f1e05a","#b59f00"),
       ("HTML",7.2,"#e34c26","#e34c26"),("TypeScript",3.4,"#3178c6","#3178c6"),
       ("CSS",2.8,"#a371f7","#663399"),("ShaderLab",2.5,"#6e8299","#4a5a6a"),
       ("Swift",1.8,"#f05138","#f05138"),("other",1.3,"#8b949e","#8b949e")]
PROJECTS=[("gorillaos.org","mod menu + launcher for Gorilla Tag"),
          ("bonelabcraze.com","mod manager for BONELAB"),
          ("gtagmapping.org","courses for building custom maps")]
FACTS=[("Name","Ezra, a.k.a. CatCraze"),("Builds","VR mod tools, launchers, the sites behind them"),
       ("Runs on","Windows . macOS . Linux . Quest"),("Daily","Visual Studio . VS Code . Unity . zsh")]
STATS=[("Repos","28",", 25 of them private"),("Commits","3,884"," across all of it"),
       ("Code","34.9 MB"," and most of it C#")]
DARK=dict(bg="#0d1117",bar="#161b22",edge="#30363d",txt="#c9d1d9",dim="#6e7681",key="#ffa657",
          val="#a5d6ff",acc="#2d97f8",g1="#1c6b32",g2="#2ea043",g3="#5ce882",os="#ffffff",rim="#222a33")
LIGHT=dict(bg="#ffffff",bar="#f6f8fa",edge="#d0d7de",txt="#1f2328",dim="#59636e",key="#953800",
           val="#0a3069",acc="#0969da",g1="#8fd8a4",g2="#2da44e",g3="#0f5323",os="#24292f",rim="#e4e8ed")

def esc(s): return html.escape(s, quote=False)

def reveal(delay, dx=10):
    """SMIL fade+slide. keyTimes must end at 1 or the whole animation is discarded.
    Element keeps opacity=1 in markup, so no-SMIL renderers just show it."""
    a, b = delay/T, (delay+0.42)/T
    assert 0 < a < b < 1, (a, b)
    kt = f'0;{a:.4f};{b:.4f};1'
    ks = '0 0 1 1;0.22 1 0.36 1;0 0 1 1'
    return (f'<animate attributeName="opacity" begin="0s" dur="{T}s" fill="freeze" '
            f'values="0;0;1;1" keyTimes="{kt}" calcMode="spline" keySplines="{ks}"/>'
            f'<animateTransform attributeName="transform" type="translate" begin="0s" dur="{T}s" '
            f'fill="freeze" values="-{dx} 0;-{dx} 0;0 0;0 0" keyTimes="{kt}" '
            f'calcMode="spline" keySplines="{ks}"/>')

def build(c, dark):
    o=[];A=o.append
    A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
      f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,Liberation Mono,monospace" font-size="{FS}px">')
    A(f'<style>text,tspan{{white-space:pre}}.k{{fill:{c["key"]}}}.v{{fill:{c["val"]}}}'
      f'.d{{fill:{c["dim"]}}}.ac{{fill:{c["acc"]}}}'
      f'.cur{{animation:bl 1.06s steps(1,end) infinite}}'
      f'@keyframes bl{{0%,50%{{opacity:1}}50.01%,100%{{opacity:0}}}}</style>')
    A(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="{c["bg"]}" stroke="{c["edge"]}"/>')
    A(f'<path d="M.5 12.5a12 12 0 0 1 12-12h{W-25}a12 12 0 0 1 12 12v23H.5z" fill="{c["bar"]}"/>')
    A(f'<line x1=".5" y1="36" x2="{W-.5}" y2="36" stroke="{c["edge"]}"/>')
    for i,(cx,col) in enumerate(((22,"#ff5f57"),(42,"#febc2e"),(62,"#28c840"))):
        A(f'<circle cx="{cx}" cy="18.5" r="6" fill="{col}" opacity="1">'
          f'<animate attributeName="opacity" begin="0s" dur="{T}s" fill="freeze" values="0;0;1;1" '
          f'keyTimes="0;{(0.05+i*0.07)/T:.4f};{(0.35+i*0.07)/T:.4f};1"/></circle>')
    A(f'<text x="{W/2}" y="23" text-anchor="middle" fill="{c["dim"]}" font-size="12">catcraze@gorillaos: ~</text>')

    # ---- ascii art: one full-width layer per colour class, spaces elsewhere (font-proof alignment)
    A(f'<g opacity="1"><animate attributeName="opacity" begin="0s" dur="{T}s" fill="freeze" '
      f'values="0;0;1;1" keyTimes="0;0.03;0.22;1"/>')
    layers=(("rim",None,c["rim"]),("g","o",c["g1"]),("g","%",c["g2"]),
            ("g","@",c["g3"]),("os",None,c["os"]))
    for cls,ch_f,col in layers:
        A(f'<text fill="{col}" xml:space="preserve" font-size="{FS}px">')
        for i,row in enumerate(ART):
            line=''.join(ch if (k==cls and (ch_f is None or ch==ch_f)) else ' ' for ch,k in row)
            if not line.strip(): continue
            A(f'<tspan x="{AX}" y="{AY+i*LH:.1f}">{esc(line.rstrip())}</tspan>')
        A('</text>')
    A('</g>')

    # ---- right panel
    d=[0.30]
    def row(inner, step=0.05):
        A(f'<g opacity="1">{reveal(d[0])}{inner}</g>'); d[0]+=step
    y=66
    row(f'<text x="{RX}" y="{y}" font-size="15" font-weight="700"><tspan class="ac">catcraze</tspan>'
        f'<tspan class="d">@</tspan><tspan class="ac">gorillaos</tspan></text>')
    y+=16; row(f'<line x1="{RX}" y1="{y}" x2="{W-26}" y2="{y}" stroke="{c["edge"]}"/>'); y+=20
    for k,v in FACTS:
        row(f'<text x="{RX}" y="{y}" class="k">{esc(k)}:</text>'
            f'<text x="{RX+KW}" y="{y}" class="v">{esc(v)}</text>'); y+=18
    y+=12; row(f'<text x="{RX}" y="{y}" fill="{c["txt"]}" font-weight="700">What I ship</text>'); y+=18
    for n,desc in PROJECTS:
        row(f'<text x="{RX+10}" y="{y}" class="ac">{esc(n)}</text>'
            f'<text x="{RX+160}" y="{y}" class="d">{esc(desc)}</text>'); y+=18
    y+=14; row(f'<text x="{RX}" y="{y}" fill="{c["txt"]}" font-weight="700">Languages</text>'); y+=10

    BW=W-26-RX
    bs=d[0]                       # bar starts right after the Languages heading lands
    a,b = bs/T, (bs+0.95)/T
    kt=f'0;{a:.4f};{b:.4f};1'; ks='0 0 1 1;0.22 1 0.36 1;0 0 1 1'
    A(f'<clipPath id="pill"><rect x="0" y="0" width="{BW}" height="11" rx="5.5"/></clipPath>')
    A(f'<g opacity="1"><animate attributeName="opacity" begin="0s" dur="{T}s" fill="freeze" '
      f'values="0;0;1;1" keyTimes="0;{a:.4f};{a+0.05:.4f};1"/>'
      f'<g transform="translate({RX},{y})" clip-path="url(#pill)">'
      f'<g transform="scale(1,1)"><animateTransform attributeName="transform" type="scale" '
      f'begin="0s" dur="{T}s" fill="freeze" values="0.0001 1;0.0001 1;1 1;1 1" '
      f'keyTimes="{kt}" calcMode="spline" keySplines="{ks}"/>')
    x=0
    for n,p,cd,cl in LANGS:
        w=BW*p/100.0
        A(f'<rect x="{x:.2f}" y="0" width="{w+0.6:.2f}" height="11" fill="{cd if dark else cl}"/>'); x+=w
    A('</g></g></g>')
    d[0]+=0.30
    y+=28
    for i in range(0,len(LANGS),4):
        parts=[]
        for j,(n,p,cd,cl) in enumerate(LANGS[i:i+4]):
            lx=RX+j*128
            parts.append(f'<circle cx="{lx+4}" cy="{y-4}" r="4.5" fill="{cd if dark else cl}"/>'
                         f'<text x="{lx+14}" y="{y}" fill="{c["txt"]}" font-size="12">{esc(n)} '
                         f'<tspan class="d">{p}%</tspan></text>')
        row(''.join(parts)); y+=19
    y+=14
    for k,v,tail in STATS:
        row(f'<text x="{RX}" y="{y}" class="k">{esc(k)}:</text><text x="{RX+KW}" y="{y}">'
            f'<tspan class="v" font-weight="700">{esc(v)}</tspan><tspan class="d">{esc(tail)}</tspan></text>'); y+=18
    y+=16
    row(f'<text x="{RX}" y="{y}"><tspan class="ac">$</tspan> <tspan fill="{c["txt"]}">ship it</tspan></text>'
        f'<rect x="{RX+74}" y="{y-9.5}" width="8" height="12" fill="{c["acc"]}" class="cur"/>', step=0)
    A('</svg>')
    return '\n'.join(o)

for name,(c,dk) in {"card-dark":(DARK,True),"card-light":(LIGHT,False)}.items():
    p=f'assets/{name}.svg'
    open(p,'w').write(build(c,dk)); print(name, len(open(p).read()), 'bytes')
