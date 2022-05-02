from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig,ax = plt.subplots(1,1)

linestyles = ['--', '-.', '-']
deg_of_freedom = [2, 4, 6]
color = ['royalblue', 'purple', 'orange']
for df, ls, c in zip(deg_of_freedom, linestyles, color):
  ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls,lw=2, label=r'$n=$'+str(df),color=c)

bwith = 1
for ax in [ax]:
    ax.tick_params(which='major', length=5,labelsize=10, width=1.0, colors='black', direction='in')
    ax.tick_params(which ='minor', length=3, width=1.0, labelsize=10, labelcolor='0.6', direction='in')

    ax.tick_params(which = 'both', top=False,bottom=True,left=True,right=True)
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)
plt.xlim(0, 10)
plt.ylim(0, 0.4)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Chi-Square Distribution')

plt.legend()
plt.tight_layout()
# plt.show()
plt.savefig('./hw3_chi_square.pdf', dpi=300)
