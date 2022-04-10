import math
import numpy as np 
import matplotlib.pyplot as plt

# def box_muller_trans():
#     x1 = 0
#     x2 = 0
#     w = 0
#
#     # x1 = np.random.rand()
#     # x2 = np.random.rand()
#
#     # y1 = np.cos(2.0*np.pi*x1) * np.sqrt(-2.0*np.log(x1))
#     # y2 = np.sin(2.0*np.pi*x2) * np.sqrt(-2.0*np.log(x2))
#
#     while (w <= 0)|(w>=1.0):
#
#         x1 = 2.0*np.random.uniform(0,1)-1
#         x2 = 2.0*np.random.uniform(0,1)-1
#         w = x1*x1 + x2*x2
#
#     w = np.sqrt(-2.0*np.log(w)/w)
#     y1 = x1*w
#     y2 = x2*w
#
#     return y1,y2

def polar_method():
    x1 = np.random.uniform(0, 1)
    x2 = np.random.uniform(0, 1)
    y1 = np.cos(2.0 * np.pi * x1) * np.sqrt(-2.0 * np.log(x2))
    y2 = np.sin(2.0 * np.pi * x1) * np.sqrt(-2.0 * np.log(x2))
    return y1, y2
data = [list(polar_method()) for i in range(100000) ]
data = np.array(data).flatten().tolist()
fig = plt.figure(figsize=(6,5))
u = 0   # 均值μ
sig = math.sqrt(1)  # 标准差δ
x = np.linspace(u - 3*sig, u + 3*sig, 50)   # 定义域
y = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2*math.pi)*sig) # 定义曲线函数
plt.plot(x, y, "black",ls='--', linewidth=1, label=r'$N\sim(0, 1)$')    
plt.hist(data,bins=50,density=True, histtype='step', color='royalblue',label='polar method')
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('./hw12.pdf', dpi=300)

plt.show()