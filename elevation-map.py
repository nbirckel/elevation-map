
import matplotlib.pyplot as plt
from ridge_map import RidgeMap
from matplotlib import rcParams
from datetime import datetime
now = datetime.now() # current date and time
date = now.strftime("%Y%m%d_%H%M")
cmaps = ["Greys_r", "plasma", "bone"]
textcolor= '#FAFAFA'
bgcolor = '#1c1c1c'
rcParams['font.family'] = 'Consolas'
title = "Chaîne des Puys"
width=8
height=12
coords =(2.900391,45.623643,3.004761,45.917721) # récupérées via http://bboxfinder.com/
nlines = 50 #le nombre de lignes tracées
elpts =100 #le nombre de points d'élevation à utiliser par ligne
vratio = 30 # l'exagération de l'élévation. Plus c'est élevé plus c'est éxagéré
rm = RidgeMap(coords, font="Consolas")
values = rm.get_elevation_data(num_lines=nlines, elevation_pts=elpts)
fig,ax = plt.subplots(figsize=(width, height))
fig.set_facecolor(bgcolor)
for cmap in cmaps :
    ridges = rm.plot_map(
                values=rm.preprocess(values=values, vertical_ratio=vratio, water_ntile=1,lake_flatness=1),
                ax=ax, kind='elevation', label=None,
                linewidth=1.2,
                line_color = plt.get_cmap(cmap),
                background_color = bgcolor
                )
    plt.figtext(0.5, 0.06 , title, fontsize=28, fontweight='bold', ha='center', color=textcolor)
    plt.figtext(0.5, 0.04 , coords, fontsize=8, fontweight='light', ha='center', color=textcolor)
    plt.figtext(0.5, 0.03 , 'Data: NASA via ridge-map.py | Code & Design by Nicolas Birckel ', fontsize=8, fontweight='regular', ha='center', color=textcolor)
    filename = date+"_"+title+"_"+cmap+"_l"+str(nlines)+"_e"+str(elpts)+"_v"+str(vratio)+"_w"+str(width)+"_h"+str(height)+".png"
    plt.savefig(filename, dpi=120, bbox_inches='tight',pad_inches=0.5, facecolor=bgcolor)
