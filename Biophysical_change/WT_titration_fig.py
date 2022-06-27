#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:05:08 2021

@author: selenm
"""

import matplotlib.pyplot as plt
plt.style.use('default')
import seaborn as sns
import numpy as np
import matplotlib as mpl

mpl.rc('hatch',  linewidth=2)

#Colistin patches
#Height
Col_h1=np.array([6.112,6.098,4.76,4.113,3.949,3.628])   #in nm 
Col_h2=np.array([5.146,5.059,4.547,4.024,3.947,3.798])   #in nm 
Col_h3=np.array([5.58,5.141,4.53,4.082,3.962,3.835])   #in nm 
Col_h=[Col_h1,Col_h2,Col_h3]

#Area
Col_a1=np.array([40883,41517,51025,54328,58722,59943])   #in nm^2
Col_a2=np.array([91232,94204,113111,136407,145602,148105])   #in nm^2
Col_a3=np.array([27440,29563,35354,43060,45158,46569])   #in nm^2

Col_a=[Col_a1,Col_a2,Col_a3]

#PMB patches
#Height
PMB_h1=np.array([5.634,5.448,4.954,4.392,3.919,3.729])   #in nm 
PMB_h2=np.array([6.29,6.004,5.43,4.257,4.106,3.984])   #in nm 
PMB_h3=np.array([6.322,5.916,5.352,4.065,3.816,3.758])   #in nm 
PMB_h=[PMB_h1,PMB_h2,PMB_h3]

#Area
PMB_a1=np.array([139675,140550,160400,216478,221937,228217])   #in nm^2
PMB_a2=np.array([60085,61367,64310,87958,90460,94414])   #in nm^2
PMB_a3=np.array([36327,37715,41767,58616,59658,61885])   #in nm^2
PMB_a=[PMB_a1,PMB_a2,PMB_a3]

#PMBN patches
#Height
PMBN_h1=np.array([5.096,4.474,4.26,3.895,3.624,3.519])   #in nm 
PMBN_h2=np.array([5.08,4.462,4.233,3.96,3.704,3.63])   #in nm 
PMBN_h3=np.array([6.109,5.98,5.002,4.127,4.053,3.925])   #in nm 
PMBN_h=[PMBN_h1,PMBN_h2,PMBN_h3]

#Area
PMBN_a1=np.array([40883,41517,51025,54328,58722,59943])   #in nm^2
PMBN_a2=np.array([106167,108751,110995,137003,140421,141798])   #in nm^2
PMBN_a3=np.array([27440,29563,35354,43060,45158,46569])   #in nm^2
PMBN_a=[PMBN_a1,PMBN_a2,PMBN_a3]

#P0257799 (short variant polymyxin E variant) patches = S for short length
#Door AFM 20220518
#Height
S_h1=np.array([5.236,5.188,5.00,4.890,4.303,4.203])   #in nm 
S_h2=np.array([6.420,6.362,6.023,5.821,5.234,5.138])   #in nm 
S_h3=np.array([6.113,6.035,5.817,5.430,5.051,4.914])   #in nm 
S_h=[S_h1,S_h2,S_h3]

#Area
# S_a1=np.array([65266,67674,68847,70963,83374,88372])   #in nm^2
S_a1=np.array([200346,207456,212320,219281,227769,237422])   #in nm^2
S_a2=np.array([25913,26646,27401,28152,35164,39909])   #in nm^2
S_a3=np.array([121521,124328,125427,132934,146206,154256])   #in nm^2
S_a=[S_a1,S_a2,S_a3]

#%%Calculate volume= height *area

Col_h_d=np.zeros((6,3))
Col_a_d=np.zeros((6,3))
Col_v=np.zeros((6,3))
Col_v_d=np.zeros((6,3))

PMB_h_d=np.zeros((6,3))
PMB_a_d=np.zeros((6,3))
PMB_v=np.zeros((6,3))
PMB_v_d=np.zeros((6,3))

PMBN_h_d=np.zeros((6,3))
PMBN_a_d=np.zeros((6,3))
PMBN_v=np.zeros((6,3))
PMBN_v_d=np.zeros((6,3))

S_h_d=np.zeros((6,3))
S_a_d=np.zeros((6,3))
S_v=np.zeros((6,3))
S_v_d=np.zeros((6,3))

for i in range(len(Col_h)):
    for j in range(len(Col_h1)):
        Col_v[j,i]=Col_h[i][j]*Col_a[i][j]
        PMB_v[j,i]=PMB_h[i][j]*PMB_a[i][j]
        PMBN_v[j,i]=PMBN_h[i][j]*PMBN_a[i][j]
        S_v[j,i]=S_h[i][j]*S_a[i][j]
        
#%% Calculate percent changes for height, area, and volume

# %Height change
for i in range(len(Col_h)):
    for j in range(len(Col_h1)):
        Col_h_d[j,i]=((Col_h[i][j]-Col_h[i][0])/(Col_h[i][0])*100)
        PMB_h_d[j,i]=((PMB_h[i][j]-PMB_h[i][0])/(PMB_h[i][0])*100)
        PMBN_h_d[j,i]=((PMBN_h[i][j]-PMBN_h[i][0])/(PMBN_h[i][0])*100)
        S_h_d[j,i]=((S_h[i][j]-S_h[i][0])/(S_h[i][0])*100)
        
# %Area change
for i in range(len(Col_a)):
    for j in range(len(Col_a1)):
        Col_a_d[j,i]=((Col_a[i][j]-Col_a[i][0])/(Col_a[i][0])*100)
        PMB_a_d[j,i]=((PMB_a[i][j]-PMB_a[i][0])/(PMB_a[i][0])*100)
        PMBN_a_d[j,i]=((PMBN_a[i][j]-PMBN_a[i][0])/(PMBN_a[i][0])*100)
        S_a_d[j,i]=((S_a[i][j]-S_a[i][0])/(S_a[i][0])*100)
        
# %Volume change
for i in range(len(Col_h)):
    for j in range(len(Col_v)):
        Col_v_d[j,i]=((Col_v[j][i]-Col_v[0][i])/(Col_v[0][i])*100)
        PMB_v_d[j,i]=((PMB_v[j][i]-PMB_v[0][i])/(PMB_v[0][i])*100)
        PMBN_v_d[j,i]=((PMBN_v[j][i]-PMBN_v[0][i])/(PMBN_v[0][i])*100)
        S_v_d[j,i]=((S_v[j][i]-S_v[0][i])/(S_v[0][i])*100)

#%% Calculate mean ans standard deviation for percent changes of height, area, and volume

#Mean
Col_h_m=np.zeros((6,1))
Col_a_m=np.zeros((6,1))
Col_v_m=np.zeros((6,1))

PMB_h_m=np.zeros((6,1))
PMB_a_m=np.zeros((6,1))
PMB_v_m=np.zeros((6,1))

PMBN_h_m=np.zeros((6,1))
PMBN_a_m=np.zeros((6,1))
PMBN_v_m=np.zeros((6,1))

S_h_m=np.zeros((6,1))
S_a_m=np.zeros((6,1))
S_v_m=np.zeros((6,1))

#Standard deviation 
Col_h_e=np.zeros((6,1))
Col_a_e=np.zeros((6,1))
Col_v_e=np.zeros((6,1))

PMB_h_e=np.zeros((6,1))
PMB_a_e=np.zeros((6,1))
PMB_v_e=np.zeros((6,1))

PMBN_h_e=np.zeros((6,1))
PMBN_a_e=np.zeros((6,1))
PMBN_v_e=np.zeros((6,1))

S_h_e=np.zeros((6,1))
S_a_e=np.zeros((6,1))
S_v_e=np.zeros((6,1))

# #Colistin height change
# h1_W=[ 0, -5.777578207, -14.27928595, -25.33651607, -37.5757504, -40.75344912]
Col_h_d[:,1]=[ 0, -5.777578207, -14.27928595, -25.33651607, -37.5757504, -40.75344912]
# #Colistin area change
# a1_W=[ 0, 13.04347826, 40.57405281, 44.37428243, 48.92078071, 54.21354765]

for i in range(len(Col_h_d)):
    #Height
    Col_h_m[i]=np.mean(Col_h_d[i][:])  #Colistin 
    Col_h_e[i]=np.std(Col_h_d[i][:])
    PMB_h_m[i]=np.mean(PMB_h_d[i][:])  #PMB
    PMB_h_e[i]=np.std(PMB_h_d[i][:])
    PMBN_h_m[i]=np.mean(PMBN_h_d[i][:])  #PMBN
    PMBN_h_e[i]=np.std(PMBN_h_d[i][:])
    S_h_m[i]=np.mean(S_h_d[i][:])  #Short polymy
    S_h_e[i]=np.std(S_h_d[i][:])
    
    #Area
    Col_a_m[i]=np.mean(Col_a_d[i][:])  #Colistin
    Col_a_e[i]=np.std(Col_a_d[i][:])
    PMB_a_m[i]=np.mean(PMB_a_d[i][:])  #PMB
    PMB_a_e[i]=np.std(PMB_a_d[i][:])
    PMBN_a_m[i]=np.mean(PMBN_a_d[i][:])  #PMBN
    PMBN_a_e[i]=np.std(PMBN_a_d[i][:])
    S_a_m[i]=np.mean(S_a_d[i][:])  #Short polymy
    S_a_e[i]=np.std(S_a_d[i][:])
    
    
    #Volume

    Col_v_m[i]=np.mean(Col_v_d[i][:])  #Colistin
    Col_v_e[i]=np.std(Col_v_d[i][:])  
    PMB_v_m[i]=np.mean(PMB_v_d[i][:])  #PMB
    PMB_v_e[i]=np.std(PMB_v_d[i][:])   
    PMBN_v_m[i]=np.mean(PMBN_v_d[i][:])  #PMBN
    PMBN_v_e[i]=np.std(PMBN_v_d[i][:]) 
    S_v_m[i]=np.mean(S_v_d[i][:])  #Short polymy
    S_v_e[i]=np.std(S_v_d[i][:]) 
    
#%% Height titration plot

x1=[0,0.1,0.3,0.6,6,60]
x2=[0,0.11,1.1,11.5,115]
def cm_to_inch(value):
    return value/2.54
## %Height change plot
fig1,ax= plt.subplots(figsize=(cm_to_inch(5.2),cm_to_inch(5.2)))

error=[0,3.22313,3.21433,3.17862,3.64014,4.44323]
error2=[0,1.28261,1.33657,5.8072,3.75854,2.76435]
error3=[0,4.74889,0.753608,4.58492,2.77157,2.99632]
error4=[0,2.23166,2.01555,1.28733,2.22696]  #LDAO std values for height
error5=[0,0.172568,0.724415,1.87507,0.45204,0.147865]  #Short poly E std values for height

ax.plot(x1, Col_h_m,color='#f57e20', linewidth=1.5,markersize=2, label='PME')
plt.errorbar(x1, Col_h_m,yerr=error,fmt='-o',color='#f57e20', linewidth=1,markersize=2)

ax.plot(x1, PMB_h_m,color='#faa819', linewidth=1.5, linestyle='--',dashes=(2, 3),markersize=2, label='PMB')
plt.errorbar(x1, PMB_h_m,yerr=error2,fmt='-o',color='#faa819', linewidth=1.5,linestyle='--',markersize=2)

ax.plot(x1, PMBN_h_m,color='#ffd27c', linewidth=1.5, linestyle='--', dashes=(2, 3),markersize=2, label='PMBN')
plt.errorbar(x1, PMBN_h_m,yerr=error3,fmt='-o',color='#ffd27c', linewidth=1.5,linestyle='--',markersize=2)

ax.plot(x1, S_h_m,color='#f8a869', linewidth=1.5,markersize=2, label='Short Poly E')
plt.errorbar(x1, S_h_m,yerr=error5,fmt='-o',color='#f8a869', linewidth=1,markersize=2)

ax.plot(x2, h_a, color='darkgray',linewidth=1)
plt.errorbar(x2,h_a, yerr=error4, color='darkgray',  fmt='o',markersize=2)

# ax.axvspan(0.5, 1, alpha=0.25, color='lightgray')
# plt.text(0.47, -48, 'MIC',fontsize = 8,fontname = "Arial",color='k')

ax.axvspan(xmin=0.5, xmax=1, ymin=0.1, ymax=1, alpha=0.25, color='lightgray', linewidth=0.05)
plt.text(0.4, -49, 'MIC',fontsize = 8,fontname = "Arial",color='k')



# for i in range(0,6):
#     ax.plot(x1[i], Col_h_m.item(i),color='#7c5daa', linewidth=1,markersize=1)
#     plt.errorbar(x1[i], Col_h_m.item(i),yerr=Col_h_e.item(i),fmt='-o',color='#7c5daa', linewidth=1,markersize=2)
    
#     ax.plot(x1[i], PMB_h_m.item(i),color='#bc9fce', linewidth=1,markersize=1)
#     plt.errorbar(x1[i], PMB_h_m.item(i),yerr=PMB_h_e.item(i),fmt='-o',color='#bc9fce', linewidth=1,markersize=2)

#     plt.plot(x1[i], PMBN_h_m.item(i),color='#dacff8', linewidth=1,markersize=1)
#     plt.errorbar(x1[i], PMBN_h_m.item(i),yerr=PMBN_h_e.item(i),fmt='-o',color='#dacff8', linewidth=1,markersize=2)

plt.xscale('log')
plt.xticks([0.1, 1, 10,100],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.yticks([0,-10,-20,-30,-40,-50],fontsize=8,fontname = "Arial",color='k', visible=True)
ax.set_ylim([-50,0])
plt.ylabel('% Height change', fontsize=8,fontname = "Arial",color='k')
plt.xlabel('Concentration (mg/l)', fontsize=8,fontname = "Arial",color='k')
# sns.despine(offset=5, trim=True)
sns.despine()
# plt.grid(True, which="both", ls="-", color='0.65')
# plt.legend(handles=[line1, line2,line3])

plt.show()
fig1.savefig('/Users/selenm/Documents/Colistin_Project/Outline/Height_change_titration.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)



#%% Area titration plot
fig2, ax = plt.subplots(figsize=(cm_to_inch(5.2),cm_to_inch(5.2)))

err=[0,2.65396,0.64052,8.89167,7.14591,6.97573088]
err2=[0,1.3048,3.71266,6.13289,5.62637,5.40015]
err3=[0,2.69945,9.91816,11.7026,13.6788,15.2721]
error4=[0,4.83402,5.39465,9.02241,2.43507] #LDAO std values for area
err5=[0,0.50803,1.25063,0.368973,9.22075,15.1464]  #Short poly E std values for area


ax.plot(x1, Col_a_m,color='#47bbc3', linewidth=1.5,markersize=2, label='PME')
plt.errorbar(x1, Col_a_m,yerr=err,fmt='-o',color='#47bbc3', linewidth=1,markersize=2)

ax.plot(x1, PMB_a_m,color='#4680be', linewidth=1.5, linestyle='--',dashes=(2, 3),markersize=2, label='PMB')
plt.errorbar(x1, PMB_a_m,yerr=err2,fmt='-o',color='#4680be', linewidth=1.5, linestyle='--',markersize=2)

ax.plot(x1, PMBN_a_m,color='#6cacd3', linewidth=1.5, linestyle='--',dashes=(2, 3),markersize=2, label='PMBN')
plt.errorbar(x1, PMBN_a_m,yerr=err3,fmt='-o',color='#6cacd3', linewidth=1.5, linestyle='--',markersize=2)

ax.plot(x1, S_a_m,color='#92d4d5', linewidth=1.5,markersize=2, label='Short Poly E')
plt.errorbar(x1, S_a_m,yerr=err5,fmt='-o',color='#92d4d5', linewidth=1,markersize=2)

ax.plot(x2, a_a,color="darkgray",linewidth=1)
plt.errorbar(x2,a_a, yerr=error4, color="darkgray",  fmt='o',markersize=2)



# ax.plot(x1, PMB_a_m,color='#4680BE', linewidth=1.5,markersize=2, label='PMB')
# plt.errorbar(x1, PMB_a_m,yerr=err2,fmt='-o',color='#4680BE', linewidth=1,markersize=2)

# ax.plot(x1, PMBN_a_m,color='#364680', linewidth=1.5,markersize=2, label='PMBN')
# plt.errorbar(x1, PMBN_a_m,yerr=err3,fmt='-o',color='#364680', linewidth=1,markersize=2)

ax.axvspan(xmin=0.5, xmax=1, ymin=0, ymax=0.93, alpha=0.25, color='lightgray', linewidth=0.05)
plt.text(0.43, 120, 'MIC',fontsize = 8,fontname = "Arial",color='k')

plt.xscale('log')
plt.xticks([0.1, 1, 10,100],fontsize=8,fontname = "Arial",color='k', visible=True)
# plt.yticks([-15,0,15,30,45,60,75],fontsize=8,fontname = "Arial",color='k', visible=True)
#plt.yticks([0,24,48,72,96,120],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.yticks([0,25,50,75,100,125],fontsize=8,fontname = "Arial",color='k', visible=True)


ax.set_ylim([-.5,125])
plt.ylabel('% Area change', fontsize=8,fontname = "Arial",color='k')
plt.xlabel('Concentration (mg/l)', fontsize=8,fontname = "Arial",color='k')
# sns.despine(offset=10, trim=True)
sns.despine()
# 
# plt.grid(True, which="minor", ls="-")
# plt.grid(True, which="both", ls="-", color='0.65')

plt.show()
fig2.savefig('/Users/selenm/Documents/Colistin_Project/Outline/Area_change_titration.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)

#%% Volume titration plot
fig2, ax = plt.subplots(figsize=(cm_to_inch(5.2),cm_to_inch(5.2)))

err=[0,2.65396,0.64052,8.89167,7.14591,6.97573088]
err2=[0,1.3048,3.71266,6.13289,5.62637,5.40015]
err3=[0,2.69945,9.91816,11.7026,13.6788,15.2721]
error4=[0,4.83402,5.39465,9.02241,2.43507] #LDAO std values for area
err5=[0,0.50803,1.25063,0.368973,9.22075,15.1464]  #Short poly E std values for area


ax.plot(x1, Col_a_m,color='#47bbc3', linewidth=1.5,markersize=2, label='PME')
plt.errorbar(x1, Col_a_m,yerr=err,fmt='-o',color='#47bbc3', linewidth=1,markersize=2)

ax.plot(x1, PMB_a_m,color='#4680be', linewidth=1.5, linestyle='--',dashes=(2, 3),markersize=2, label='PMB')
plt.errorbar(x1, PMB_a_m,yerr=err2,fmt='-o',color='#4680be', linewidth=1.5, linestyle='--',markersize=2)

ax.plot(x1, PMBN_a_m,color='#6cacd3', linewidth=1.5, linestyle='--',dashes=(2, 3),markersize=2, label='PMBN')
plt.errorbar(x1, PMBN_a_m,yerr=err3,fmt='-o',color='#6cacd3', linewidth=1.5, linestyle='--',markersize=2)

ax.plot(x1, S_a_m,color='#92d4d5', linewidth=1.5,markersize=2, label='Short Poly E')
plt.errorbar(x1, S_a_m,yerr=err5,fmt='-o',color='#92d4d5', linewidth=1,markersize=2)

ax.plot(x2, a_a,color="darkgray",linewidth=1)
plt.errorbar(x2,a_a, yerr=error4, color="darkgray",  fmt='o',markersize=2)



# ax.plot(x1, PMB_a_m,color='#4680BE', linewidth=1.5,markersize=2, label='PMB')
# plt.errorbar(x1, PMB_a_m,yerr=err2,fmt='-o',color='#4680BE', linewidth=1,markersize=2)

# ax.plot(x1, PMBN_a_m,color='#364680', linewidth=1.5,markersize=2, label='PMBN')
# plt.errorbar(x1, PMBN_a_m,yerr=err3,fmt='-o',color='#364680', linewidth=1,markersize=2)

ax.axvspan(xmin=0.5, xmax=1, ymin=0, ymax=0.93, alpha=0.25, color='lightgray', linewidth=0.05)
plt.text(0.43, 120, 'MIC',fontsize = 8,fontname = "Arial",color='k')

plt.xscale('log')
plt.xticks([0.1, 1, 10,100],fontsize=8,fontname = "Arial",color='k', visible=True)
# plt.yticks([-15,0,15,30,45,60,75],fontsize=8,fontname = "Arial",color='k', visible=True)
#plt.yticks([0,24,48,72,96,120],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.yticks([0,25,50,75,100,125],fontsize=8,fontname = "Arial",color='k', visible=True)


ax.set_ylim([-.5,125])
plt.ylabel('% Area change', fontsize=8,fontname = "Arial",color='k')
plt.xlabel('Concentration (mg/l)', fontsize=8,fontname = "Arial",color='k')
# sns.despine(offset=10, trim=True)
sns.despine()
# 
# plt.grid(True, which="minor", ls="-")
# plt.grid(True, which="both", ls="-", color='0.65')

plt.show()
fig2.savefig('/Users/selenm/Documents/Colistin_Project/Outline/Area_change_titration.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)