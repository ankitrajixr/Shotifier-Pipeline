import matplotlib.pyplot as plt

def draw_ground():

    fig,ax = plt.subplots(figsize=(10.4,6.8))
    # hides the x and y ticks
    ax.axis('off') 


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

    plt.show()

    #plt.scatter(20,10,marker='o',color='red', zorder=10)

