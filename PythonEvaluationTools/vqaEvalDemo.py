# coding: utf-8

import sys
dataDir = '../../VQA'
sys.path.insert(0, '%s/PythonHelperTools/vqaTools' %(dataDir))
from vqa import VQA
from vqaEvaluation.vqaEval import VQAEval
import matplotlib.pyplot as plt
import skimage.io as io
import json
import random
import os

# set up file names and paths
annFileName = 'test_annotations_yesno_arethere.json'
quesFileName = 'test_questions_yesno_arethere.json'
resultFileName = 'knn_results_test_yesno.json'
versionType ='v2_' # this should be '' when using VQA v2.0 dataset
taskType    ='OpenEnded' # 'OpenEnded' only for v2.0. 'OpenEnded' or 'MultipleChoice' for v1.0
dataType    ='mscoco'  # 'mscoco' only for v1.0. 'mscoco' for real and 'abstract_v002' for abstract for v1.0. 
dataSubType ='val2014'
#annFile     ='%s/Annotations/%s%s_%s_annotations_yesno_arethere.json'%(dataDir, versionType, dataType, dataSubType)
#quesFile    ='%s/Questions/%s%s_%s_%s_questions.json'%(dataDir, versionType, taskType, dataType, dataSubType)
annFile     ='%s/Annotations/%s'%(dataDir, annFileName)
quesFile    ='%s/Questions/%s'%(dataDir, quesFileName)
imgDir      ='%s/Images/%s/%s/' %(dataDir, dataType, dataSubType)
# resultType  ='fake'
# fileTypes   = ['results', 'accuracy', 'evalQA', 'evalQuesType', 'evalAnsType']

# An example result json file has been provided in './Results' folder.  

# [resFile, accuracyFile, evalQAFile, evalQuesTypeFile, evalAnsTypeFile] = ['%s/Results/%s%s_%s_%s_%s_%s.json'%(dataDir, versionType, taskType, dataType, dataSubType, \
# resultType, fileType) for fileType in fileTypes]

resFile = '%s/Results/%s'%(dataDir, resultFileName)

# create vqa object and vqaRes object
vqa = VQA(annFile, quesFile)
vqaRes = vqa.loadRes(resFile, quesFile)

# create vqaEval object by taking vqa and vqaRes
vqaEval = VQAEval(vqa, vqaRes, n=2)   #n is precision of accuracy (number of places after decimal), default is 2

# evaluate results
"""
If you have a list of question ids on which you would like to evaluate your results, pass it as a list to below function
By default it uses all the question ids in annotation file
"""
vqaEval.evaluate() 

# print accuracies
print "\n"
print "Overall Accuracy is: %.02f\n" %(vqaEval.accuracy['overall'])
print "Per Question Type Accuracy is the following:"
for quesType in vqaEval.accuracy['perQuestionType']:
	print "%s : %.02f" %(quesType, vqaEval.accuracy['perQuestionType'][quesType])
print "\n"
print "Per Answer Type Accuracy is the following:"
for ansType in vqaEval.accuracy['perAnswerType']:
	print "%s : %.02f" %(ansType, vqaEval.accuracy['perAnswerType'][ansType])
print "\n"