import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import warnings
from scipy.optimize import curve_fit
from matplotlib.pyplot import MultipleLocator
# fig = plt.figure(


warnings.filterwarnings('ignore')
# import seaborn as sns
def f(x):
    if x>0:
        y = np.exp(-x)
    else:
        y = 0
    return y

x_ = np.linspace(-1, 4, 100)
y_ = list(map(lambda x:f(x), x_))


# plt.show()
rate = 1
#Population mean
mu = 1/rate
# Population standard deviation
sd = np.sqrt(1/(rate**2))

print('Population mean:', mu)
print('Population standard deviation:', sd)

def mydf(sample_size):
    df2 = pd.DataFrame()

    for i in range(1, 201):
        exponential_sample = np.random.exponential((1/rate), sample_size)
        df2['sample %s'%str(i)] = exponential_sample
    data = df2.mean()
    return data

fig, axs = plt.subplots(2, 2,figsize=(10, 8))
ax1 = axs[0, 0]
ax1.plot(x_,y_, color='black')

hist1, edges1 = np.histogram(mydf(1),bins="auto",density=True)
x = edges1[:-1]+np.diff(edges1)/2.
ax1.scatter(x,hist1, color='purple')
ax1.scatter(np.linspace(-1, 0, 5), [0] * 5, color='purple')
ax1.text(0.05, 1.05,s='average of 1 values',transform=ax1.transAxes,fontsize=15,color='black')
ax2 = axs[0, 1]
ax2.plot(x_,y_, color='black')

hist2,edges2 = np.histogram(mydf(2),bins="auto",density=True)
x = edges2[:-1]+np.diff(edges2)/2.
ax2.scatter(x,hist2, color='purple')
ax2.scatter(np.linspace(-1, 0, 6), [0] * 6, color='purple')


# plt.ylim(0, 1.5)
# plt.xlim(-1, 4)
func = lambda x,beta: 1./(np.sqrt(2*np.pi) * beta) * np.exp(-(x-mu)**2/(2*beta**2))
popt, pcov = curve_fit(f=func, xdata=x, ydata=hist2)
aa = np.linspace(-1, 4, 101)
ax2.plot(aa, func(aa,*popt), ls="--", color="black", label="fit, $beta = ${}".format(popt))
ax2.text(0.05, 1.05,s='average of 2 values',transform=ax2.transAxes,fontsize=15,color='black')

ax3 = axs[1, 0]
ax3.plot(x_,y_, color='black')

hist3,edges3 = np.histogram(mydf(4),bins="auto",density=True)
x = edges3[:-1]+np.diff(edges3)/2.
ax3.scatter(x,hist3, color='purple')
ax3.scatter(np.linspace(-1, 0, 5), [0] * 5, color='purple')


# plt.ylim(0, 1.5)
# plt.xlim(-1, 4)
func = lambda x,beta: 1./(np.sqrt(2*np.pi) * beta) * np.exp(-(x-mu)**2/(2*beta**2))
popt, pcov = curve_fit(f=func, xdata=x, ydata=hist3)
aa = np.linspace(-1, 4, 101)
ax3.plot(aa, func(aa,*popt), ls="--", color="k", label="fit, $beta = ${}".format(popt))
ax3.text(0.05, 1.05,s='average of 4 values',transform=ax3.transAxes,fontsize=15,color='black')


ax4 = axs[1, 1]
ax4.plot(x_,y_, color='black')

hist4,edges4 = np.histogram(mydf(16),bins="auto",density=True)
x = edges4[:-1]+np.diff(edges4)/2.
ax4.scatter(x,hist4, color='purple')
ax4.scatter(np.linspace(-1, 0, 7), [0] * 7, color='purple')

func = lambda x,beta: 1./(np.sqrt(2*np.pi) * beta) * np.exp(-(x-mu)**2/(2*beta**2))
popt, pcov = curve_fit(f=func, xdata=x, ydata=hist4)
aa = np.linspace(-1, 4, 101)
ax4.plot(aa, func(aa,*popt), ls="--", color="k", label="fit, $beta = ${}".format(popt))
ax4.text(0.05, 1.05,s='average of 16 values',transform=ax4.transAxes,fontsize=15,color='black')

bwith = 1.5
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_ylim(-0.1, 1.6)
    ax.set_xlim(-1, 4)

    ax.set_xlabel('x',fontsize=15)
    ax.set_ylabel(r'$\rm y=exp(-x)$',fontsize=15)
    ax.vlines(x=1, ymin=-0.1, ymax=1.6, color='black', ls='--')
    ax.tick_params(which='major', length=6,labelsize=15, width=1.0, colors='black', direction='in')
    ax.tick_params(which ='minor', length=3, width=1.0, labelsize=15, labelcolor='0.6', direction='in') 
    ax.tick_params(which = 'both', top=True,bottom=True,left=True,right=True)
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.2))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
plt.tight_layout()
# plt.show()
plt.savefig('./hw_ex6.pdf',dpi=300)