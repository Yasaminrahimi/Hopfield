import os
import sys
import numpy as num
train_data = []
weightSum = num.zeros((63,63) , dtype=float)

def Readfile():
 
    with open("training-data.txt") as file:
        cnt,ind = 0,0
        train = num.zeros(63, dtype=float)
        for line in file:
            if cnt == 0:
                cnt+=1
                for element in line:
                    if element=='#':
                        train[ind] = 1
                        ind+=1
                    elif element=='*':
                        train[ind] = -1
                        ind+=1
                    
            elif cnt==9:
                cnt,ind = 0,0
                train_data.append(train)
                train = num.zeros(63,dtype=float)
            else:
                for element in line:
                    if element=='#':
                        train[ind] = 1
                        ind+=1
                    elif element=='*':
                        train[ind] = -1
                        ind+=1
                    else:
                        ind = ind
                cnt+=1
        return train_data
 
 
def weightTotal(train_data):
    weightSum = num.zeros((63,63) , dtype=float)
#    print (weightSum)       
    weight_array = num.zeros((63,63), dtype=float)
    for i in range (0,7):
        s = num.zeros((1,63), dtype=float)
        s = train_data[i]
        
        weight_array = num.outer( s, s)
        weightSum += weight_array
    weightSum -= 7 * (num.identity(63))
    return weightSum

def weight(train_data):
    s = train_data[0]
    weightSum = num.outer( s, s)
    weightSum -= num.identity(63)
    return weightSum

def weight1(train_data):
    weightSum = num.zeros((63,63) , dtype=float)
    weight_array = num.zeros((63,63), dtype=float)
    for i in range (1,2):
        s = num.zeros((1,63), dtype=float)
        s = train_data[i]
        weight_array = num.outer( s, s)
        weightSum += weight_array
    weightSum -= 2 * (num.identity(63))
 #   return weightSum


def test(weightSum):
    test = num.zeros((1,63), dtype=float)
    ind = 0
    with open("test.txt") as file:
        for line in file:
            
            for element in line:
 #               test[ind] = int('element')
                if element=='1':
                   test[0][ind] = 1
                   ind += 1
                else:
                    if element=='0':
                        test[0][ind] = -1
                        ind += 1
                    elif element == '/n':
                        ind += 0
    print (test)
    testweight= weightSum
    epoch = 0
    while True:
        old_test = test.copy()
        y_in = num.zeros((1,63), dtype=float)
        for i in range (1):
 #           print (test)
            for l in range(63):
                for k in range(63):
                    x = test[i][k]
                    y = testweight[k][l]
                y_in[i][l] += x * y
                test[0][l] = Actfunc(y_in[0][l])
        if num.array_equal(old_test, test):
            break
        epoch += 1
    print (epoch)       
    return test


def Actfunc (y_in):
    y_out = 0 
    y = y_in
    if y > 0:
        y_out += 1
    else:
        y_out += -1
    return y_out


def main ():
    
    test1 = (weightTotal(Readfile()))
    test2 = test(weight(Readfile()))
    test3 = (weight1(Readfile()))
    print (test1)
    print (test2)
    print (test3)
