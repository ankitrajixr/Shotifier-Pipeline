import pandas as pd
import numpy as np
import math
import zone_classifier
import plot_color_zones

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


def classifyPriorZonesCSV():
    
    priorEventDetails = pd.read_csv('prior_event.csv')
    #convert the percent of (x,y) data to 104*68 dimensions
    (x_start,y_start)=scaling_axis(priorEventDetails['x start'],priorEventDetails['y start'])
    (x_stop,y_stop)=scaling_axis(priorEventDetails['x stop'],priorEventDetails['y stop'])
    #fetch the zones for a given (x,y)
    cooridnates = {'eventId':priorEventDetails['id'],'playerId':priorEventDetails['playerId'],'teamId':priorEventDetails['teamId'],'eventName':priorEventDetails['eventName'],'subEventName':priorEventDetails['subEventName'],'x_start':x_start,'y_start':y_start,'x_stop':x_stop,'y_stop':y_stop,'tags':priorEventDetails['tags1']}
    cooridnates_df = pd.DataFrame(cooridnates, columns = ['eventId','playerId','teamId','eventName','subEventName','x_start','y_start','x_stop','y_stop','tags'])

    s_zone = [zone_classifier.zone_classifier(cooridnates_df.iloc[i,5],cooridnates_df.iloc[i,6]) for i in range(len(cooridnates_df))]
    e_zone = [zone_classifier.zone_classifier(cooridnates_df.iloc[i,7],cooridnates_df.iloc[i,8]) for i in range(len(cooridnates_df))]

    cooridnates_df['start_zone'] = s_zone
    cooridnates_df['end_zone'] = e_zone

    cooridnates_df.to_csv('prior_events_zone_classified.csv')
    print("done")

def fetchTeamEvents(teamId, df):

    is_team = df['teamId'] == int(teamId)
    return df[is_team]

# classifyPriorZonesCSV()
general_prior_event_zone_df = pd.read_csv('prior_events_zone_classified.csv', index_col=0)
general_event_zone_df = pd.read_csv('events_zone_classified.csv', index_col=0)

value =  input("Do you want fetch prior event details w.r.t a team? (y/n): ")
if value.lower() == 'y':
    teamId = input("Enter team ID: ")
    prior_event_zone_df = fetchTeamEvents(teamId, general_prior_event_zone_df)
        # print(event_zone_df.head(10))
    count_event_zone_df = fetchTeamEvents(teamId, general_event_zone_df)

else: 
    prior_event_zone_df = general_prior_event_zone_df
    count_event_zone_df = general_event_zone_df

max_zone_activity_df = count_event_zone_df['start_zone'].value_counts().rename_axis('start_zone').reset_index(name='event_counts')
    
is_goal = count_event_zone_df['tags'] == 101
zone_goals_df = count_event_zone_df[is_goal]
count_zone_goals_df = zone_goals_df['start_zone'].value_counts().rename_axis('start_zone').reset_index(name='goal_counts')
zone_goal_events_count_df = max_zone_activity_df.merge(count_zone_goals_df, how='left', left_on = 'start_zone', right_on = 'start_zone')
print(zone_goal_events_count_df)

i=0
while i<3: 
    zone = input("Enter the zone: ")
    is_prior_zone = prior_event_zone_df['end_zone'] == zone
    zone_df = prior_event_zone_df[is_prior_zone]

    prior_zone_percent_df =  zone_df['start_zone'].value_counts(normalize=True).rename_axis('priorZone').reset_index(name='percent')
    plot_color_zones.zoneInteractionsColored(prior_zone_percent_df)
    i=i+1
