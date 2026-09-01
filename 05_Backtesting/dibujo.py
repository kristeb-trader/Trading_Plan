import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import motor

BG="#0B0E14"; PANEL="#0B0E14"; UP="#2E86FF"; DN="#FFFFFF"
GREY="#8B93A7"; GOLD="#F5C542"; DIM="#3A4152"; TXT="#E8EDF7"

def col(h): return f"{(int(h[:2])-5)%24:02d}:{h[2:4]}"

def dibujar(D,i0,i1,zonas_vivas,zonas_muertas,zonas_pm,titulo,sub,out):
    n=i1-i0
    fig,ax=plt.subplots(figsize=(24,12))
    fig.patch.set_facecolor(BG); ax.set_facecolor(PANEL)
    lo=min(D[i]['l'] for i in range(i0,i1)); hi=max(D[i]['h'] for i in range(i0,i1))
    m=(hi-lo)*0.10; ylo,yhi=lo-m,hi+m

    # zonas muertas: solo contorno tenue
    for z in zonas_muertas:
        x=z['vela']-i0
        ax.add_patch(Rectangle((max(x,0),z['lo']),n-max(x,0)+2,max(z['hi']-z['lo'],0.25),
                     facecolor='none',edgecolor=DIM,lw=0.7,zorder=1))
    # zonas vivas
    for z in zonas_vivas:
        x=z['vela']-i0
        ax.add_patch(Rectangle((max(x,0),z['lo']),n-max(x,0)+2,max(z['hi']-z['lo'],0.25),
                     facecolor=GREY,alpha=.28,edgecolor=GREY,lw=1.6,zorder=2))
        ax.text(n+2.6,(z['lo']+z['hi'])/2,
                f"{'RESIST' if z['tipo']=='R' else 'SOPORTE'}  {z['lo']:.2f}–{z['hi']:.2f}",
                color=GREY,fontsize=10,va='center',weight='bold')
    # zona premercado R-20
    for z in zonas_pm:
        ax.add_patch(Rectangle((0,z['lo']),n+2,max(z['hi']-z['lo'],0.25),
                     facecolor=GOLD,alpha=.22,edgecolor=GOLD,lw=2.0,zorder=3))
        ax.text(n+2.6,(z['lo']+z['hi'])/2,
                f"R-20 PREMERCADO  {z['lo']:.2f}–{z['hi']:.2f}",
                color=GOLD,fontsize=10.5,va='center',weight='bold')
    # velas
    for i in range(i0,i1):
        k=D[i]; x=i-i0; c=UP if k['c']>=k['o'] else DN
        ax.plot([x,x],[k['l'],k['h']],color=c,lw=1.0,zorder=5)
        ax.add_patch(Rectangle((x-.36,min(k['o'],k['c'])),.72,max(abs(k['c']-k['o']),0.25),
                     facecolor=c,edgecolor=c,lw=0.4,zorder=6))
    # ejes
    ticks=[i for i in range(0,n,10)]
    ax.set_xticks(ticks); ax.set_xticklabels([col(D[i0+t]['t']) for t in ticks],
                   color=GREY,fontsize=10)
    ax.tick_params(axis='y',colors=GREY,labelsize=10); ax.yaxis.tick_right()
    for s in ax.spines.values(): s.set_color(DIM)
    ax.grid(axis='y',color=DIM,lw=0.4,alpha=.5)
    ax.set_xlim(-2,n+18); ax.set_ylim(ylo,yhi)
    ax.text(.004,1.055,titulo,transform=ax.transAxes,color=TXT,fontsize=19,weight='bold',va='top')
    ax.text(.004,1.018,sub,transform=ax.transAxes,color=GREY,fontsize=12,va='top')
    plt.tight_layout(); plt.savefig(out,dpi=115,facecolor=BG); plt.close()
