from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData, buildExamplesFromXorData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import sys
import getopt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

xorData = buildExamplesFromXorData()
def testXorData(hiddenLayers = [1]):
    return buildNeuralNet(xorData, maxItr = 200, hiddenLayerList= hiddenLayers)

def q5():
    print 'Question 5'
    penAccuracy = []
    carAccuracy = []
    for i in range(5):
        penAccuracy.append(testPenData()[1])
        carAccuracy.append(testCarData()[1])
    penStats = {'max': max(penAccuracy), 'avg': average(penAccuracy), 'stDev': stDeviation(penAccuracy)}
    carStats = {'max': max(carAccuracy), 'avg': average(carAccuracy), 'stDev': stDeviation(carAccuracy)}

    print 'pen statistics:'
    print penStats
    print 'car statistics:'
    print carStats

def q6():
    print 'Question 6'
    penStats = {}
    carStats = {}
    for percepNum in xrange(0, 41, 5):
        penAccuracy = []
        carAccuracy = []
        for i in range(5):
            percep = [percepNum]
            penAccuracy.append(testPenData(percep)[1])
            carAccuracy.append(testCarData(percep)[1])
        percepNumString = str(percepNum)
        penStats[percepNumString] = {'max': max(penAccuracy), 'avg': average(penAccuracy), 'stDev': stDeviation(penAccuracy)}
        carStats[percepNumString] = {'max': max(carAccuracy), 'avg': average(carAccuracy), 'stDev': stDeviation(carAccuracy)}
        print 'pen statistics, ', percepNum, ' perceptrons'
        print penStats[percepNumString]
        print 'car statistics, ', percepNum, ' perceptrons'
        print carStats[percepNumString]
    print 'final pen statistics:'
    print penStats
    print 'final car statistics'
    print carStats

def q7():
    print 'question 7'
    stats = {}
    hlNum = 0
    while True:
        accuracy = []
        for i in range(5):
            hl = [hlNum]
            accuracy.append(testXorData(hl)[1])
        hlNumString = str(hlNum)
        stats[hlNumString] = {'max': max(accuracy), 'avg': average(accuracy), 'stDev': stDeviation(accuracy)}
        print 'stats, ', hlNumString, ' hidden layer perceptrons'
        print stats[hlNumString]
        if average(accuracy) == 1.0:
            break
        hlNum += 1
    print 'final stats'
    print stats


def main():

    args = sys.argv
    questions = ['q5','q6','q7']
    if len(args)==1:
        print '\nPlease input question number (5, 6, or 7). For example: -q q5'
    else:
        opts, args = getopt.getopt(args[1:],"q",["q="])

        for opt, arg in opts:
            if opt=='-q' or opt=='--q':
                if args[0] in questions:
                    if args[0] == 'q5':
                        q5()
                    elif args[0] == 'q6':
                        q6()
                    else:
                        q7()
                else:
                    print 'can only test q5 and q6 and q7'
            else:
                print '\nPlease input question number (5, 6, or 7). For example: -q q5'

if __name__=='__main__':
	main()
