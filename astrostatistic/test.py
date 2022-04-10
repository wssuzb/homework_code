import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return (0.3*np.exp(-(x-0.3)**2) + 0.7* np.exp(-(x-2.)**2/0.3))/1.2113
def f2(x):
    sigma = 1.2
    return 2.5/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(x-1.4)**2/sigma**2)
x = np.arange(-4., 6.,0.001)
plt.plot(x,f1(x),color = "purple")
plt.plot(x,f2(x),color = "blue")
plt.fill_between(x,f1(x),f2(x),color = 'royalblue', alpha=0.5)
size = int(1e+07)
sigma = 1.2
loc = 1.4
z = np.random.normal(loc = loc,scale = sigma, size = size)
qz = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(z-loc)**2/sigma**2)
k = 2.5
#z = np.random.uniform(low = -4, high = 6, size = size)
#qz = 0.1
#k = 10
u = np.random.uniform(low = 0, high = k*qz, size = size)

pz =  0.3*np.exp(-(z-0.3)**2) + 0.7* np.exp(-(z-2.)**2/0.3)
sample = z[pz >= u]
# plt.hist(z)
plt.hist(sample,bins=50, density=True,color='orange')

plt.show()
#
# def f1(x):
#     return 0.3*np.exp(-(x-0.3)**2) + 0.7* np.exp(-(x-2.)**2/0.3)
# def f2(x):
#     sigma =1.2
#     return 2.5/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(x-1.4)**2/sigma**2)
# x = np.arange(-4.,6.,0.01)
#
# plt.plot(x,f1(x),color = "red")
# plt.plot(x,f2(x),color = "blue")
# plt.xticks([])
# plt.yticks([])
# plt.ylim(0,0.9)
# plt.xlim(-4,6)
# plt.plot([0.3,0.3],[0,0.54601532],color = "black")
# plt.plot(0.3,0.54601532,'b.')
# plt.fill_between(x,f1(x),f2(x),color = (0.7,0.7,0.7))
# plt.annotate('$z_0$',xy=(0.,0),xytext=(0.2,-0.04),fontsize=15)
# plt.annotate('$u_0$',xy=(0.,0.),xytext=(0.35,0.15),fontsize=15)
# plt.annotate('$kq(z_0)$',xy=(0.,0.),xytext=(-0.8,0.55),fontsize=15)
# plt.annotate('$p(z)$',xy=(0.,0.),xytext=(2,0.15),fontsize=15)
# plt.annotate('$kq(z)$',xy=(0.,0.),xytext=(2.7,0.5),fontsize=15)
# plt.show()
