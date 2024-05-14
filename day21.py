##Give a simple coding example on multiple and multilevel inheritance in python.
##MULTIPLE INHERITANCE

##multiple inheritance
class grandfather:
    def call(self):
        print('im grandfather')
class father():
    def call2(self):
        print('im father')
class son(father,grandfather):
    def __init__(self):
        print('im son')
obj=son()
obj.call2()
obj.call()
##MULTILEVEL INHERITANCE
class parentclass1:
    def call(self):
        print('im P1')
class derived1(parentclass1):
    def call2(self):
        print('im D1')
class derived2(derived1):
    def call3(self):
        print('im D2')
obj=derived2()
obj.call3()
obj.call2()
obj2=derived1()
obj2.call()
##Write a function of python that takes the confusion matrix output as an input, and return the precision and recall score.
##confusion matrix
def cmatrix():
    TP=int(input('enter first element of matrix'))
    FP=int(input('enter second element of matrix'))
    FN=int(input('enter third element of matrix'))
    TN=int(input('enter fourth element of matrix'))
    matrix=[TP,FP,FN,TN]
    PRECISION_SCORE=TP/(TP+FP)
    RECALL_SCORE=TP/(TP+FN)
    print('confusion matrix is',matrix)
    print('Precision score is',PRECISION_SCORE)
    print('Recall score is',RECALL_SCORE)
cmatrix()
##Actual prediction
#0 0
# 1 1
# 0 1
# 1 0
# 1 0
#  Make a confusion matrix on this given above dataset, and count
# TP,FP ,FN,TN are in the given example. Don’t need to perform
# code, just count manually all the components of confusion matrix
##TP=1
##FP=1
##FN=2
##TN=1
##CONFUSION_MATRIX=[1,1,2,1]