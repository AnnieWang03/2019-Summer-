import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import math
from sklearn.datasets import load_iris, load_digits
#digits.data
#digit = digits.data()
import seaborn as sns; sns.set()


#storing in a class for later calling 
class Dimension:
    def __init__(self, x):
        self.x = x
        #self.y = y
    def calc(self):
    #norm
        samp = len(self.x)
        iris = load_iris()
        y = np.random.randn(samp, 2)
        plt.scatter(y[:, 0], y[:, 1], c =[sns.color_palette()[x] for x in iris.target], label = 'initial y')
        plt.savefig('initial subplot.png')
        plt.legend()
        plt.show()
        dij = []
        for i in range(0, samp):
            dij.append([])
            for j in range(0, samp):
                distance_x = np.linalg.norm(self.x[i] - self.x[j])
                dij[i].append(distance_x)
        #print('dij = {}'.format(dij))

    #direction
        step_size = float(input("Enter a step size value: "))

        direction = []
        for i in range(0, len(y)):
            direction.append([])
            for j in range(0, len(y)):
                direction1 = np.linalg.norm(y[i] - y[j])**2 - dij[i][j]**2
                direction[i].append(direction1)
        #print('direction = {}'.format(direction))
    #gradient
        gradient_average = 4
        gradient_list = np.zeros((1,samp))
        position_count = 1
        rows = 2
        columns = 4
        fig = plt.figure(1)
#running the algorithm for the first time
        for i in range(samp):
            gradient_i = 0
            for j in range(samp):
                if i != j:
                    direction_temp = np.linalg.norm(y[i] - y[j])**2 - dij[i][j]**2
                    gradient_i += np.linalg.norm(direction_temp*(y[i]-y[j]))
                    y[i] -= step_size * direction_temp *(y[i]-y[j])
            gradient_list[0][i] = gradient_i/samp

        gradient_average = 4
        count = 0
        #print('gradient list')
        #print(gradient_list[0])
        #running after the first time 
        #stop after a certain value is reached
        while gradient_average > 0.15 and count < 70:
            #finding the index that still need to be moved
            for index, elem in enumerate(gradient_list[0]):
                if elem > 0.15:
                    i = index
                    gradient_i = 0
                    for j in range(samp):
                        if i != j:
                            direction_temp = np.linalg.norm(y[i] - y[j])**2 - dij[i][j]**2
                            gradient_i += np.linalg.norm(direction_temp*(y[i]-y[j]))
                            #moving y values 
                            y[i] -= step_size * direction_temp *(y[i]-y[j])
                    gradient_list[0][i] = gradient_i/samp

                #graphing the progression of each 10 trials
            if count%10 == 0:
                sub = fig.add_subplot(rows,columns,position_count)
                plt.scatter(y[:, 0], y[:, 1], c =[sns.color_palette()[x] for x in iris.target])
                plt.subplots_adjust(bottom = 0.1, right = 0.8, top = 0.9, wspace = 0.3, hspace = 1)
                sub.set_title('Trial = '+str(count))
                position_count += 1
            count += 1
            gradient_average = sum(gradient_list[0])/len(gradient_list[0])

#plotting the graph for trial #70
        sub = fig.add_subplot(rows,columns,position_count)
        plt.scatter(y[:, 0], y[:, 1], c =[sns.color_palette()[x] for x in iris.target])
        plt.subplots_adjust(bottom = 0.05, right = 0.8, top = 0.9, wspace = 0.6, hspace = 1)
        sub.set_title('Trial = '+str(count))

        plt.savefig('final subplot.png') 
        plt.show()
                    
        #print('y = {}'.format(y))
        print('gradient average = {}'.format(gradient_average))
        print('count = {}'.format(count))
        plt.show()

        plt.scatter(y[:, 0], y[:, 1], c =[sns.color_palette()[x] for x in iris.target], label = 'final y')
        plt.legend()
        plt.savefig('final y.png') 
        plt.show()

        
if __name__ == "__main__":

##    #digits.data
##    d = Dimension(load_digits().data[0:100,:])
##    #digit = Dimension(digits.data())
##    print(d.calc())

    x1 = Dimension(load_iris().data)
    print(x1.calc())
