from DataInterface import getDummyDataset2,getDummyDataset1,getConnect4Dataset, getCarDataset, getExtraCreditDataset
from DecisionTree import makeTree, setEntropy,infoGain, makePrunedTree
import Testing
import random
import sys, getopt

def testExtraCredit(setFunc = setEntropy, infoFunc = infoGain):
    examples,attrValues,labelName,labelValues = getExtraCreditDataset()
    print 'Testing Poker dataset. Number of examples %d.'%len(examples)
    tree = makeTree(examples, attrValues, labelName, setFunc, infoFunc)
    f = open('poker.out','w')
    f.write(str(tree))
    f.close()
    print 'Tree size: %d.\n'%tree.count()
    print 'Entire tree written out to poker.out in local directory\n'
    evaluation = Testing.getAverageClassificaionRate((examples,attrValues,labelName,labelValues))
    print 'Results for training set:\n%s\n'%str(evaluation)
    Testing.printDemarcation()
    return (tree,evaluation)

def q8():
    print 'Question 8'
    tree, eval = testExtraCredit()
    print 'tree size', tree.count()
    print 'tree classification rates', eval[0]

if __name__=='__main__':
	q8()