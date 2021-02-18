# Try the following
from Python_Demo import myplot,slin,sqfun
import matplotlib.pyplot as plt
myplot(0,100,1,slin,sqfun)
plt.legend(loc="best")
import math
plt.plot([41+40*math.cos(th/10) for th in range(50)],
[100+100*math.sin(th/10) for th in range(50)])
plt.text(40,100,"elilipse ?")
plt.xscale('log')