import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Infocambio_cinematico.csv")
fuelFinish = False 
dfFuel = df[df[' instFuel'] != 0]
dfNotFuel = df[(df[' instFuel'] == 0) & (df[' Height'] > 0)]

if len(list(dfNotFuel['Seconds'])) != 0:
    fuelFinish = True



if fuelFinish :
    #Acceleration
    figA, axsA = plt.subplots(figsize=(12, 6))
    axsA.plot(dfFuel['Seconds'], dfFuel[' Acceleration Y'])
    plt.grid()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    axsA.set_xlabel('Time', labelpad=10, fontsize = 14)  
    axsA.xaxis.set_label_coords(1.05, 0.01) 
    axsA.set_ylabel('Acceleration', labelpad=10, rotation= 0, fontsize = 14 )  
    axsA.yaxis.set_label_coords(0.02, 1.02)
    axsA.set_xlim(0, max(dfFuel["Seconds"]))
    axsA.set_ylim(min(dfFuel[' Acceleration Y']), max(dfFuel[' Acceleration Y']) + 20)
    axsA.set_title('Acceleration Y While Fuel Supported ')
    plt.savefig('Acceleration Y over time While Fuel Supported.png')

    figA2, axsA2 =plt.subplots(figsize=(12, 6))
    axsA2.plot(df['Seconds'], df[' Acceleration Y'])
    plt.grid()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    axsA2.set_xlabel('Time (s)', labelpad=10, fontsize = 14)  
    axsA2.xaxis.set_label_coords(1.05, 0.01) 
    axsA2.set_ylabel('Acceleration Y (m/s^2)', labelpad=10, rotation= 0, fontsize = 14 )  
    axsA2.yaxis.set_label_coords(0.02, 1.02)
    axsA2.set_title(' General Acceleration Y', fontsize = 20)
    axsA2.set_xlim(0, max(df['Seconds']))
    axsA2.set_ylim(min(df[" Acceleration Y"])-1, max(df[" Acceleration Y"])+20)
    plt.savefig('Acceleration Y over time General.png')

    #Speed
    figV, axV = plt.subplots()
    axV.plot(dfFuel['Seconds'], dfFuel[' Speed Y'])
    plt.grid()
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axV.set_xlabel('Time', labelpad=10, fontsize = 12)  
    axV.xaxis.set_label_coords(1.05, 0.01) 
    axV.set_ylabel('Speed Y', labelpad=10, rotation= 0, fontsize = 12 )  
    axV.yaxis.set_label_coords(0.02, 1.02)
    axV.set_xlim(0, max(dfFuel['Seconds']))
    axV.set_ylim(min(dfFuel[' Speed Y']), max(dfFuel[' Speed Y'])+300)
    axV.set_title('Speed Y over Time while fuel supported')
    plt.savefig('Speed Y over time while fuel supported')

    figV2, axV2 = plt.subplots()
    axV2.plot(df['Seconds'], df[' Speed Y'])
    plt.grid()
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axV2.set_xlabel('Time (s)', labelpad=10, fontsize = 12)  
    axV2.xaxis.set_label_coords(1.03, -0.07) 
    axV2.set_ylabel('Speed Y (m/s)', labelpad=10, rotation= 0, fontsize = 12)  
    axV2.yaxis.set_label_coords(0.02, 1.02)
    axV2.set_xlim(0, max(df['Seconds'],))
    axV2.set_ylim(0, max(df[' Speed Y'])+300)
    axV2.set_title('Speed Y over Time general ')
    plt.savefig('Speed Y over time general.png')

    #Height
    figPY, axPY = plt.subplots()
    axPY.plot(dfFuel['Seconds'], dfFuel[' Height'])
    plt.grid()
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axPY.set_xlabel('Time', labelpad=10, fontsize = 12)  
    axPY.xaxis.set_label_coords(1.05, 0.01) 
    axPY.set_ylabel('Height', labelpad=10, rotation= 0, fontsize = 12 )  
    axPY.yaxis.set_label_coords(0.02, 1.02)
    axPY.set_xlim(0, max(dfFuel['Seconds']))
    axPY.set_ylim(0, max(dfFuel[' Height'])+50)
    axPY.set_title('Height over Time while fuel supported')
    plt.savefig('Height over time while fuel supported')

    figPY2, axPY2 = plt.subplots()
    axPY2.plot(df['Seconds'], df[' Height'])
    plt.grid()
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axPY2.set_xlabel('Time (s)', labelpad=10, fontsize = 12)  
    axPY2.xaxis.set_label_coords(1.03, -0.07) 
    axPY2.set_ylabel('Height (m)', labelpad=10, rotation= 0, fontsize = 12 )  
    axPY2.yaxis.set_label_coords(0.02, 1.05)
    axPY2.set_xlim(0, max(df['Seconds'],))
    axPY2.set_ylim(0, max(df[' Height'])+100000)
    axPY2.set_title('Height over Time general ', fontsize = 15)
    plt.savefig('Height over time general.png')

    #X against Height

    figT, axT = plt.subplots()
    axT.plot(dfFuel[' Delta X'], dfFuel[' Height'])
    plt.axis('equal')
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axT.set_xlabel('X', labelpad=10, fontsize = 14)  
    axT.xaxis.set_label_coords(1.05, 0.01) 
    axT.set_ylabel('Y', labelpad=10, rotation= 0, fontsize = 14 )  
    axT.yaxis.set_label_coords(0.0001, 1.03)
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
    axT.set_xlim(0, max(dfFuel[' Delta X'])+50)
    axT.set_ylim(0, max(dfFuel[' Height'])+10000)
    axT.set_title('Trajectory while fuel supported')
    plt.savefig('Trajectory while fuel supported')

    figT2, axT2 = plt.subplots()  
    axT2.plot(df[' Delta X'], df[' Height'])
    plt.axis('equal')
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axT2.set_xlabel('X', labelpad=10, fontsize = 14)  
    axT2.xaxis.set_label_coords(1.05, 0.01) 
    axT2.set_ylabel('Y', labelpad=10, rotation= 0, fontsize = 14 )  
    axT2.yaxis.set_label_coords(0.0001, 1.03)
    plt.ticklabel_format(style='sci', axis='both', scilimits=(0, 0))
    axT2.set_xlim(0, max(df[' Delta X']+50))
    axT2.set_ylim(0, max(df[' Height'])+10000)
    axT2.set_title('Trajectory General ')
    plt.savefig('Trajectory  General.png')

