########################################################################################################################################################################################
#   This code creates a combined KDE and scatterplots in which KDE plots show the activity of football forwards (Wingers,strikers and forwards) and scatter plot show the goals scored # 
#   Author: Sindhu Subramanya                                                                                                                                                          #  
########################################################################################################################################################################################

#importing libraries
import pymongo 
import pprint
import pandas as pd
import seaborn as sb                          
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot
import matplotlib.gridspec as gridspec
import numpy as np


#importing csv using pandas
footballForwards_df=pd.read_csv(r'C:/Users/Sindhu Subramanya/AppData/Local/Programs/Python/Python38/Data/EventsForwardsData.csv')
event_name = pd.read_csv(r'C:/Users/Sindhu Subramanya/AppData/Local/Programs/Python/Python38/Data/event_id_name.csv')
footballForwards_df.columns
event_name.columns


#Filters all events with respect to a particular Event Name  
def filter_event(event_name):
    data =footballForwards_df[(footballForwards_df.values==event_name )].dropna(how='all')
    return data

Duel_data = filter_event("Duel")
Foul_data = filter_event("Foul")
Free_Kick_data = filter_event("Free Kick")
Goalkeeper_leaving_line_data = filter_event("Goalkeeper leaving line")
Interruption_data = filter_event("Interruption")
Offside_data = filter_event("Offside")
Others_on_the_ball_data = filter_event("Others on the ball")
Pass_data = filter_event("Pass")
Save_attempt_data = filter_event("Save attempt")
Shot_data = filter_event("Shot")

#Filters all events with respect to a particular Event Name that ended in goal
def filter_event_goal(event_data):
    data_goal = event_data[(event_data['tags']==1)]
    return data_goal

Duel_data_goal = filter_event_goal(Duel_data)
Foul_data_goal = filter_event_goal(Foul_data)
print(len(Foul_data_goal))
Free_Kick_data_goal = filter_event_goal(Free_Kick_data)
print(len(Free_Kick_data_goal))
Goalkeeper_leaving_line_data_goal = filter_event_goal(Goalkeeper_leaving_line_data)
Interruption_data_goal = filter_event_goal(Interruption_data)
Offside_data_goal = filter_event_goal(Offside_data)
Others_on_the_ball_data_goal = filter_event_goal(Others_on_the_ball_data)
Pass_data_goal = filter_event_goal(Pass_data)
Save_attempt_data_goal = filter_event_goal(Save_attempt_data)
Shot_data_goal = filter_event_goal(Shot_data)

#correlation between goals and expected goals for indivisual events
#def correlation_coeffecient(event_data,column_namex,column_namey):
#    coeffecient_value = np.corrcoef(event_data[column_namex],event_data[column_namey])
#    return coeffecient_value

#correlation_coeffecient(Duel_data,'total.xgShot','total.duels')
#correlation_coeffecient(Foul_data,'total.xgShot','total.duels')
#correlation_coeffecient(Free_Kick_data,'total.xgShot','total.duels')
#correlation_coeffecient(Goalkeeper_leaving_line_data,'total.xgShot','total.duels')
#correlation_coeffecient(Interruption_data,'total.xgShot','total.duels')
#correlation_coeffecient(Offside_data,'total.xgShot','total.duels')
#correlation_coeffecient(Others_on_the_ball_data,'total.xgShot','total.duels')
#correlation_coeffecient(Pass_data,'total.xgShot','total.duels')
#correlation_coeffecient(Save_attempt_data,'total.xgShot','total.duels')
#correlation_coeffecient(Shot_data,'total.xgShot','total.duels')

