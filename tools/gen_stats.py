import html
T = 2.0

DARK=dict(bg="#0d1117",edge="#30363d",txt="#c9d1d9",dim="#6e7681",key="#ffa657",
          val="#a5d6ff",acc="#2d97f8",ring="#2d97f8",track="#21262d")
LIGHT=dict(bg="#ffffff",edge="#d0d7de",txt="#1f2328",dim="#59636e",key="#953800",
           val="#0a3069",acc="#0969da",ring="#0969da",track="#eaeef2")

LANGS=[("C#",71.42,"#178600","#178600"),("JavaScript",9.61,"#f1e05a","#b59f00"),
       ("HTML",7.20,"#e34c26","#e34c26"),("TypeScript",3.38,"#3178c6","#3178c6"),
       ("CSS",2.75,"#a371f7","#663399"),("ShaderLab",2.47,"#6e8299","#4a5a6a"),
       ("Swift",1.78,"#f05138","#f05138"),("Lua",0.54,"#7a7aff","#000080"),
       ("Python",0.34,"#3572A5","#3572A5"),("other",0.51,"#8b949e","#8b949e")]

ICONS={  # octicons, 16x16
 "commit":"M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z",
 "repo":"M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8Z",
 "lock":"M4 4a4 4 0 0 1 8 0v2h.25c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25v-5.5C2 6.784 2.784 6 3.75 6H4Zm8.25 3.5h-8.5a.25.25 0 0 0-.25.25v5.5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25ZM10.5 6V4a2.5 2.5 0 1 0-5 0v2Z",
 "code":"m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06-1.06L13.94 8l-3.72-3.72a.75.75 0 0 1 1.06-1.06Zm-6.56 0a.75.75 0 1 1 1.06 1.06L2.06 8l3.72 3.72a.749.749 0 0 1-1.06 1.06L.47 8.53a.75.75 0 0 1 0-1.06Z",
 "cal":"M4.75 0a.75.75 0 0 1 .75.75V2h5V.75a.75.75 0 0 1 1.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 0 1 4.75 0ZM2.5 7.5v6.75c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V7.5Zm10.75-4H2.75a.25.25 0 0 0-.25.25V6h11V3.75a.25.25 0 0 0-.25-.25Z"}

ROWS=[("commit","total commits","3,884"),("repo","repositories","28"),
      ("lock","private repos","25"),("code","languages","14"),
      ("cal","here since","jan 2022")]

def esc(s): return html.escape(s, quote=False)

def reveal(delay, dx=8):
    a,b = delay/T, (delay+0.40)/T
    assert 0 < a < b < 1, (a,b)
    kt=f'0;{a:.4f};{b:.4f};1'; ks='0 0 1 1;0.22 1 0.36 1;0 0 1 1'
    return (f'<animate attributeName="opacity" begin="0s" dur="{T}s" fill="freeze" '
            f'values="0;0;1;1" keyTimes="{kt}" calcMode="spline" keySplines="{ks}"/>'
            f'<animateTransform attributeName="transform" type="translate" begin="0s" dur="{T}s" '
            f'fill="freeze" values="-{dx} 0;-{dx} 0;0 0;0 0" keyTimes="{kt}" '
            f'calcMode="spline" keySplines="{ks}"/>')

def frame(c,W,Hh,title):
    return (f'<rect x=".5" y=".5" width="{W-1}" height="{Hh-1}" rx="10" fill="{c["bg"]}" stroke="{c["edge"]}"/>'
            f'<g opacity="1">{reveal(0.12)}<text x="24" y="36" font-size="16" font-weight="700" '
            f'fill="{c["acc"]}">{esc(title)}</text></g>')