else :
    #Acceleration
    figA, axA = plt.subplots()
    axA.plot(dfFuel['Seconds'], dfFuel[' Acceleration'])
    axA.set_xlim(0, max(dfFuel["Seconds"]))
    axA.set_ylim(min(dfFuel[' Acceleration']), max(dfFuel[' Acceleration']))
    axA.set_xlabel('Seconds')
    axA.set_ylabel('Acceleration')
    axA.set_title('Acceleration over Time while fuel supported')
    plt.savefig('Acceleration over time While Fuel Supported.png')

    #Speed
    figV, axV = plt.subplots()
    axV.plot(dfFuel['Seconds'], dfFuel[' Total Speed'])
    axV.set_xlim(0, max(dfFuel['Seconds']))
    axV.set_ylim(0, max(dfFuel[' Total Speed'])+5)
    axV.set_title('Speed over Time while fuel supported')
    plt.savefig('Speed over time while fuel supported')

    #Height
    figPY, axPY = plt.subplots()
    axPY.plot(dfFuel['Seconds'], dfFuel[' Height'])
    axPY.set_xlim(0, max(dfFuel['Seconds']))
    axPY.set_ylim(0, max(dfFuel[' Height'])+50)
    axPY.set_title('Height over Time while fuel supported')
    plt.savefig('Height over time while fuel supported')

    #Trajectory

    figT, axT = plt.subplots()
    axT.plot(dfFuel[' Delta X'], dfFuel[' Height'])
    axT.set_xlim(0, max(dfFuel[' Delta X']))
    axT.set_ylim(0, max(dfFuel[' Height'])+50)
    axT.set_title('Trajectory while fuel supported')
    plt.savefig('Trajectory General.png')



