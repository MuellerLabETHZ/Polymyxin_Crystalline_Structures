#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:46:45 2022

@author: selenm
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:12:35 2021

@author: selenm
"""

# cm=1/2.54


import os
# import glob 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def cm_to_inch(value):
    return value/2.54

# Folder Path
path = "/Users/selenm/polybox/Colistin_Project_Collab/Selen/Modulus_calc/SI_modulus_fig/Modulus_titration"
# Change the directory
os.chdir(path)

Mod_d1 = pd.read_csv("Patch1_Modulus_Titration.csv")
Mod_d2 = pd.read_csv("Patch2_Modulus_Titration.csv")
Mod_d3 = pd.read_csv("Patch3_Modulus_Titration.csv")
Mod_d4 = pd.read_csv("Patch4_Modulus_Titration.csv")

frames = [Mod_d1, Mod_d2, Mod_d3, Mod_d4]
Modulus_dat = pd.concat(frames)
Mod_dat=Modulus_dat[Modulus_dat.Modulus<100]

Mod_dat.groupby(["File"])['Modulus'].mean()

#%%
import matplotlib as mp

fig = plt.figure(figsize=(cm_to_inch(5.5),cm_to_inch(2.25)),linewidth=0.25)


# fig.suptitle('MCR-1', fontsize=fs+2,fontname = "Arial")
# axes[0].set_xlabel('PBS', fontsize=fs,fontname = "Arial") 
# axes[1].set_xlabel('+Colistin', fontsize=fs,fontname = "Arial")


# #Remove the modulus values for 0.1ug/L concentration
# Modulus_dat.drop(Modulus_dat.loc[Modulus_dat['Concentration']==1].index, inplace=True)


# palet=sns.color_palette("YlOrBr", as_cmap=True)
# reversed_pal=palet.reversed()


ax=sns.boxplot(x='Concentration',y='Modulus',data=Mod_dat,linewidth=0.5,
               boxprops={'edgecolor':'black'},
               medianprops={'color':'black'},
               whiskerprops={'color':'black'},
               capprops={'color':'black'},
                showmeans=True,
            meanprops={"marker":"o",
                        "markerfacecolor":"white", 
                        "markeredgecolor":"black",
                      "markersize":"2.5"},palette='YlOrBr_r',showfliers=False)



# means=[]
# for i in range(deformation.Concentration.nunique()):
#     means.append(np.mean(deformation[deformation.Concentration == str(i)].Modulus))

# axes=sns.regplot(x='Concentration',y='Modulus',data=deformation,x_estimator=means)

fs=8
ls=8
ax.legend().set_visible(False)
ax.set_ylabel('Modulus (MPa)', fontsize=fs,fontname = "Arial") 
ax.set_xlabel('Concentration (mg/l)', fontsize=fs,fontname = "Arial")

ax.set_xticks([0,1,2,3,4])
ax.set_xticklabels(['0','0.3','0.6','6','60'],fontsize=fs,fontname = "Arial")
ax.set_yticks([0,20,40,60])
ax.set_yticklabels(['0','20','40','60'],fontsize=fs,fontname = "Arial")
# plt.ylim(0,60)
ax.tick_params(axis="x", labelsize=ls, length=2,width=0.5)
ax.tick_params(axis="y", labelsize=ls, length=2,width=0.5)

# fig.savefig('/Users/selenm/polybox/Colistin_Project_Collab/Selen/Modulus_calc/SI_modulus_fig/Modulus_titration/Modulus_titration.pdf', format='pdf',  dpi=600, bbox_inches = 'tight',pad_inches=0.01)
