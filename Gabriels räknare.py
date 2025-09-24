import math
import matplotlib.pyplot as plt
import numpy as np

# Empty lists and values
x_komp = []
y_komp = []
R = None
V = None


# Takes in inputs from the user, and later multiplies it with cos or sin to give its components, which will be returned
def inputs():
    ik = float(input("Kraft: "))
    iv = float(input("Vinkel: "))
    x_komp.append(ik * math.cos(math.radians(iv)))
    y_komp.append(ik * math.sin(math.radians(iv)))
    return x_komp, y_komp

# Calculates the vectors resultant and its angle
def calc(x_komp, y_komp, R, V):
    for x in x_komp:
        x_sum = sum(x_komp)
    for y in y_komp:
        y_sum = sum(y_komp)
    R = math.sqrt(x_sum**2 + y_sum**2)
    V = math.degrees(math.atan2(y_sum, x_sum))
    return R, V

# While-loop
while True:
    Q = str(input("Vill du lägga till en kraft? (j/n) "))

    # Starts taking in the values
    if "j" in Q.lower():
        inputs()
        R, V = calc(x_komp, y_komp, R, V)
    if "n" in Q.lower():
        break
    
    # Calculates the sum and prints
    if R != None and V != None:
        print(f"Resultantens storlek är {R:.2f} N")
        print(f"Resultantens vinkel är {V:.2f}°")

    Q2 = str(input("Vill du se resultanten? (j/n) "))
    if "j" in Q2.lower():

        # Visualises the vectors in matplotlib

        Q3 = str(input("Se genom translation eller resultant= (t/r) "))

        # Resultant
        if "r" in Q3.lower():
            y = R * math.sin(math.radians(V))
            x = R * math.cos(math.radians(V))
            xrp = np.array([0, x])
            yrp = np.array([0, y])
            
            # From the last values, creates an array of values which will be visualised
            if len(x_komp) > 1:
                for i in range(len(x_komp)):
                    y = y_komp[i]
                    x = x_komp[i]
                    xp = np.array([0, x])
                    yp = np.array([0, y])

                    plt.arrow(xp[0], yp[0], xp[1], yp[1], head_width=R/20, head_length=R/20, fc='red', ec='red')
        
            # Creates a line for the X and Y
            for i in range(len(x_komp)):
                e = 0
                if x_komp[i] > e:
                    e = x_komp[i]
                if y_komp[i] > e:
                    e = y_komp[i]
                if R > e:
                    e = R

            # A small addition to make it slightly bigger than the vectors
            e += e//10

            xaxeln = np.array([-e, e])
            yaxeln = np.array([0, 0])
            plt.plot(xaxeln, yaxeln, color="black")
            plt.plot(yaxeln, xaxeln, color="black")

            plt.arrow(xrp[0], xrp[0], xrp[1], yrp[1], head_width=e/20, head_length=e/20, fc='orange', ec='orange')

            plt.title("Resultant")
            plt.xlabel("X-komponent (N)")
            plt.ylabel("Y-komponent (N)")

            plt.grid()     
            plt.show()

        # Translation   
        if "t" in Q3.lower():

            # Values for the previous X and Y, now set to origo
            prevx = 0
            prevy = 0

            # Creates a line for the X and Y
            for i in range(len(x_komp)):
                e = 0
                if x_komp[i] > e:
                    e = x_komp[i]
                if y_komp[i] > e:
                    e = y_komp[i]
                if R > e:
                    e = R
            
            # A small addition to make it slightly bigger than the vectors
            e += e//10
            
            # Loops through the vectors
            for i in range(len(x_komp)):
                
                # Vectors
                x = x_komp[i]
                y = y_komp[i]
                
                # Creates a vector that originates in the previous vector
                xp = np.array([prevx, x])
                yp = np.array([prevy, y])

                plt.arrow(xp[0], yp[0], xp[1], yp[1], head_width=R/20, head_length=R/20, fc='red', ec='red')

                # Saves the current value for the next loop
                prevx = x_komp[i] + prevx
                prevy = y_komp[i] + prevy

                # Array the values for visualisation
                if i == len(x_komp) - 1:
                    xrp = np.array([0, x + prevx - x_komp[i]])
                    yrp = np.array([0, y + prevy - y_komp[i]])
                    plt.arrow(xrp[0], yrp[0], xrp[1], yrp[1], head_width=e/20, head_length=e/20, fc='orange', ec='orange')


            # Visualisation
            xaxeln = np.array([-e, e])
            yaxeln = np.array([0, 0])
            plt.plot(xaxeln, yaxeln, color="black")
            plt.plot(yaxeln, xaxeln, color="black")

        
            plt.title("Translation")
            plt.xlabel("X-komponent (N)")
            plt.ylabel("Y-komponent (N)")
            plt.grid()
            plt.show()