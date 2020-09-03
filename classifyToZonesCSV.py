import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import zone_classifier

#############
#### Begin event_zone_classified.csv
## The below code is written to populate a csv that contains eventID, matchID, playerID, start(x,y), stop(x,y), start_zone, end_zone
#############
def scaling_axis(x_axis,y_axis):
    x=[]
    y=[]
    for i in x_axis:
        if math.isnan(i):
            x.append(999)
        else:
            x.append(i*1.04)
    for j in y_axis:
        if math.isnan(j):
            y.append(999)
        else:
            y.append(j*0.68)

    return (x,y)


def classifyToZonesCSV():
    
    forwardEventDetails = pd.read_csv('EventsForwardsData.csv')
    #convert the percent of (x,y) data to 104*68 dimensions
    (x_start,y_start)=scaling_axis(forwardEventDetails['x start'],forwardEventDetails['y start'])
    (x_stop,y_stop)=scaling_axis(forwardEventDetails['x stop'],forwardEventDetails['y stop'])
    #fetch the zones for a given (x,y)
    cooridnates = {'playerId':forwardEventDetails['playerId'],'x_start':x_start,'y_start':y_start,'x_stop':x_stop,'y_stop':y_stop,'goal':forwardEventDetails['tags']}
    cooridnates_df = pd.DataFrame(cooridnates, columns = ['playerId','x_start','y_start','x_stop','y_stop','goal'])

    s_zone = [zone_classifier.zone_classifier(cooridnates_df.iloc[i,1],cooridnates_df.iloc[i,2]) for i in range(len(cooridnates_df))]
    e_zone = [zone_classifier.zone_classifier(cooridnates_df.iloc[i,3],cooridnates_df.iloc[i,4]) for i in range(len(cooridnates_df))]

    cooridnates_df['start_zone'] = s_zone
    cooridnates_df['end_zone'] = e_zone

    cooridnates_df.to_csv('events_zone_classified.csv')
    print("done")
