# high-quality worlds A (wall + roller) and E (Luxembourg relief map + subsidy gauge)
import math, random
BL='#2F6BFF'; INK='#0E131E'

def defs_common(p):
    return f'''<defs>
<filter id="{p}plaster" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="4" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0.45  0 0 0 0 0.42  0 0 0 0 0.38  0 0 0 0.10 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="{p}rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.5 0.03" numOctaves="2" seed="7" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="18" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="{p}nap" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.6 0.25" numOctaves="2" seed="11" result="t"/><feColorMatrix in="t" type="matrix" values="0 0 0 0 0  0 0 0 0 0.05  0 0 0 0 0.25  0 0 0 0.55 -0.12"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="{p}streak" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.09 0.003" numOctaves="2" seed="3" result="t"/><feColorMatrix in="t" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.22 -0.07"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="{p}blot" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="3" seed="21" result="t"/><feColorMatrix in="t" type="matrix" values="0 0 0 0 0.98  0 0 0 0 0.97  0 0 0 0 0.95  0 0 0 -7 3.6"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="{p}soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="18"/></filter>
<filter id="{p}soft6" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
<linearGradient id="{p}wall" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.55" stop-color="#F4F1EA"/><stop offset="1" stop-color="#E4DFD4"/></linearGradient>
<linearGradient id="{p}paint" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2A62F0"/><stop offset="0.35" stop-color="#3C76FF"/><stop offset="0.6" stop-color="#2F6BFF"/><stop offset="1" stop-color="#1F52D6"/></linearGradient>
<linearGradient id="{p}sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.42" stop-color="#fff" stop-opacity="0.22"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.05"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="{p}cyl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1A44C2"/><stop offset="0.18" stop-color="#4F82FF"/><stop offset="0.34" stop-color="#7FA4FF"/><stop offset="0.55" stop-color="#2F6BFF"/><stop offset="0.85" stop-color="#1A44C2"/><stop offset="1" stop-color="#0F2E8F"/></linearGradient>
<linearGradient id="{p}metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4F6FA"/><stop offset="0.45" stop-color="#B9C0CC"/><stop offset="0.55" stop-color="#8C95A3"/><stop offset="1" stop-color="#D8DDE5"/></linearGradient>
<linearGradient id="{p}metalv" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#D8DDE5"/><stop offset="0.45" stop-color="#8C95A3"/><stop offset="0.55" stop-color="#B9C0CC"/><stop offset="1" stop-color="#F4F6FA"/></linearGradient>
<linearGradient id="{p}grip" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B1120"/><stop offset="0.3" stop-color="#2A3346"/><stop offset="0.5" stop-color="#3B465C"/><stop offset="1" stop-color="#0B1120"/></linearGradient>
<linearGradient id="{p}cap" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1B2232"/><stop offset="1" stop-color="#4A5468"/></linearGradient>
<linearGradient id="{p}skirt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.15" stop-color="#ECE8DF"/><stop offset="1" stop-color="#D9D3C6"/></linearGradient>
<linearGradient id="{p}floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9B79C"/><stop offset="1" stop-color="#A88F6E"/></linearGradient>
<linearGradient id="{p}tape" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F3E7C4"/><stop offset="1" stop-color="#E2D3A6"/></linearGradient>
<radialGradient id="{p}light" cx="0.25" cy="0.15" r="0.9"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.35"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
</defs>'''

