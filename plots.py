# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:44:17 2023

@author: annam
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams

##PLOT ON THE SENSITIVITY
#df = pd.read_excel(r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\graph_sensitivity.xlsx')
##print(df)
#boxplot = df.boxplot()
#SMALL_SIZE = 12
#MEDIUM_SIZE = 15
#BIGGER_SIZE = 15
#plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
##    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#plt.xlabel("Increase of initial price [%]")
#plt.ylabel("Operational profit [kUSD]")
#boxplot = df.boxplot(grid=False, rot=45)
#mpl.rc('figure', figsize=(10, 7))
##plt.ticklabel_format(axis='y', scilimits=[0, 1])
#plt.show()

##PLOT ON THE ELASTICITY CHANGE
#plt.rcParams.update(plt.rcParamsDefault)
#plt.style.use('seaborn-colorblind')
#df1 = pd.read_excel(r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\elasticity change.xlsx')
#print(df1)
#fig, ax = plt.subplots(figsize=(10, 7))
#plt.ylim([0,3000000])
##plt.style.use('seaborn-white')
#ax = plt.subplot(111, xlabel='Increase of initial price [%]', ylabel='Operational profit [kUSD]')
#for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
#          ax.get_xticklabels() + ax.get_yticklabels()):
#    item.set_fontsize(15)
#plt.ylim([0,3000])
#index = df1.index
##print(index)
#ax.plot(index*100, df1.iloc[:,0], label='Elasticity -0,1')
#ax.plot(index*100, df1.iloc[:,1], label='Elasticity -0,2')
#ax.plot(index*100, df1.iloc[:,2], label='Elasticity -0,3')
#ax.plot(index*100, df1.iloc[:,3], label='Elasticity -0,4')
#ax.plot(index*100, df1.iloc[:,5], label='Elasticity -0,6')
#ax.plot(index*100, df1.iloc[:,4], label='Elasticity -0,5')
#ax.plot(index*100, df1.iloc[:,6], label='Elasticity -0,7')
#ax.plot(index*100, df1.iloc[:,7], label='Elasticity -0,8')
#ax.plot(index*100, df1.iloc[:,8], label='Elasticity -0,9')
#ax.plot(index*100, df1.iloc[:,9], label='Elasticity -1')
##plt.style.use('seaborn-white')
#plt.legend(fontsize=12)
#plt.show()


#cut the graph after zero. and mark the maximum point with an x or something 
#maybe also remove the extreme. and removre everthing below zero and make it higher 




##PLOT OF 0,6043 ELESTICITY CURVE
#
#iteration = range(0, 180, 10)
#profit = [0,
# 217.068,
# 424.551,
# 578.183,
# 705.651,
# 802.042,
# 887.272,
# 921.493,
# 955.618,
# 938.233,
# 904.332,
# 843.348,
# 753.692,
# 635.800,
# 488.817,
# 318.770,
# 121.949,
# -168.103]
#
#fig, ax = plt.subplots(figsize=(10, 5))
#ax = plt.subplot(111, xlabel='Increase of initial price [%]', ylabel='Operational profit [kUSD]')
#for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
#             ax.get_xticklabels() + ax.get_yticklabels()):
#    item.set_fontsize(15)
#plt.ylim([0,1200])
#plt.style.use('seaborn-colorblind')
#ax.plot(iteration, profit)
#plt.show()




##PLOT ON THE SENSITIVITY
#iteration = range(73, 91, 1)
#df = pd.read_excel(r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\graph_sensitivity.xlsx')
#fig, ax = plt.subplots(figsize=(10, 3))
#plt.ylim([930000,960000])
#plt.style.use('seaborn-colorblind')
#plt.xlabel("Increase of initial price [%]")
#plt.ylabel("Operational profit [USD]")
#ax = plt.subplot(111, xlabel='Increase of initial price [%]', ylabel='Operational profit [kUSD]')
#for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
#             ax.get_xticklabels() + ax.get_yticklabels()):
#    item.set_fontsize(15)
#ax.plot(iteration, df.iloc[0,:], label='elasticity -0,1')
#ax.plot(iteration, df.iloc[1,:], label='elasticity -0,2')
#ax.plot(iteration, df.iloc[2,:], label='elasticity -0,3')
#ax.plot(iteration, df.iloc[3,:], label='elasticity -0,4')
#ax.plot(iteration, df.iloc[5,:], label='elasticity -0,6')
#ax.plot(iteration, df.iloc[4,:], label='elasticity -0,5')
#ax.plot(iteration, df.iloc[6,:], label='elasticity -0,7')
#ax.plot(iteration, df.iloc[7,:], label='elasticity -0,8')
#plt.show()



