#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:25:02 2022

@author: selenm
"""

#This script plots the elastic modulus distribution of MG1655 WT and MCR-1 strain OM patches 
#(n=3)before and after polymyxin (60 mg/l) treatment.

#Using the distribution data, it calculates the combined mean and standard deviation. 

#Finally, it applies statistical test to report on the significance of the observed change. 

import pandas as pd
from scipy import stats
from scipy.stats import normaltest
from scipy.stats import kruskal
from scipy.stats import ranksums
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np

#%%Folder Path for MCR-1 data

path = "/Users/selenm/polybox/Colistin_Project_Collab/Selen/Modulus_calc/Main_modulus_fig/MCR1"
  
# Change the directory
os.chdir(path)
Mcr1_PBS = pd.read_csv("MCR1_PBS.csv")
Mcr1_Col = pd.read_csv("MCR1_Colistin.csv")

#%% Folder Path for WT data

path = "/Users/selenm/polybox/Colistin_Project_Collab/Selen/Modulus_calc/Main_modulus_fig/WT"
  
# Change the directory
os.chdir(path)
Wt_PBS = pd.read_csv("WT_PBS.csv")
Wt_Col = pd.read_csv("WT_Colistin.csv")

#%%Arrangements on the dataframes

Mcr1_PBS.drop(['Unnamed: 0','Unnamed: 0.1'], axis='columns', inplace=True)
Mcr1_Col.drop(['Unnamed: 0','Unnamed: 0.1'], axis='columns', inplace=True)

Wt_PBS.drop(['Unnamed: 0'], axis='columns', inplace=True)
Wt_Col.drop(['Unnamed: 0'], axis='columns', inplace=True)


# Wt_PBS.drop(['Unnamed: 0','Unnamed: 0.1'], axis='columns', inplace=True)
# Wt_Col.drop(['Unnamed: 0','Unnamed: 0.1'], axis='columns', inplace=True)


#%%Generate data sets

frames = [Mcr1_PBS, Mcr1_Col]
result = pd.concat(frames)   #Data set for MCR1
result[['Modulus']].describe()

result=result[result.Modulus<100]  #Data filter (data>100 MPa)
#%%Generate data sets

frames2 = [Wt_PBS, Wt_Col]
result2 = pd.concat(frames2)   #Data set for WT
result2[['Modulus']].describe()

result2=result2[result2.Modulus<100]   #Data filter (data>100 MPa)
#%%Calculate combined mean and std for data sets

##########  MCR1  ##########
#Combined mean for MCR1 data set
ns=result.groupby(["Group", "File"])['Modulus'].size()
ms=result.groupby(["Group", "File"])['Modulus'].mean()
stds=result.groupby(["Group", "File"])['Modulus'].std()

b_ms= ((ns[0]*ms[0])+(ns[1]*ms[1])+(ns[2]*ms[2]))/(ns[0]+ns[1]+ns[2])  #Combined mean for MCR1 dataset before polymyxin
a_ms= ((ns[3]*ms[3])+(ns[4]*ms[4])+(ns[5]*ms[5]))/(ns[3]+ns[4]+ns[5])  #Combined mean for MCR1 dataset after polymyxin

#Combined std for MCR1 data set
b_ds=[b_ms-ms[0],b_ms-ms[1],b_ms-ms[2]]
a_ds=[a_ms-ms[3],a_ms-ms[4],a_ms-ms[5]]

b_sig=np.sqrt(((ns[0]*(stds[0]**2+b_ds[0]**2))+(ns[1]*(stds[1]**2+b_ds[1]**2))+(ns[2]*(stds[2]**2+b_ds[2]**2)))/(ns[0]+ns[1]+ns[2]))
a_sig=np.sqrt(((ns[3]*(stds[3]**2+a_ds[0]**2))+(ns[4]*(stds[4]**2+a_ds[1]**2))+(ns[5]*(stds[5]**2+a_ds[2]**2)))/(ns[3]+ns[4]+ns[5]))

print(b_ms)
print(b_sig)
print ('\n')
print(a_ms)
print(a_sig)

#%%Violin plots of modulus distribution of MCR-1

from matplotlib import pyplot as plt
plt.style.use('default')
import seaborn as sns
import numpy as np
import os
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 0.5 #set the value globally

def cm_to_inch(value):
    return value/2.54

fig,ax = plt.subplots(figsize=(cm_to_inch(6),cm_to_inch(2.7)), linewidth=0.5)
dy="Modulus"; dx = "Group"; dhue="File"

# make a plot
# palette = 'YlOrBr'
palette = ["#ed6f5b","#86201a"]

ax = sns.violinplot(y = dy, x=dx, data=result,
                    palette=palette,showmeans=True,
                    scale="count", inner=None,linewidth=0.1,color='k')
for violin in ax.collections:
    ax.collections[0].set_edgecolor('k')
    ax.collections[1].set_edgecolor('k')

# sns.boxplot(y = dy, x=dx, data=result, saturation=0.75,linewidth= 0.25, width=0.075,
#             palette=palette, boxprops={'zorder': 2},showfliers=False, ax=ax)


sns.pointplot(y = dy, x=dx, markers='o',scale=0.2,join=False, ci='sd',errwidth=0.5,capsize=0.025,color='black', data=result)


# plt.ylim(-2, 40)
min_ylim, max_ylim = plt.ylim()

plt.text(b_ms*0.0025, max_ylim*0.6, '$\mu={:.2f}$ MPa'.format(b_ms), fontsize=6,color='k')

plt.text(a_ms*0.12, max_ylim*0.6, '$\mu={:.2f}$ MPa'.format(a_ms), fontsize=6,color='k')

xlim = ax.get_xlim()
ylim = ax.get_ylim()
# ylim = 100

labelsize=7
fontsize=7

plt.setp(ax.artists, edgecolor = 'k')  
plt.setp(ax.lines, color='k')
old_len_collections = len(ax.collections)

# set y-axis label
ax.set_ylabel("Modulus (MPa)",color="k",fontsize=fontsize)
# set x-axis label
ax.set_xlabel("Polymyxin",color="k",fontsize=fontsize)

ax.tick_params(axis='x', labelsize=labelsize,width=0.5 )
ax.tick_params(axis='y', labelsize=labelsize,width=0.5)
x_ticks_labels=['(-)','(+)']
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=fontsize)

plt.yticks([0,25,50,75,100],fontsize=fontsize,fontname = "Arial",color='k', visible=True)
# plt.yticks([0,10,20,30,40,50],fontsize=8,fontname = "Arial",color='k', visible=True)
# plt.yticks([0,10,20,30,40],fontsize=8,fontname = "Arial",color='k', visible=True)


# plt.xticks()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.tick_params(axis = 'x',  length = 0)

ax.set_xlim(xlim)
ax.set_ylim(ylim)
# plt.ylim(-5, 100)
plt.ylim(-5, 100)
plt.legend('',frameon=False)
plt.show()

#  Save figure  # # 
path = "/Users/selenm/polybox/Colistin_Project_Collab/Selen/Modulus_calc/Main_modulus_fig/MCR1"

# Change the directory
os.chdir(path) 
 
# fig.savefig('MCR_Modulus_Main.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)

#%% Statistical test for MCR-1


before=[ms[0],ms[1],ms[2]]
after=[ms[3],ms[4],ms[5]]

stat, p =mannwhitneyu(before,after)
print('Statistics=%.3f, p=%.6f' % (stat, p))

#%%
##########  WT  ##########
#Combined mean for WT data set
ns=result2.groupby(["Group", "File"])['Modulus'].size()
ms=result2.groupby(["Group", "File"])['Modulus'].mean()
stds=result2.groupby(["Group", "File"])['Modulus'].std()

b_ms= ((ns[0]*ms[0])+(ns[1]*ms[1])+(ns[2]*ms[2])+(ns[3]*ms[3])+(ns[4]*ms[4]))/(ns[0]+ns[1]+ns[2]+ns[3]+ns[4])  #Combined mean for WT dataset before polymyxin
a_ms= ((ns[5]*ms[5])+(ns[6]*ms[6])+(ns[7]*ms[7])+(ns[8]*ms[8])+(ns[9]*ms[9]))/(ns[5]+ns[6]+ns[7]+ns[8]+ns[9])  #Combined mean for WT dataset after polymyxin

#Combined std for WT data set
b_ds=[b_ms-ms[0],b_ms-ms[1],b_ms-ms[2],b_ms-ms[3],b_ms-ms[4]]
a_ds=[a_ms-ms[5],a_ms-ms[6],a_ms-ms[7],a_ms-ms[8],a_ms-ms[9]]

b_sig=np.sqrt(((ns[0]*(stds[0]**2+b_ds[0]**2))+(ns[1]*(stds[1]**2+b_ds[1]**2))
               +(ns[2]*(stds[2]**2+b_ds[2]**2))+(ns[3]*(stds[3]**2+b_ds[3]**2))
               +(ns[4]*(stds[4]**2+b_ds[4]**2)))/(ns[0]+ns[1]+ns[2]+ns[3]+ns[4]))

a_sig=np.sqrt(((ns[5]*(stds[5]**2+a_ds[0]**2))+(ns[6]*(stds[6]**2+a_ds[1]**2))
               +(ns[7]*(stds[7]**2+a_ds[2]**2))+(ns[8]*(stds[8]**2+a_ds[3]**2))
               +(ns[9]*(stds[9]**2+a_ds[4]**2)))/(ns[5]+ns[6]+ns[7]+ns[8]+ns[9]))

print(b_ms)
print(b_sig)
print ('\n')
print(a_ms)
print(a_sig)
#%%Violin plots of modulus distribution of WT

from matplotlib import pyplot as plt
plt.style.use('default')
import seaborn as sns
import numpy as np
import os
import matplotlib as mpl

mpl.rcParams['axes.linewidth'] = 0.5 #set the value globally

def cm_to_inch(value):
    return value/2.54

fig,ax = plt.subplots(figsize=(cm_to_inch(6),cm_to_inch(2.7)), linewidth=0.5)
dy="Modulus"; dx = "Group"; dhue="File"

# make a plot
# palette = 'YlOrBr'
palette = ["#bec5c6","#546a77"]

ax = sns.violinplot(y = dy, x=dx, data=result2,
                    palette=palette,showmeans=True,
                    scale="count", inner=None,linewidth=0.1,color='k')
for violin in ax.collections:
    ax.collections[0].set_edgecolor('k')
    ax.collections[1].set_edgecolor('k')

# sns.boxplot(y = dy, x=dx, data=result2, saturation=0.75,linewidth= 0.25, width=0.075,
#             palette=palette, boxprops={'zorder': 2},showfliers=False, ax=ax)


sns.pointplot(y = dy, x=dx, markers='o',scale=0.2,join=False, ci='sd',errwidth=0.5,capsize=0.025,color='black', data=result2)


# plt.ylim(-2, 40)
min_ylim, max_ylim = plt.ylim()

plt.text(b_ms*0.0025, max_ylim*0.6, '$\mu={:.2f}$ MPa'.format(b_ms), fontsize=6,color='k')
plt.text(a_ms*0.055, max_ylim*0.6, '$\mu={:.2f}$ MPa'.format(a_ms), fontsize=6,color='k')

xlim = ax.get_xlim()
ylim = ax.get_ylim()
# ylim = 100


plt.setp(ax.artists, edgecolor = 'k')  
plt.setp(ax.lines, color='k')
old_len_collections = len(ax.collections)

# set y-axis label
ax.set_ylabel("Modulus (MPa)",color="k",fontsize=7)
# set x-axis label
ax.set_xlabel("Polymyxin",color="k",fontsize=7)

ax.tick_params(axis='x', labelsize=7,width=0.5 )
ax.tick_params(axis='y', labelsize=7,width=0.5)


x_ticks_labels=['(-)','(+)']
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=7)

plt.yticks([0,25,50,75,100],fontsize=7,fontname = "Arial",color='k', visible=True)
# plt.yticks([0,10,20,30,40,50],fontsize=8,fontname = "Arial",color='k', visible=True)
# plt.yticks([0,10,20,30,40],fontsize=8,fontname = "Arial",color='k', visible=True)


# plt.xticks()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.tick_params(axis = 'x',  length = 0)

ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.ylim(-5, 100)


plt.show()

# #  Save figure  # # 
path = "/Users/selenm/polybox/Colistin_Project_Collab/Selen/Modulus_calc/Main_modulus_fig/WT"

# Change the directory
os.chdir(path) 
 
# fig.savefig('WT_Modulus_Main.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)


#%% Statistical test for WT

# stat, p =mannwhitneyu(result2[(result2["Group"] == 'PBS')].Modulus,result2[(result2["Group"] == 'Polymyxin')].Modulus)

before=[ms[0],ms[1],ms[2],ms[3],ms[4]]
after =[ms[5],ms[6],ms[7],ms[8],ms[9]]

stat, p =mannwhitneyu(before,after)
print('Statistics=%.3f, p=%.6f' % (stat, p))