def roller(p, x, y, s=1.0, rot=-8):
    # cylinder length 300, diameter 118, frame and handle going down-right
    L, D = 300, 118
    g = f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
    g += f'<ellipse cx="{L/2+40}" cy="{D+70}" rx="{L*0.62}" ry="34" fill="#0E131E" opacity="0.28" filter="url(#{p}soft)"/>'
    # frame: from right cap, out, down to handle
    g += f'<path d="M{L+6} {D/2} H{L+46} Q{L+70} {D/2} {L+70} {D/2+26} V{D+70} Q{L+70} {D+96} {L+44} {D+96} H{L/2+40} Q{L/2+16} {D+96} {L/2+16} {D+122} V{D+150}" fill="none" stroke="url(#{p}metal)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
    g += f'<path d="M{L+6} {D/2-4} H{L+46} Q{L+66} {D/2-4} {L+66} {D/2+22}" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.7"/>'
    # handle
    g += f'<rect x="{L/2-6}" y="{D+140}" width="44" height="40" rx="10" fill="url(#{p}cap)"/>'
    g += f'<rect x="{L/2-12}" y="{D+176}" width="56" height="250" rx="26" fill="url(#{p}grip)"/>'
    g += ''.join(f'<rect x="{L/2-12}" y="{D+200+i*26}" width="56" height="5" rx="2.5" fill="#000" opacity="0.25"/>' for i in range(7))
    g += f'<rect x="{L/2-2}" y="{D+190}" width="10" height="220" rx="5" fill="#FFFFFF" opacity="0.12"/>'
    # cylinder
    g += f'<rect x="0" y="0" width="{L}" height="{D}" rx="22" fill="url(#{p}cyl)"/>'
    g += f'<rect x="0" y="0" width="{L}" height="{D}" rx="22" fill="#2F6BFF" filter="url(#{p}nap)"/>'
    g += f'<rect x="12" y="{D*0.24}" width="{L-24}" height="{D*0.12}" rx="6" fill="#FFFFFF" opacity="0.28"/>'
    g += f'<ellipse cx="{L}" cy="{D/2}" rx="16" ry="{D/2}" fill="url(#{p}cap)"/><ellipse cx="{L}" cy="{D/2}" rx="7" ry="14" fill="url(#{p}metal)"/>'
    g += f'<ellipse cx="0" cy="{D/2}" rx="14" ry="{D/2-2}" fill="#1A44C2"/>'
    g += '</g>'
    return g

def wall_scene(p, x, y, w, h, patchy=False, roller_pos=None, tray=False):
    o = f'<g>'
    o += f'<rect x="{x}" y="{y+40}" width="{w}" height="{h}" rx="34" fill="#0E131E" opacity="0.22" filter="url(#{p}soft)"/>'
    o += f'<clipPath id="{p}clip"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30"/></clipPath><g clip-path="url(#{p}clip)">'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{p}wall)"/>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#000" filter="url(#{p}plaster)"/>'
    # painted band (rough roller edges), with streaks and sheen
    lanes = [(0.07, 0.30, 0.10, 0.80, 1.0), (0.28, 0.51, 0.09, 0.81, 0.93), (0.49, 0.72, 0.10, 0.80 if patchy else 0.50, 1.0)]
    band = ''
    for i, (l0, l1, t0, b0, op) in enumerate(lanes):
        lx0, lx1, ty, by = x + w*l0, x + w*l1, y + h*t0, y + h*b0
        dd = f'M{lx0:.0f} {ty:.0f} L{lx1:.0f} {ty-6:.0f} L{lx1+6:.0f} {by:.0f} Q{(lx0+lx1)/2:.0f} {by+14:.0f} {lx0-4:.0f} {by+4:.0f} Z'
        band += dd + ' '
        o += f'<g filter="url(#{p}rough)"><path d="{dd}" fill="url(#{p}paint)" opacity="{op}"/><path d="{dd}" fill="#fff" filter="url(#{p}streak)"/></g>'
    top, bot = y + h*0.10, y + h*0.80
    if patchy:
        o += f'<g filter="url(#{p}rough)"><path d="{band}" fill="#F7F4EE" filter="url(#{p}blot)"/></g>'
        for i, (dx, L, wd) in enumerate([(0.12, 90, 7), (0.22, 150, 5), (0.36, 70, 8), (0.44, 120, 5), (0.60, 95, 6)]):
            cx = x + w*dx; y0 = bot - 4
            o += f'<path d="M{cx-wd*1.6:.1f} {y0} C{cx-wd:.1f} {y0+L*0.3:.1f} {cx-wd*0.55:.1f} {y0+L*0.75:.1f} {cx-wd*0.9:.1f} {y0+L:.1f} A{wd*1.25:.1f} {wd*1.35:.1f} 0 1 0 {cx+wd*0.9:.1f} {y0+L:.1f} C{cx+wd*0.55:.1f} {y0+L*0.75:.1f} {cx+wd:.1f} {y0+L*0.3:.1f} {cx+wd*1.6:.1f} {y0} Z" fill="url(#{p}paint)"/>'
            o += f'<ellipse cx="{cx-wd*0.35:.1f}" cy="{y0+L+wd*0.2:.1f}" rx="{wd*0.35:.1f}" ry="{wd*0.5:.1f}" fill="#fff" opacity="0.55"/>'
    o += f'<path d="{band}" fill="url(#{p}sheen)" opacity="0.7"/>'
    # painter's tape along the top edge
    o += f'<rect x="{x}" y="{y+h*0.065}" width="{w}" height="26" fill="url(#{p}tape)" transform="rotate(-0.6 {x+w/2} {y})"/>'
    o += f'<rect x="{x}" y="{y+h*0.065+20}" width="{w}" height="6" fill="#000" opacity="0.06" transform="rotate(-0.6 {x+w/2} {y})"/>'
    # skirting + floor
    o += f'<rect x="{x}" y="{y+h*0.86}" width="{w}" height="{h*0.05}" fill="url(#{p}skirt)"/>'
    o += f'<rect x="{x}" y="{y+h*0.91}" width="{w}" height="{h*0.09}" fill="url(#{p}floor)"/>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{p}light)"/>'
    if tray:
        tx, ty = x + w*0.60, y + h*0.83
        o += f'<ellipse cx="{tx+150}" cy="{ty+120}" rx="190" ry="26" fill="#0E131E" opacity="0.3" filter="url(#{p}soft6)"/>'
        o += f'<path d="M{tx} {ty+20} L{tx+300} {ty+20} L{tx+270} {ty+118} L{tx+30} {ty+118} Z" fill="url(#{p}metalv)"/>'
        o += f'<path d="M{tx+14} {ty+28} L{tx+286} {ty+28} L{tx+262} {ty+80} L{tx+38} {ty+80} Z" fill="url(#{p}paint)"/><path d="M{tx+40} {ty+36} L{tx+200} {ty+36}" stroke="#fff" stroke-width="5" opacity="0.35" stroke-linecap="round"/>'
    o += '</g></g>'
    if roller_pos:
        o += roller(p, *roller_pos)
    return o

