"""
MOTOR DE VERIFICACION — Chaumer  ·  FASE 1
Aplica R-10 (corrida), R-11 (retroceso), R-12 (zona) y R-20 (premercado)
sobre datos OHLC exactos. NO opera, no envia ordenes, no es un indicador.
Herramienta de auditoria: 05_Backtesting.
"""
TICK = 0.25

def cargar(path):
    velas=[]
    for ln in open(path, encoding='utf-8', errors='ignore'):
        ln=ln.strip()
        if not ln: continue
        p=ln.split(';')
        if len(p)<6: continue
        fh=p[0].split(' ')
        velas.append(dict(d=fh[0], t=fh[1], o=float(p[1]), h=float(p[2]),
                          l=float(p[3]), c=float(p[4]), v=int(float(p[5]))))
    return velas

def hhmm(t): return int(t[:4])

# ---------- R-12 : limites de la zona ----------
def zona_resistencia(k):   # corrida ALCISTA -> mecha superior
    return (max(k['o'],k['c']), k['h'])
def zona_soporte(k):       # corrida BAJISTA -> mecha inferior
    return (k['l'], min(k['o'],k['c']))

# ---------- R-10 + R-11 + R-12 : estructura ----------
def estructura(V, i0, i1):
    """Dos marcos independientes corriendo en paralelo.
       Alcista -> RESISTENCIAS.  Bajista -> SOPORTES."""
    zonas=[]
    # --- marco ALCISTA ---
    st='retro'; c0=None
    for i in range(i0+1, i1):
        if st=='retro':
            if V[i]['h'] > V[i-1]['h']:        # R-10 nace
                st='corrida'; c0=i-1
        else:
            if V[i]['l'] < V[i-1]['l']:        # R-10 muere -> R-11 empieza
                seg=range(c0,i+1)              # R-12: INCLUYE la vela del retroceso
                k=max(seg, key=lambda x: V[x]['h'])
                lo,hi=zona_resistencia(V[k])
                zonas.append(dict(tipo='R', vela=k, lo=lo, hi=hi,
                                  c0=c0, c1=i, origen='estructura'))
                st='retro'
    # --- marco BAJISTA ---
    st='retro'; c0=None
    for i in range(i0+1, i1):
        if st=='retro':
            if V[i]['l'] < V[i-1]['l']:
                st='corrida'; c0=i-1
        else:
            if V[i]['h'] > V[i-1]['h']:
                seg=range(c0,i+1)              # R-12: INCLUYE la vela del retroceso
                k=min(seg, key=lambda x: V[x]['l'])
                lo,hi=zona_soporte(V[k])
                zonas.append(dict(tipo='S', vela=k, lo=lo, hi=hi,
                                  c0=c0, c1=i, origen='estructura'))
                st='retro'
    return zonas

# ---------- R-20 : zona de premercado por volumen ----------
def zonas_premercado(V, i0, i1, umbral=2000):
    z=[]
    for i in range(i0,i1):
        if V[i]['v'] > umbral:
            k=V[i]
            if k['c'] > k['o']:                 # alcista -> RESISTENCIA
                lo,hi=zona_resistencia(k); tipo='R'
            else:                               # bajista -> SOPORTE
                lo,hi=zona_soporte(k); tipo='S'
            z.append(dict(tipo=tipo, vela=i, lo=lo, hi=hi,
                          c0=i, c1=i, origen='premercado', vol=k['v']))
    return z