def draw_ground(ax):

    #fig,ax = plt.subplots(figsize=(10.4,6.8))
    # hides the x and y ticks
    #ax.axis('off') 


    #side and goal lines
    yLine1 = [0,0,68,68,0]
    xLine1 = [0,104,104,0,0]
    plt.plot(xLine1,yLine1,color="black",zorder=5)


    #outer boxes
    yRightBox = [13.84,13.84,54.16,54.16] 
    xRightBox = [104,87.5,87.5,104]
    plt.plot(xRightBox,yRightBox,color="black",zorder=5)


    yLeftBox = [13.84,13.84,54.16,54.16] 
    xLeftBox = [0,16.5,16.5,0]
    plt.plot(xLeftBox,yLeftBox,color="black",zorder=5)

    #goals
    yRightGoal = [30.34,30.34,37.66,37.66]
    xRightGoal = [104,104.5,104.5,104]
    plt.plot(xRightGoal,yRightGoal,color="black",zorder=5)

    yLeftGoal = [30.34,30.34,37.66,37.66]
    xLeftGoal = [0,-0.5,-0.5,0]
    plt.plot(xLeftGoal,yLeftGoal,color="black",zorder=5)


    #yard boxes
    yRightYard = [24.84,24.84,43.16,43.16]
    xRightYard = [104,99.5,99.5,104]
    plt.plot(xRightYard,yRightYard,color="black",zorder=5)

    yLeftYard = [24.84,24.84,43.16,43.16]
    xLeftYard = [0,4.5,4.5,0]

    plt.plot(xLeftYard,yLeftYard,color="black",zorder=5)


    #halfway line
    yHalfLine = [0,68] 
    xHalfLine = [52,52]
    plt.plot(xHalfLine,yHalfLine,color="black",zorder=5)


    #kickoff circle
    circle =plt.Circle((52, 34), 9.15,ls='solid',lw=1.5,color="black", fill=False, zorder=2,alpha=1)
    ax.add_artist(circle)

    #arc circle

    #left_half_circle = Arc(())

    #plt.show()
def scaling_axis(x_axis,y_axis):
    xaxis = [i*1.04 for i in (x_axis)]
    yaxis = [j*0.68 for j in (y_axis)]
    return xaxis,yaxis


def heat_map(event_data,event_data_goal,event_title):
    fig=plt.figure(figsize=(10.4,6.8))
    #fig.set_size_inches(5,7)
    ax=fig.add_subplot(1,1,1)
    draw_ground(ax)
    plt.axis()
    (axis_x,axis_y)=scaling_axis(event_data['x start'],event_data['y start'])
    (axis_x1,axis_y1)=scaling_axis(event_data_goal['x start'],event_data_goal['y start'])
    #axis_data=scaling_axis(event_data['x stop'],event_data['positions x start'])
    #cmap = sb.cubehelix_palette(as_cmap=True, dark=1, light=0, reverse=True)
    sb.kdeplot(axis_x,axis_y,cmap= plt.cm.Reds, shade = "True",shade_lowest="True",color = "red",n_levels=30,cbar = "True")
    sb.scatterplot(axis_x1,axis_y1,label = "Goal", color = "black")
    #sb.kdeplot(axis_x1,axis_y1,cmap=cmap,shade = "True",color = "green",n_levels=30)
    plt.ylim(0, 68)
    plt.xlim(0, 104)
    plt.title(event_title)
    #plt.contour(axis_x,axis_y, gridsize=(25,25), cmap=plt.cm.Reds)
    #plt.colorbar()
    plt.legend(loc='upper right')
    plt.show()

Fig_1 = heat_map(Duel_data,Duel_data_goal,"Duel")
Fig_1.add_subplots(111)
#Fig_2 = heat_map(Duel_data_goal,"Duel with goal")

#Fig_3 = heat_map(Foul_data,Foul_data_goal,"Foul with goal")
#Fig_4 = heat_map(Foul_data_goal,"Duel with goal")

Fig_5 = heat_map(Free_Kick_data,Free_Kick_data_goal,"Free Kick")
#Fig_6 = heat_map(Free_Kick_data_goal,"Duel with goal")

#Fig_7 = heat_map(Goalkeeper_leaving_line_data,"Goalkeeper leaving line")                 #not required 
#Fig_8 = heat_map_goal(Goalkeeper_leaving_line_data_goal,"Goalkeeper leaving line")

#Fig_9 = heat_map(Interruption_data,"Interruption")        #not required 
#Fig_10 = heat_map_shot(Interruption_data_goal, "Interruption")

#Fig_11 = heat_map(Offside_data,Offside_data_goal,"Offside with goal")
#Fig_12 = heat_map(Offside_data_goal,"Duel with goal")

#Fig_13 = heat_map(Others_on_the_ball_data,"Others on the ball")
#Fig_14 = heat_map(Others_on_the_ball_data_goal,"Duel with goal")

Fig_15 = heat_map(Pass_data,Pass_data_goal,"Pass")
#Fig_16 = heat_map(Pass_data_goal,"Duel with goal")

#Fig_17 = heat_map_shot(Save_attempt_data,"Save attempt")   #not required 
#Fig_18 = heat_map_shot(Save_attempt_data_goal,"Save attempt")

Fig_19 = heat_map(Shot_data,Shot_data_goal,"Shot")
#Fig_20 = heat_map(Shot_data_goal,"Duel with goal")

