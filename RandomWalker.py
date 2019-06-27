#!/usr/local/bin/python3
#-*-coding:utf-8-*-



import matplotlib.pyplot as plot
import random


class ranWakler():
    '''
    随机漫步
    '''
    def __init__(self,num_points=5000):
        '''
         初始化函数
        '''
        self.num_points=num_points
        self.x_step=[0]
        self.y_step=[0]

    def stepDirectionstep(self):
        while(len(self.x_step)<self.num_points):
            direction_x=random.choice([-1,1])
            step_x=random.choice([1,2,3,4,5])
            direction_y=random.choice([-1,1])
            step_y=random.choice([1,2,3,4,5])
            next_x=self.x_step[-1]+direction_x*step_x
            next_y=self.y_step[-1]+direction_y*step_y
            if (next_x == 0 and next_y == 0):
                continue
            self.x_step.append(next_x)
            self.y_step.append(next_y)

for i in range(0,10):
    rw=ranWakler(5000*i)
    rw.stepDirectionstep()
    plot.grid('-')
    plot.xlabel("Random Walk Number--y",fontsize=14)
    plot.ylabel("Random Walk Number--x",fontsize=14)
    plot.title("Random Walker",fontsize=20)
    plot.scatter(rw.x_step,rw.y_step,c=rw.y_step,edgecolors='none',s=2)
    # plot.show()
    plot.savefig("Randomwalker{}.png".format(i))
# rw=ranWakler(5000)
# plot.figure()
# rw.stepDirectionstep()
# plot.grid('-')
# plot.xlabel("Random Walk Number--y",fontsize=14)
# plot.ylabel("Random Walk Number--x",fontsize=14)
# plot.title("Random Walker",fontsize=20)
# plot.scatter(rw.x_step,rw.y_step,c=rw.y_step,edgecolors='none',s=2)
# # plot.show()
# plot.savefig("Randomwalker{}.png")