# ---------- Luxembourg relief map
LUX = [(6.03,50.18),(6.11,50.16),(6.14,50.11),(6.13,50.05),(6.18,49.98),(6.22,49.94),(6.30,49.87),(6.43,49.81),(6.50,49.73),(6.52,49.70),(6.43,49.63),(6.39,49.55),(6.37,49.47),(6.25,49.50),(6.16,49.50),(6.03,49.45),(5.97,49.49),(5.89,49.50),(5.82,49.55),(5.88,49.60),(5.90,49.66),(5.82,49.72),(5.75,49.79),(5.74,49.86),(5.78,49.96),(5.83,50.02),(5.87,50.09),(5.97,50.17)]
CITIES = [('Lëtzebuerg', 6.13, 49.61), ('Esch', 5.98, 49.50), ('Ettelbréck', 6.10, 49.85), ('Clierf', 6.03, 50.05), ('Wolz', 5.93, 49.95), ('Gréiwemaacher', 6.44, 49.68)]
def proj(lon, lat, ox, oy, k):
    return ox + (lon - 5.72) * k, oy + (50.20 - lat) * k * 1.55

def map_scene(p, ox, oy, k):
    pts = [proj(a, b, ox, oy, k) for a, b in LUX]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts) + ' Z'
    o = f'''<defs><linearGradient id="{p}land" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EEF1F8"/></linearGradient>
<linearGradient id="{p}edge" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D3D9E6"/><stop offset="1" stop-color="#AEB8CC"/></linearGradient>
<radialGradient id="{p}pin" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#8FB0FF"/><stop offset="0.45" stop-color="#2F6BFF"/><stop offset="1" stop-color="#1A44C2"/></radialGradient>
<pattern id="{p}dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="11" cy="11" r="2.4" fill="#2F6BFF" opacity="0.16"/></pattern></defs>'''
    o += f'<path d="{d}" transform="translate(0 46)" fill="#0E131E" opacity="0.25" filter="url(#{p}soft)"/>'
    for i in range(14, 0, -2):  # extruded edge
        o += f'<path d="{d}" transform="translate(0 {i})" fill="url(#{p}edge)"/>'
    o += f'<path d="{d}" fill="url(#{p}land)"/><path d="{d}" fill="url(#{p}dots)"/>'
    o += f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.9"/>'
    # Ösling / Gutland divide (subtle relief line)
    a = proj(5.76, 49.90, ox, oy, k); b = proj(6.22, 49.93, ox, oy, k)
    o += f'<path d="M{a[0]:.0f} {a[1]:.0f} Q{(a[0]+b[0])/2:.0f} {a[1]-30:.0f} {b[0]:.0f} {b[1]:.0f}" fill="none" stroke="#C5CEE0" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
    for i, (name, lon, lat) in enumerate(CITIES):
        x, y = proj(lon, lat, ox, oy, k)
        if i in (0, 1, 2, 4):  # pins = areas reached (illustrative)
            o += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#2F6BFF" opacity="0.10"/><circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="none" stroke="#2F6BFF" stroke-width="3" opacity="0.35"/>'
            o += f'<ellipse cx="{x:.0f}" cy="{y+4:.0f}" rx="14" ry="5" fill="#0E131E" opacity="0.3" filter="url(#{p}soft6)"/>'
            o += f'<path d="M{x:.0f} {y:.0f} C{x-6:.0f} {y-18:.0f} {x-24:.0f} {y-30:.0f} {x-24:.0f} {y-50:.0f} A24 24 0 1 1 {x+24:.0f} {y-50:.0f} C{x+24:.0f} {y-30:.0f} {x+6:.0f} {y-18:.0f} {x:.0f} {y:.0f} Z" fill="url(#{p}pin)"/>'
            o += f'<circle cx="{x:.0f}" cy="{y-50:.0f}" r="9" fill="#FFFFFF"/>'
        else:
            o += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#9AA6BE"/>'
        if i in (0, 1, 2, 4): o += f'<text x="{x+30:.0f}" y="{y-40:.0f}" font-family="Montserrat" font-weight="700" font-size="24" fill="#3C4458">{name}</text>'
    return o

