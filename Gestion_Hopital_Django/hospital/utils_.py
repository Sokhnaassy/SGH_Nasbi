import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import base64
from io import BytesIO
def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph
def cons():
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('test')
    
    taille=ctrl.Antecedent(np.arange(0,200,5),'taille')
    proximite_bord=ctrl.Antecedent(np.arange(0,200,5),'proximite_bord')
    frein=ctrl.Consequent(np.arange(0,100,2),'frein')

    taille_petit=fuzz.trapmf(taille.universe,[0,0,120,160])
    taille_grand=fuzz.trapmf(taille.universe,[130,170,200,200])
    taille['pre']=taille_petit
    taille['post']=taille_grand
    plt.plot(taille.universe,taille_petit,'b',label='PreAdo')
    plt.plot(taille.universe,taille_grand,'r',label='PostAdo')
    graph=get_graph()
    return graph

