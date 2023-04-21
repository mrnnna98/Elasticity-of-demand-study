# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:41:17 2022

@author: annam
"""

#THIS CODE SHOULD BE USED IN ORDER TO CALL RAMP CALL MICROGRID AND FIND OUT 
#WHAT WOULD BE THE OUTCOME OF A CHENGE IN PRICE IN TERM OF CHANGE IN QUANTITY 
#AND OPTIMAL ALLOCATION OF THE PRICE IN ORDER TO MAXIMISE THE REVENEW

#%% Import required modules
import sys,os
import pandas as pd
import numpy as np 
import xlwt
from os.path import exists
sys.path.append(r'C:\Users\annam\RAMP-master (2)\ramp')
import config
import importlib
import matplotlib.pyplot as plt
#___________________________________________________________________________________________________________________

#definition of functions
#calculation of revenue
def revenue_calc(filepath_demand, filepath_LCOE,price,price_change):
    df_dict = pd.read_excel(filepath_demand, sheet_name=None) #load Excel file using Pandas with `sheet_name=None`
    df_all = pd.concat(df_dict.values(), ignore_index=True) # combine data from all worksheets
    demand = df_all['Scenario 1'] #select only the first column of demand
    demand = pd.to_numeric(demand, errors='coerce') #change whatever is not a number to a nan
    demand.dropna(axis=0, how='any', inplace=True) #delete all the raws which contain nans
    totdemand_kwh = (demand.sum())/1000 #sum the demand of the 20 years and devides by 1000 to get the kWh
    
    df_dict = pd.read_excel(filepath_LCOE, 'Cost') #load Excel sheet 'cost' file using Pandas 
    LCOE = df_dict.iloc[5,4]
    print('LCOE:',LCOE)
    revenue = (price*(1+price_change)-LCOE)*totdemand_kwh #here it considers the change in price considering the price setted in the begining and adding the change in price 
    return(totdemand_kwh, LCOE, revenue)

#take the needed variable from the results, save it in right xlsx format and pass it to the microgrid directory (this function is done for 2 stocastic processes)
def demand_mgp_2(j):
    #from minutes output to hours output (making the mean within 60 values so that to get mean hourly)
    df1 = pd.read_csv(r'C:\Users\annam\RAMP-master (2)\ramp\results\output_file_ela_1.csv') #read the csv output where is applied elasticity from ramp
    df1.drop(columns = df1.columns[0], axis = 1, inplace= True) #drop the colum that contains the minutes count
    df1_hours = df1.groupby(np.arange(len(df1))//60).mean() #make the average of 60 minutes in order to get the hourly demand
    # if len(df1)/60 == len(df1_hours): #this is just to check the division is correct but it is
    #   print("fine")
    # else:
    #   print("error")  
    df1_hours.index = np.arange(1, len(df1_hours) + 1) #change the row index making it starting from 1
    df1_hours.columns = pd.RangeIndex(1, len(df1_hours.columns)+1) #change the column index making it starting from 1
    
    #from 2 days here concat in order to get a 365 dataframe (if it is 73 days range(1,6))
    df_desired = pd.DataFrame()
    for i in range(1,184): #the for loop concatenate the 48 hours in order to get a whole dataframe (it is more then 8760 so later i have to drop some rows)
        df_desired = pd.concat([df_desired, df1_hours])
        
    index = [] #put the correct index bacause also the indexes are concatenated in the for loop and therefore thy repeat from 1 to 48
    for i in range(1,8785):
        index.append(i)  
    df_desired.index = index
    df_desired = df_desired.iloc[:-24,:]#drop the last 24 rows
    #print (df_desired)
    
    for x in range(2,21): #repeat the first column until 20th
        df_desired['{}'.format(x)] = df_desired[1]
        
    df_desired.columns = df_desired.columns.astype(int)    

    #check if the file demand already exist in microgrid directory and if yes rename it and then save the new demand
    file_exists = exists(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs\Demand.xls') #checking if the file Demand already exists 
    
    if file_exists == True: #if the file exists rename it, then it should be renamed in relation ot the number of iteration 
        old_file = os.path.join(r"C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs", "Demand.xls")
        new_file = os.path.join(r"C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs", "Demand_before%f.xls" %j)
        os.rename(old_file, new_file)
    else:
        pass
    
    df_desired.to_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs\Demand.xls') #save the dataframe as new Demand file 
    
    
def demand_mgp_5(j): #this is for 5 days of stocasthic process
    #from minutes output to hours output (making the mean within 60 values so that to get mean hourly)
    df1 = pd.read_csv(r'C:\Users\annam\RAMP-master (2)\ramp\results\output_file_ela_1.csv') #read the csv output where is applied elasticity from ramp
    df1.drop(columns = df1.columns[0], axis = 1, inplace= True) #drop the colum that contains the minutes count
    df1_hours = df1.groupby(np.arange(len(df1))//60).mean() #make the average of 60 minutes in order to get the hourly demand
    # if len(df1)/60 == len(df1_hours): #this is just to check the division is correct but it is
    #   print("fine")
    # else:
    #   print("error")  
    df1_hours.index = np.arange(1, len(df1_hours) + 1) #change the row index making it starting from 1
    df1_hours.columns = pd.RangeIndex(1, len(df1_hours.columns)+1) #change the column index making it starting from 1
    
    #from 2 days here concat in order to get a 365 dataframe (if it is 73 days range(1,6))
    df_desired = pd.DataFrame()
    for i in range(1,74): #the for loop concatenate the 48 hours in order to get a whole dataframe (it is more then 8760 so later i have to drop some rows)
        df_desired = pd.concat([df_desired, df1_hours])
        
    index = [] #put the correct index bacause also the indexes are concatenated in the for loop and therefore thy repeat from 1 to 48
    for i in range(1,8761):
        index.append(i)  
    df_desired.index = index

    
    for x in range(2,21): #repeat the first column until 20th
        df_desired['{}'.format(x)] = df_desired[1]
        
    df_desired.columns = df_desired.columns.astype(int)    

    #check if the file demand already exist in microgrid directory and if yes rename it and then save the new demand
    file_exists = exists(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs\Demand.xls') #checking if the file Demand already exists 
    
    if file_exists == True: #if the file exists rename it, then it should be renamed in relation ot the number of iteration 
        old_file = os.path.join(r"C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs", "Demand.xls")
        new_file = os.path.join(r"C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs", "Demand_before%f.xls" %j)
        os.rename(old_file, new_file)
    else:
        pass
    
    df_desired.to_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Inputs\Demand.xls') #save the dataframe as new Demand file     
    
    
def Revenue_plot(Revenue):
    #x = np.arange(0,1440,5)
    plt.figure(figsize=(10,5))
    plt.plot(np.arange(len(Revenue)),Revenue,'#4169e1')
    #plt.xlabel('Time (hours)')
    plt.ylabel('Net revenue')
    plt.xlabel('Percentual price change')
    plt.ylim(ymin=0)
    #plt.ylim(ymax=5000)
    plt.margins(x=0)
    plt.margins(y=0)
    #plt.xticks([0,240,480,(60*12),(60*16),(60*20),(60*24)],[0,4,8,12,16,20,24])
    #plt.savefig('profiles.eps', format='eps', dpi=1000)
    plt.show()    

#___________________________________________________________________________________________________________________

#import needed parameters from config module 
price = config.price #define price from config
elasticity = config.elasticity #define elasticity from config
price_change = config.price_change #define price-change from config
pc_file = open(r'C:\Users\annam\RAMP-master (2)\ramp\price_change.txt', 'w') #file for price change 
pc_file.write(str(price_change))
pc_file.close()
pc_file = open(r'C:\Users\annam\RAMP-master (2)\ramp\price_change.txt', "r")
price_change = float(pc_file.read())

#revenue from the opt zero without chnage in price and therefore in demand
totdemand_kwh_0, LCOE_0, revenue_0 = revenue_calc(r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\Ramp e microgrid inputs\microgrids opt\opt NPC\Results\Time_Series.xlsx' , 
                                                    r'C:\Users\annam\OneDrive - Politecnico di Milano\Desktop\uni\ricerca\Ramp e microgrid inputs\microgrids opt\opt NPC\Results\Results_Summary.xlsx',
                                                    price,0) #import first optimization demand and Lcoe
Revenue_list = [revenue_0]
LCOE_list = [LCOE_0]
Totdemand_kwh_list = [totdemand_kwh_0]
j_list = [0]

#import and run ramp modules
sys.path.append('C:/Users/annam/RAMP-master (2)/ramp')
import ramp_run

#create the new demand for microgrid
demand_mgp_5(0.7)

#import and run microgrids modules  
sys.path.append(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code')
import Micro_Grids

print('this is price change', price_change)
#calculate the new revenue with updated parameters from optimization
totdemand_kwh, LCOE, revenue = revenue_calc(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Time_Series.xlsx' , 
                                              r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx',
                                              price,price_change)
print('this is revenue', revenue)
Revenue_list.append(revenue)
LCOE_list.append(LCOE)
Totdemand_kwh_list.append(totdemand_kwh)
j_list.append(price_change)

#_______________________________________________________________________________________________________________________

#outside for loop try

# #upload the  txt file that will be read by ramp on the next iteration to create the uploaded demand
# pc_file = open(r'C:\Users\annam\RAMP-master (2)\ramp\price_change.txt', 'w') #file for price change 
# new_price_change = 0.15
# pc_file.write(str(new_price_change))
# pc_file.close()
# pc_file = open(r'C:\Users\annam\RAMP-master (2)\ramp\price_change.txt', "r")
# new_new_price_change = pc_file.read()
# print('this is new new price change', new_new_price_change)

# #reload the module every time the code is repeated in the for loop
# importlib.reload(ramp_run)

# #create the new demand for microgrid
# demand_mgp(0.15)

# #reload microgrid to optimise the new load demand
# del sys.modules['Micro_Grids']
# del Micro_Grids
# import Micro_Grids

# #calculate the new revenue with updated parameters from optimization
# totdemand_kwh, LCOE, revenue = revenue_calc(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Time_Series.xlsx' , 
#                                               r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx',
#                                               price)
# Revenue.append(revenue) #add the new revenue (being revenue the difference between price and lcoe multiplied y the total demand)       
# print('this is the revenue list', Revenue)
# Revenue_plot(Revenue)

#__________________________________________________________________________________________________________________________

#iterate the process for the desired change in price 
for j in np.arange(0.71, 0.9, 0.01): #qui crea il config price solo con 0.15 test NB!!! GUARDA CHE QUI IL PRIMO DEI DUE NUMERI E' IL PRICE CHANGE DI PARTENZA
    
    #upload the  txt file that will be read by ramp on the next iteration to create the uploaded demand
    pc_file = open(r'C:\Users\annam\RAMP-master (2)\ramp\price_change.txt', 'w') #file for price change 
    new_price_change = j
    pc_file.write(str(new_price_change))
    pc_file.close()
    pc_file = open(r'C:\Users\annam\RAMP-master (2)\ramp\price_change.txt', "r")
    new_new_price_change = float(pc_file.read())
    print('this is new new price change', new_new_price_change)
    
    #reload the module every time the code is repeated in the for loop
    importlib.reload(ramp_run)
    
    #create the new demand for microgrid
    demand_mgp_5(j)

    #reload microgrid to optimise the new load demand
    del sys.modules['Micro_Grids']
    del Micro_Grids
    import Micro_Grids
    
    #calculate the new revenue with updated parameters from optimization
    totdemand_kwh, LCOE, revenue = revenue_calc(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Time_Series.xlsx' , 
                                                  r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx',
                                                  price,new_new_price_change)
    

    print('this is revenue', revenue)
    Revenue_list.append(revenue)
    print('this is the revenue list', Revenue_list)
    LCOE_list.append(LCOE)
    Totdemand_kwh_list.append(totdemand_kwh)
    j_list.append(j)
    
    df1 = pd.read_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx','Size')
    df2 = pd.read_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx','Cost')
    df3 = pd.read_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx','Yearly cash flows')
    df4 = pd.read_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\Results\Results_Summary.xlsx','Yearly energy parameters')
    
    with pd.ExcelWriter(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\summary\Summary%f.xlsx'%j) as writer:
           df1.to_excel(writer, sheet_name='Size')
           df2.to_excel(writer, sheet_name='Cost')
           df3.to_excel(writer, sheet_name='Yearly cash flows')
           df4.to_excel(writer, sheet_name='Yearly energy parameters')
        
    
print('this is the revenue list', Revenue_list)
Revenue_plot(Revenue_list)

dc_econ_param = {
    'Iteration': j_list,
    'Totdemandkwh': Totdemand_kwh_list,
    'LCOE': LCOE_list,
    'Revenue': Revenue_list
          }
df_econ_param = pd.DataFrame(dc_econ_param)
df_econ_param.to_excel(r'C:\Users\annam\MicroGridsPy-SESAM-MYCE\Code\summary\Summary_tot.xlsx')

    
