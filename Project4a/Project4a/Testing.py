from DataInterface import getDummyDataset2,getDummyDataset1,getConnect4Dataset, getCarDataset
from DecisionTree import makeTree, setEntropy,infoGain, makePrunedTree
import random
import sys, getopt


def getAverageClassificaionRate(dataset,runs=20,testSize=200,setFunc = setEntropy, infoFunc = infoGain):
    """
    Randomly selects a test set and removes it from the training set.
    """
    scores = []
    examples,attrValues,labelName,labelValues = dataset
    l = len(examples)-1
    print 'Starting test for average error for %d runs with test size %d'%(runs,testSize)
    for r in xrange(runs):
        runExamples = examples[:]
        test = []
        for i in xrange(testSize):
            test.append(runExamples.pop(random.randint(0,l-i)))
        tree = makeTree(runExamples, attrValues, labelName, setFunc, infoFunc)
        score = evaluateTree(tree,test,labelName)[0]
        print 'Score for run %d is %f'%(r+1,score)
        scores.append(score)
    average = sum(scores)/float(runs)
    print 'Average classification rate over all runs: %f'%(average)
    return (scores,average)

def evaluateTree(tree,testExamples,labelName):    
    """
    Simple function to get the correct classification ratio for a given DTree 
    and a set of testing examples.
    
    Args:
        testExamples (list<dictionary<str,str>>): list of examples to test with
        labelName (str): the name of the label
    Returns:
        tuple<float,
        list<tuple<str,str>>>
        Tuple
    """
    confusion=[]
    f=0.0
    for example in testExamples:
        z = tree.classify(example)
        if example[labelName]==z:
            f+=1.0
        else:
            confusion.append((example[labelName],z))
    return (f/len(testExamples),confusion)
  
def printDemarcation():
    print 'Done\n____________________________________________________________________\n'
    
def testDummySet1(setFunc = setEntropy, infoFunc = infoGain):
    """Correct classification rate is 1.0"""
    examples,attrValues,labelName,labelValues = getDummyDataset1()
    print 'Testing dummy dataset 1. Number of examples %d.'%len(examples)
    tree = makeTree(examples, attrValues, labelName, setFunc, infoFunc)
    print 'Tree is as follows:\n%s\n'%str(tree)
    print 'Tree size: %d.\n'%tree.count()
    examples,attrValues,labelName,labelValues = getDummyDataset1(test=True)
    evaluation = evaluateTree(tree,examples,labelName)
    print 'Results for training set:\n%s\n'%str(evaluation)
    printDemarcation()
    return (tree,evaluation)

def testDummySet2(setFunc = setEntropy, infoFunc = infoGain):
    """Correct classification rate is 0.55"""
    examples,attrValues,labelName,labelValues = getDummyDataset2()
    print 'Testing dummy dataset 2. Number of examples %d.'%len(examples)
    tree = makeTree(examples, attrValues, labelName, setFunc, infoFunc)
    print 'Tree is as follows:\n%s\n'%str(tree)
    print 'Tree size: %d.\n'%tree.count()
    examples,attrValues,labelName,labelValues = getDummyDataset2(test=True)
    evaluation = evaluateTree(tree,examples,labelName)
    print 'Results for training set:\n%s\n'%str(evaluation)
    printDemarcation()
    return (tree,evaluation)

def testConnect4(setFunc = setEntropy, infoFunc = infoGain):
    """Correct classification averate rate is about 0.75"""
    examples,attrValues,labelName,labelValues = getConnect4Dataset() 
    print 'Testing Connect4 dataset. Number of examples %d.'%len(examples)
    tree = makePrunedTree(examples, attrValues, labelName, setFunc, infoFunc, .05)
    f = open('connect4.out','w')
    print 'Tree size: %d.\n'%tree.count()
    print 'Entire tree written out to connect4.out in local directory\n'
    f.write(str(tree))
    f.close()
    evaluation = getAverageClassificaionRate((examples,attrValues,labelName,labelValues),runs=10,testSize=2000)
    print 'Results for training set:\n%s\n'%str(evaluation)
    printDemarcation()
    return (tree,evaluation)

def testCar(setFunc = setEntropy, infoFunc = infoGain):
    """Correct classification averate rate is about 0.95"""
    examples,attrValues,labelName,labelValues = getCarDataset()
    print 'Testing Car dataset. Number of examples %d.'%len(examples)
    tree = makeTree(examples, attrValues, labelName, setFunc, infoFunc)
    f = open('car.out','w')
    f.write(str(tree))
    f.close()
    print 'Tree size: %d.\n'%tree.count()
    print 'Entire tree written out to car.out in local directory\n'
    dataset = getCarDataset()
    evaluation = getAverageClassificaionRate((examples,attrValues,labelName,labelValues))
    print 'Results for training set:\n%s\n'%str(evaluation)
    printDemarcation()
    return (tree,evaluation)

def q6():
    print 'Question 6'
    tree1, eval1 = testDummySet1()
    tree2, eval2 = testDummySet2()
    treeCars, evalCars = testCar()
    treeConnect, evalConnect = testConnect4()
    print 'tree1 size', tree1.count()
    print 'tree1 classification rate', eval1[0]
    print 'tree2 size', tree2.count()
    print 'tree2 classification rate', eval2[0]
    print 'treeCar size', treeCars.count()
    print 'treeCar classification rate', evalCars[0]
    print 'treeConnect size', treeConnect.count()
    print 'treeConnect classification rate', evalConnect[0]

def main():

    args = sys.argv
    questions = ['q6','q7']
    if len(args)==1:
        print '\nPlease input question number (6 or 7). For example: -q q6'
    else:
        opts, args = getopt.getopt(args[1:],"q",["q="])

        for opt, arg in opts:
            if opt=='-q' or opt=='--q':
                if args[0] in questions:
                    if args[0] == 'q6':
                        q6()
                    else:
                        q7()
                else:
                    print 'can only test q6 and q7'
            else:
                print '\nPlease input question number (6 or 7). For example: -q q5'

if __name__=='__main__':
	main()