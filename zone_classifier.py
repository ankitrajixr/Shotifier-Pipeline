import numpy as np
import pandas as pd

def zone_classifier(x,y):

    #coordinates of zones into a dataframe
    zones_df = pd.DataFrame([['C11',0,17.334,0,22.667],
    ['C21',17.334,34.667,0,22.667],
    ['C31',34.667,52,0,22.667],
    ['C41',52,69.33,0,22.667],
    ['C51',69.33,86.65,0,22.667],
    ['C61',86.65,104,0,22.667],
    ['C12',0,17.334,22.667,45.334],
    ['C22',17.334,34.667,22.667,45.334],
    ['C32',34.667,52,22.667,45.334],
    ['C42',52,69.32,22.667,45.334],
    ['C52',69.32,86.65,22.667,45.334],
    ['C62',86.65,104,22.667,45.334],
    ['C13',0,17.334,45.334,68],
    ['C23',17.334,34.667,45.334,68],
    ['C33',34.667,52,45.334,68],
    ['C43',52,69.32,45.334,68],
    ['C53',69.32,89.65,45.334,68],
    ['C63',89.65,104,45.334,68]],
    index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
    columns = ['Zone','xStart','xEnd','yStart','yEnd'])

    zone = "NA"
    #iterate through the dataframe
    for i in range(len(zones_df)) :
        #check whether the given '(x,y)' falls in which range of Xs and Ys on a cordinate plane   
        if((x>=zones_df.iloc[i,1] and x<=zones_df.iloc[i,2]) and (y>=zones_df.iloc[i,3] and y<=zones_df.iloc[i,4])):
            zone = zones_df.iloc[i,0]
            break
        
    return zone


#a=zone_classifier(20,65)
#print(a)