import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    sigma = 1.5
    # return (0.3*np.exp(-(x-1.3)**2) + 0.7* np.exp(-(x+0.7)**2/0.3))/1.2113
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(x-0)**2/sigma**2)
def f2(x):
    sigma = 1.5
    return 2/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(x-0)**2/sigma**2)
x = np.arange(-5., 5.,0.001)
fig = plt.figure(figsize=(6,5))
plt.plot(x,f1(x),color = "purple", label=r'$\rm Target: \it{f(x)}=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$',lw=1)
plt.plot(x,f2(x),color = "royalblue", label='Proposal: Gaussian Distribution',lw=1,ls='--')
plt.fill_between(x,f1(x),f2(x),color = 'royalblue', alpha=0.2, label='Rejection')
size = int(1e+07)
sigma = 1.5
loc = 0
z = np.random.normal(loc = loc,scale = sigma, size = size)
qz = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(z-loc)**2/sigma**2)
k = 5
u = np.random.uniform(low = 0, high = k*qz, size = size)

pz =  1/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5*(z-0)**2/sigma**2)
sample = z[pz >= u]

plt.hist(sample,bins=100, density=True,edgecolor='black', color='purple',alpha=0.2, label='Acception')
plt.xlim(-5, 5)
plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
plt.legend(loc='upper left', )
plt.tight_layout()
plt.grid()
plt.savefig('./hw11.pdf', dpi=300)

plt.show()