#DEMAND PLOT
def Profile_demands_ela(filepath_demand_a, filepath_demand_b, filepath_demand_c,filepath_demand_d, 
                        filepath_demand_e, filepath_demand_f,filepath_demand_g, filepath_demand_h,
                        filepath_demand_i, filepath_demand_l,filepath_demand_m, filepath_demand_n,
                        filepath_demand_o,filepath_demand_p,filepath_demand_q,filepath_demand_r,
                        filepath_demand_s): #,filepath_demand_t,filepath_demand_u,filepath_demand_v):
    df_a = pd.read_excel(filepath_demand_a)
    df_b = pd.read_excel(filepath_demand_b)
    df_c = pd.read_excel(filepath_demand_c)
    df_d = pd.read_excel(filepath_demand_d)
    df_e = pd.read_excel(filepath_demand_e)
    df_f = pd.read_excel(filepath_demand_f)
    df_g = pd.read_excel(filepath_demand_g)
    df_h = pd.read_excel(filepath_demand_h)
    df_i = pd.read_excel(filepath_demand_i)
    df_l = pd.read_excel(filepath_demand_l)
    df_m = pd.read_excel(filepath_demand_m)
    df_n = pd.read_excel(filepath_demand_n)
    df_o = pd.read_excel(filepath_demand_o)
    df_p = pd.read_excel(filepath_demand_p)
    df_q = pd.read_excel(filepath_demand_q)
    df_r = pd.read_excel(filepath_demand_r)
    df_s = pd.read_excel(filepath_demand_s)
    plt.style.use('seaborn-colorblind')
    plt.figure(figsize=(10,7))

    plt.plot(np.arange(25),df_a.iloc[:25,1]/1000,linewidth=1,label='0%')
    plt.plot(np.arange(25),df_b.iloc[:25,1]/1000,linewidth=1,label='10%')
    plt.plot(np.arange(25),df_c.iloc[:25,1]/1000,linewidth=1,label='20%')
    plt.plot(np.arange(25),df_d.iloc[:25,1]/1000,linewidth=1,label='30%')
    plt.plot(np.arange(25),df_e.iloc[:25,1]/1000,linewidth=1,label='40%')
    plt.plot(np.arange(25),df_f.iloc[:25,1]/1000,linewidth=1,label='50%')
    plt.plot(np.arange(25),df_g.iloc[:25,1]/1000,linewidth=1,label='60%')
    plt.plot(np.arange(25),df_h.iloc[:25,1]/1000,linewidth=1,label='70%')
    plt.plot(np.arange(25),df_i.iloc[:25,1]/1000,linewidth=1,label='80%')
    plt.plot(np.arange(25),df_l.iloc[:25,1]/1000,linewidth=1,label='90%')
    plt.plot(np.arange(25),df_m.iloc[:25,1]/1000,linewidth=1,label='100%')
    plt.plot(np.arange(25),df_n.iloc[:25,1]/1000,linewidth=1,label='110%')
    plt.plot(np.arange(25),df_o.iloc[:25,1]/1000,linewidth=1,label='120%')
    plt.plot(np.arange(25),df_p.iloc[:25,1]/1000,linewidth=1,label='130%')
    plt.plot(np.arange(25),df_q.iloc[:25,1]/1000,linewidth=1,label='140%')
    plt.plot(np.arange(25),df_r.iloc[:25,1]/1000,linewidth=1,label='150%')
    plt.plot(np.arange(25),df_s.iloc[:25,1]/1000,linewidth=1,label='160%')

    SMALL_SIZE = 12
    MEDIUM_SIZE = 15
    BIGGER_SIZE = 15
    plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.xlabel('Time [hours]')
    plt.ylabel('Power [KW]')
    plt.ylim([0,100])
    plt.legend(fontsize=12)
    plt.show()



Profile_demands_ela(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE_original\MicroGridsPy-SESAM-MYCE\Code\Inputs\Demand.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.200000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.300000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.400000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.500000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.600000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.700000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.800000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before0.900000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.000000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.100000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.200000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.300000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.400000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.500000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.600000.xls',
                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\figure\results 10% increase until double the lcoe\Demand_before1.700000.xls')