def gauge(p, cx, cy, r, frac, num, label):
    a0, a1 = math.radians(135), math.radians(135 + 270*frac)
    def pt(a, rr): return cx + rr*math.cos(a), cy + rr*math.sin(a)
    sx, sy = pt(math.radians(135), r); ex, ey = pt(math.radians(405), r); fx, fy = pt(a1, r)
    big = 1 if 270*frac > 180 else 0
    o = f'''<defs><linearGradient id="{p}g" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#1A44C2"/><stop offset="0.6" stop-color="#2F6BFF"/><stop offset="1" stop-color="#7FA4FF"/></linearGradient></defs>'''
    o += f'<circle cx="{cx}" cy="{cy+24}" r="{r+60}" fill="#0E131E" opacity="0.22" filter="url(#{p}soft)"/>'
    o += f'<circle cx="{cx}" cy="{cy}" r="{r+58}" fill="#FFFFFF"/><circle cx="{cx}" cy="{cy}" r="{r+58}" fill="none" stroke="#ECEFF5" stroke-width="2"/>'
    o += f'<path d="M{sx:.1f} {sy:.1f} A{r} {r} 0 1 1 {ex:.1f} {ey:.1f}" fill="none" stroke="#E8ECF4" stroke-width="30" stroke-linecap="round"/>'
    o += f'<path d="M{sx:.1f} {sy:.1f} A{r} {r} 0 {big} 1 {fx:.1f} {fy:.1f}" fill="none" stroke="url(#{p}g)" stroke-width="30" stroke-linecap="round"/>'
    for i in range(11):
        a = math.radians(135 + 27*i); x0, y0 = pt(a, r-30); x1, y1 = pt(a, r-42)
        o += f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#C5CEE0" stroke-width="3" stroke-linecap="round"/>'
    o += f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="22" fill="#FFFFFF" stroke="#2F6BFF" stroke-width="7"/>'
    o += f'<text x="{cx}" y="{cy-58}" text-anchor="middle" font-family="Montserrat" font-weight="600" font-size="26" fill="#6B7590">bis zu</text>'
    o += f'<text x="{cx}" y="{cy+36}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="96" letter-spacing="-4" fill="{INK}">{num}</text>'
    o += f'<text x="{cx}" y="{cy+86}" text-anchor="middle" font-family="IBM Plex Mono" font-weight="500" font-size="22" letter-spacing="3" fill="#2F6BFF">{label}</text>'
    return o