def stats_card(c, dark):
    W,Hh = 480,200
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" '
       f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,Liberation Mono,monospace" font-size="13px">']
    o.append(frame(c,W,Hh,"catcraze's github stats"))
    d=0.28; y=70
    for icon,label,val in ROWS:
        o.append(f'<g opacity="1">{reveal(d)}'
                 f'<g transform="translate(24,{y-12})"><path d="{ICONS[icon]}" fill="{c["key"]}"/></g>'
                 f'<text x="50" y="{y}" fill="{c["txt"]}">{esc(label)}</text>'
                 f'<text x="316" y="{y}" text-anchor="end" font-weight="700" fill="{c["val"]}">{esc(val)}</text></g>')
        y+=25; d+=0.07
    # ring: 25 of 28 repos private
    cx,cy,r = 396,112,40
    C = 2*3.141592653589793*r
    frac = 25/28.0
    dash = C*frac
    a,b = (d+0.05)/T, (d+0.95)/T
    o.append(f'<g opacity="1">{reveal(d+0.05, dx=0)}'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["track"]}" stroke-width="7"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["ring"]}" stroke-width="7" '
             f'stroke-linecap="round" stroke-dasharray="{dash:.2f} {C:.2f}" transform="rotate(-90 {cx} {cy})">'
             f'<animate attributeName="stroke-dasharray" begin="0s" dur="{T}s" fill="freeze" '
             f'values="0 {C:.2f};0 {C:.2f};{dash:.2f} {C:.2f};{dash:.2f} {C:.2f}" '
             f'keyTimes="0;{a:.4f};{b:.4f};1" calcMode="spline" '
             f'keySplines="0 0 1 1;0.22 1 0.36 1;0 0 1 1"/></circle>'
             f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-size="20" font-weight="700" '
             f'fill="{c["txt"]}">{frac*100:.0f}%</text>'
             f'<text x="{cx}" y="{cy+20}" text-anchor="middle" font-size="11" fill="{c["dim"]}">private</text></g>')
    o.append('</svg>')
    return '\n'.join(o)

def langs_card(c, dark):
    W,Hh = 400,200
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" '
       f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,Liberation Mono,monospace" font-size="13px">']
    o.append(frame(c,W,Hh,"most used languages"))
    BW=W-48; by=56
    a,b = 0.30/T, 1.25/T
    o.append(f'<clipPath id="lp"><rect x="0" y="0" width="{BW}" height="10" rx="5"/></clipPath>'
             f'<g opacity="1"><animate attributeName="opacity" begin="0s" dur="{T}s" fill="freeze" '
             f'values="0;0;1;1" keyTimes="0;{a:.4f};{a+0.05:.4f};1"/>'
             f'<g transform="translate(24,{by})" clip-path="url(#lp)"><g transform="scale(1,1)">'
             f'<animateTransform attributeName="transform" type="scale" begin="0s" dur="{T}s" fill="freeze" '
             f'values="0.0001 1;0.0001 1;1 1;1 1" keyTimes="0;{a:.4f};{b:.4f};1" calcMode="spline" '
             f'keySplines="0 0 1 1;0.22 1 0.36 1;0 0 1 1"/>')
    x=0
    for n,p,cd,cl in LANGS:
        w=BW*p/100.0
        o.append(f'<rect x="{x:.2f}" y="0" width="{max(w,1.2)+0.6:.2f}" height="10" fill="{cd if dark else cl}"/>'); x+=w
    o.append('</g></g></g>')
    d=0.46; y=96; COLW=178
    for i in range(0,len(LANGS),2):
        parts=[]
        for j,(n,p,cd,cl) in enumerate(LANGS[i:i+2]):
            lx=24+j*COLW
            parts.append(f'<circle cx="{lx+5}" cy="{y-4}" r="5" fill="{cd if dark else cl}"/>'
                         f'<text x="{lx+17}" y="{y}" font-size="12" fill="{c["txt"]}">{esc(n)} '
                         f'<tspan fill="{c["dim"]}">{p:.1f}%</tspan></text>')
        o.append(f'<g opacity="1">{reveal(d)}{"".join(parts)}</g>'); y+=21; d+=0.06
    o.append('</svg>')
    return '\n'.join(o)

for nm,fn,c,dk in (("stats-dark",stats_card,DARK,True),("stats-light",stats_card,LIGHT,False),
                   ("langs-dark",langs_card,DARK,True),("langs-light",langs_card,LIGHT,False)):
    p=f'assets/{nm}.svg'; open(p,'w').write(fn(c,dk)); print(nm, len(open(p).read()),'bytes')
