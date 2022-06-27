#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 12:35:03 2021

@author: selenm
"""

import matplotlib.pyplot as plt
plt.style.use('default')
import seaborn as sns
# sns.set(style="whitegrid")
import numpy as np
import os

# Folder Path
path = "/Users/selenm/Documents/Colistin_Project/Outline/Titration_height_area"
  
# Change the directory
os.chdir(path)

# x2=[0.5,5,50,500]
x2=[0.11,1.1,11.5,115]

def cm_to_inch(value):
    return value/2.54

h1=np.array([6.413,6.387,6.232,5.908,5.675])   #in nm 
h2=np.array([6.534,6.343,6.267,6.225,6.138])   #in nm 
h3=np.array([6.972,6.563,6.443,6.546,6.377])   #in nm 
h=[h1,h2,h3]

a1=np.array([0.158, 0.161,0.165 ,0.174 ,0.325])*1e+6  #in nm^2
a2=np.array([0.076,0.078,0.079,0.096,0.153])*1e+6     #in nm^2
a3=np.array([0.032,0.036,0.037,0.042,0.064])*1e+6     #in nm^2
a=[a1,a2,a3]

h_d=np.zeros((5,3))
a_d=np.zeros((5,3))
v=np.zeros((5,3))
v_d=np.zeros((5,3))


for i in range(len(h)):
    for j in range(len(h1)):
        v[j,i]=h[i][j]*a[i][j]

#%% Calculate percent changes for height, area, and volume
for i in range(len(h)):
    for j in range(len(h1)):
        h_d[j,i]=((h[i][j]-h[i][0])/(h[i][0])*100)

for i in range(len(a)):
    for j in range(len(a1)):
        a_d[j,i]=((a[i][j]-a[i][0])/(a[i][0])*100)
        
for i in range(len(h)):
    for j in range(len(v)):
        v_d[j,i]=((v[j][i]-v[0][i])/(v[0][i])*100)
        
#%% Calculate average percent changes for height, area, and volume
h_a=np.zeros((5,1))
a_a=np.zeros((5,1))
v_a=np.zeros((5,1))

h_e=np.zeros((5,1))
a_e=np.zeros((5,1))
v_e=np.zeros((5,1))
for i in range(len(h_d)):
    h_a[i]=np.mean(h_d[i][:])
    h_e[i]=np.std(h_d[i][:])
    a_a[i]=np.mean(a_d[i][:])
    a_e[i]=np.std(a_d[i][:])
    v_a[i]=np.mean(v_d[i][:])
    v_e[i]=np.std(v_d[i][:])

#%%
# create figure and axis objects with subplots()
fig,ax = plt.subplots(figsize=(cm_to_inch(5),cm_to_inch(5)))
error=[2.23166,2.01555,1.28733,2.22696]
# make a plot
plt.xscale('log')
ax.plot(x2, h_a[1:], color="#ef7800",linewidth=1)
plt.errorbar(x2,h_a[1:], yerr=error, color="#ef7800",  fmt='o',markersize=2)
# set x-axis label
# ax.set_xlabel("LDAO concentration (μM)",color="k",fontsize=8)
ax.set_xlabel("LDAO concentration (mg/l)",color="k",fontsize=8)
# set y-axis label
ax.set_ylabel("% Height change",color="#ef7800",fontsize=8)
ax.set_xlim([0.05,150])  
ax.set_ylim([-55,0])
ax.tick_params(axis='x', labelsize=8,width=0.5 )
ax.tick_params(axis='y', labelsize=8,width=0.5)
# plt.yticks([0,-2.5,-5,-7.5,-10],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.xticks([0.1, 1, 10,100],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.yticks([0,-10,-20,-30,-40,-50],fontsize=8,fontname = "Arial",color='k', visible=True)
sns.despine()
plt.show()

# twin object for two different y-axis on the sample plot
# ax2=ax.twinx()
# make a plot with different y-axis using second axis object
fig2,ax2 = plt.subplots(figsize=(cm_to_inch(5),cm_to_inch(5)))
error2=[4.83402,5.39465,9.02241,2.43507]
plt.xscale('log')
ax2.plot(x2, a_a[1:],color="#47bbc3",linewidth=1)
plt.errorbar(x2,a_a[1:], yerr=error2, color="#47bbc3",  fmt='o',markersize=2)
# set x-axis label
# ax2.set_xlabel("LDAO concentration (μM)",color="k",fontsize=8)
ax2.set_xlabel("LDAO concentration (mg/l)",color="k",fontsize=8)

# set y-axis label
ax2.set_ylabel("% Area change",color="#47bbc3",fontsize=8)
ax2.set_ylim([-10,125])  
ax2.set_xlim([0.05,150])  
# plt.xticks([0.1, 1, 10,100,1000],fontsize=8 )
ax2.tick_params(axis='x', labelsize=8,width=0.5)
ax2.tick_params(axis='y', labelsize=8,width=0.5)
plt.xticks([0.1, 1, 10,100],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.yticks([0,25,50,75,100,125],fontsize=8,fontname = "Arial",color='k', visible=True)
sns.despine()
# plt.grid(True, which="both", ls="-", color='0.85')
# ax.set_yticklabels(np.flipud([0 , -2, -4, -6, -8, -10,-12 ]), rotation=0, fontsize=8)
# ax2.set_yticklabels([0 , 20, 40, 60, 80, 100 ], rotation=0, fontsize=8)
plt.show()

# fig.savefig('/Users/selenm/Documents/Colistin_Project/Outline/Titration_height_area/LDAO_H.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)
# fig2.savefig('/Users/selenm/Documents/Colistin_Project/Outline/Titration_height_area/LDAO_A.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)



#%%Volume change with LDAO concentration plot

# create figure and axis objects with subplots()
fig3,ax3 = plt.subplots(figsize=(cm_to_inch(5),cm_to_inch(5)))
error3=[2.62947,3.03974,9.65675,3.1503]
# make a plot
plt.xscale('log')
ax3.plot(x2, v_a[1:], color="#7c5daa", marker="o",markersize=1.5,linewidth=1)
plt.errorbar(x2,v_a[1:], yerr=error3, color="#7c5daa",  fmt='o',markersize=2)
# ax3.plot(x2, v_a[1:], color="#4ADEDE", marker="o",markersize=1.5,linewidth=1)
# set x-axis label
# ax3.set_xlabel("LDAO concentration (μM)",fontsize=8)
ax3.set_xlabel("LDAO concentration (mg/l)",fontsize=8)
# set y-axis label
ax3.set_ylabel("% Volume change", color="#7c5daa",fontsize=8)
# ax3.set_ylabel("% Relative volume change", color="#4ADEDE",fontsize=8)
ax3.set_xlim([0.05,150])  
ax3.set_ylim([-10,125])
# plt.xticks([0.1, 1, 10,100,1000],fontsize=8 )
ax3.tick_params(axis='x', labelsize=8,width=0.5)
ax3.tick_params(axis='y', labelsize=8,width=0.5)
plt.xticks([0.1, 1, 10,100],fontsize=8,fontname = "Arial",color='k', visible=True)
plt.yticks([0,25,50,75,100,125],fontsize=8,fontname = "Arial",color='k', visible=True)
sns.despine()
# plt.grid(True, which="both", ls="-", color='0.85')
# ax.set_yticklabels(np.flipud([0 , -2, -4, -6, -8, -10,-12 ]), rotation=0, fontsize=8)
plt.show()

# fig3.savefig('/Users/selenm/Documents/Colistin_Project/Outline/Titration_height_area/LDAO_V.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)