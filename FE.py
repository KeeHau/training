import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


a=int(input())
Ka=int(input())
Ki=int(input())
Ko=int(input())
for i in range(1,a,1):
    t=(float(i)/12)
    d=((np.log(50.0 / Ka) + (0.1 + (0.3 ** 2 / 2)) * (float(i) / 12)) / (0.3 * (float(i) / 12)**0.5))
    DeltaA= norm.cdf(d)
    di=((np.log(50.0 / Ki) + (0.1 + (0.3 ** 2 / 2)) * (float(i) / 12)) / (0.3 * (float(i) / 12)**0.5))
    DeltaI= norm.cdf(di)
    do=((np.log(50.0 / Ko) + (0.1 + (0.3 ** 2 / 2)) * (float(i) / 12)) / (0.3 * (float(i) / 12)**0.5))
    DeltaO= norm.cdf(do)
    x='3'
    plt.plot(0,0,x)
    plt.plot(0,0.5,x)
    plt.plot(0,1,x)
    plt.plot([t],[DeltaA],x)
    plt.plot([t],[DeltaI],x)
    plt.plot([t],[DeltaO],x)
    


plt.axis([0, 5, 0, 1])
plt.title('Graph of Delta Against Time to Maturity')
plt.ylabel('Delta')
plt.xlabel('Time to Maturity')
plt.ylabel('Delta')
plt.show()

