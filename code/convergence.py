from compact_binary_spiral import evolve
import numpy as np
import matplotlib.pyplot as plt

r0 = np.array([0,6.0],dtype="float64")
v0 = np.array([1.0/np.sqrt(6),0],dtype="float64")
R = np.array([r0,v0])

t_initial = 0
t_final = 100

dt = 0.125
time1,r1,velocity1,_,_,_ = evolve(t_initial, t_final, R, dt)
time2,r2,velocity2,_,_,_ = evolve(t_initial,t_final, R, dt/2)
time3,r3,velocity3,_,_,_ = evolve(t_initial,t_final, R, dt/4)
time4,r4,velocity4,_,_,_ = evolve(t_initial,t_final, R, dt/8)
time5,r5,velocity5,_,_,_ = evolve(t_initial,t_final, R, dt/16)
time6,r6,velocity6,_,_,_ = evolve(t_initial,t_final, R, dt/32)


h = 16 ## scale factor
plt.plot(time1,np.abs(np.sqrt(velocity1[:,0]**2 +velocity1[:,1]**2) - np.sqrt(velocity2[::2,0]**2 +velocity2[::2,1]**2)),color='yellow',label=r'$E_dt$',linewidth=2.5)
plt.plot(time1,np.abs(np.sqrt(velocity2[::2,0]**2 +velocity2[::2,1]**2) - np.sqrt(velocity3[::4,0]**2 +velocity3[::4,1]**2))*h**1,color='blue',label=r'$(E_{dt/2})\times 16$',linewidth=2.5)
plt.plot(time1,np.abs(np.sqrt(velocity3[::4,0]**2 +velocity3[::4,1]**2) - np.sqrt(velocity4[::8,0]**2 +velocity4[::8,1]**2))*h**2,color='green',label=r'$(E_{dt/4})\times 16^2$',linewidth=2.5)
plt.plot(time1,np.abs(np.sqrt(velocity4[::8,0]**2 +velocity4[::8,1]**2) - np.sqrt(velocity5[::16,0]**2 +velocity5[::16,1]**2))*h**3,color='cyan',label=r'$(E_{dt/8})\times 16^3$',linewidth=2.5)
plt.plot(time1,np.abs(np.sqrt(velocity5[::16,0]**2 +velocity5[::16,1]**2) - np.sqrt(velocity6[::32,0]**2 +velocity6[::32,1]**2))*h**4,color='red',label=r'$(E_{dt/16})\times 16^4$',linewidth=2.5)

plt.grid(1)
plt.legend(fancybox=True)
plt.xlabel(r'time',fontsize=14)
plt.ylabel(r'$|E_{i} - E_{i/2}|$',fontsize=14)
plt.show()
