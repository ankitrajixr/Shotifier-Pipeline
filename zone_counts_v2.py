import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import classifyToZonesCSV

def zoneGoalEventsCount():

    #classifyToZonesCSV.classifyToZonesCSV()

    event_zone_df = pd.read_csv('events_zone_classified.csv', index_col=0)
    # print(event_zone_df.head(10))
     
    max_zone_activity_df = event_zone_df['start_zone'].value_counts().rename_axis('start_zone').reset_index(name='event_counts')
    
    is_goal = event_zone_df['goal'] == 1
    zone_goals_df = event_zone_df[is_goal]
    count_zone_goals_df = zone_goals_df['start_zone'].value_counts().rename_axis('start_zone').reset_index(name='goal_counts')
    # print(count_zone_goals_df)
    
    zone_goal_events_count_df = max_zone_activity_df.merge(count_zone_goals_df, how='left', left_on = 'start_zone', right_on = 'start_zone')
    # print(zone_goal_events_count_df)
    
    return zone_goal_events_count_df
