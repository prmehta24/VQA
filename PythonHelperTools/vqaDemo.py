# coding: utf-8

from vqaTools.vqa import VQA
import json
import random
import skimage.io as io
import matplotlib.pyplot as plt
import os

dataDir = '../../VQA'
versionType = 'v2_'  # this should be '' when using VQA v2.0 dataset
taskType = 'OpenEnded'  # 'OpenEnded' only for v2.0. 'OpenEnded' or 'MultipleChoice' for v1.0
dataType = 'mscoco'  # 'mscoco' only for v1.0. 'mscoco' for real and 'abstract_v002' for abstract for v1.0.
dataSubType = 'val2014'
annFile = '%s/Annotations/%s%s_%s_annotations.json' % (dataDir, versionType, dataType, dataSubType)
quesFile = '%s/Questions/%s%s_%s_%s_questions.json' % (dataDir, versionType, taskType, dataType, dataSubType)
imgDir = '%s/Images/%s/%s/' % (dataDir, dataType, dataSubType)

# initialize VQA api for QA annotations
vqa = VQA(annFile, quesFile)

# load and display QA annotations for given question types
"""
All possible quesTypes for abstract and mscoco has been provided in respective text files in ../QuestionTypes/ folder.
"""

# imgFilename = 'COCO_' + dataSubType + '_'+ str(imgId).zfill(12) + '.jpg'
# if os.path.isfile(imgDir + imgFilename):
# 	I = io.imread(imgDir + imgFilename)
# 	plt.imshow(I)
# 	plt.axis('off')
# 	plt.show()
# else:
# 	print("Path: ",(imgDir + imgFilename))
# 	print("Image not found.")

# load and display QA annotations for given answer types
"""
ansTypes can be one of the following
yes/no
number
other
"""

# delete non yes no images
# imgIds = set(vqa.getImgIds(ansTypes='yes/no', quesTypes=['are there']));
# allImgIds = set(vqa.getImgIds());
# print(len(imgIds))
# print(len(allImgIds))
# delImgIds = filter(lambda i: i not in imgIds, allImgIds)
# print(len(delImgIds))
# for imgId in delImgIds:
#     imgFilename = 'COCO_' + dataSubType + '_' + str(imgId).zfill(12) + '.jpg'
#     if os.path.isfile(imgDir + imgFilename):
#         os.remove(imgDir + imgFilename)
#     else:
#         print("Path: ",(imgDir + imgFilename))
#         print("Image not found.")
# print(len(imgIds))

# create a new json file with only yes no annotations with question filters - training
# print(type(vqa.dataset))
# print(type(vqa.dataset['annotations']))
# filtered_dataset = vqa.dataset
# print(len(vqa.dataset['annotations']))
# somelist = [x for x in filtered_dataset['annotations'] if (x['answer_type']=='yes/no' and x['question_type'] in ['are there'])]
# print(len(somelist))
# filtered_dataset['annotations'] = somelist
# json.dump(filtered_dataset, open("train_annotations_yesno_arethere.json","w"))

# create a new json file with only yes no annotations with question filters - val and test
# print(type(vqa.dataset))
# print(type(vqa.dataset['annotations']))
# filtered_dataset = vqa.dataset
# print(len(vqa.dataset['annotations']))
# somelist = [x for x in filtered_dataset['annotations'] if (x['answer_type']=='yes/no' and x['question_type'] in ['are there'])]
# print(len(somelist))
# listlensplit = len(somelist)/2
# filtered_dataset['annotations'] = somelist[:listlensplit]
# print("Val: ",len(filtered_dataset['annotations']))
# json.dump(filtered_dataset, open("val_annotations_yesno_arethere.json","w"))
# filtered_dataset['annotations'] = somelist[listlensplit:]
# print("Test: ",len(filtered_dataset['annotations']))
# json.dump(filtered_dataset, open("test_annotations_yesno_arethere.json","w"))

# create a new json file with only yes no questions and question type filters - training
# questionIds = vqa.getQuesIds(ansTypes='yes/no', quesTypes=['are there'] )
# print(type(vqa.questions))
# print(type(vqa.questions['questions']))
# filtered_dataset = vqa.questions
# print(len(vqa.questions['questions']))
# somelist = [vqa.qqa[id] for id in questionIds]
# print(len(somelist))
# #print(somelist[0])
# listlen = len(somelist)
# filtered_dataset['questions'] = somelist
# json.dump(filtered_dataset, open("train_questions_yesno_arethere.json","w"))

# create a new json file with only yes no questions and question type filters - val and test
#display number of questions and images
# questionIds = vqa.getQuesIds(ansTypes='yes/no', quesTypes=['are there'] )
# print(type(vqa.questions))
# print(type(vqa.questions['questions']))
# filtered_dataset = vqa.questions
# print(len(vqa.questions['questions']))
# somelist = [vqa.qqa[id] for id in questionIds]
# print(len(somelist))
# #print(somelist[0])
# listlensplit = len(somelist)/2
#
# filtered_dataset['questions'] = somelist[:listlensplit]
# print("VaL: ",len(filtered_dataset['questions']))
# valImages = vqa.getImgIds(quesIds=[questionIds[0]])
# print("Val Images",len(valImages))
#json.dump(filtered_dataset, open("val_questions_yesno_arethere.json","w"))
# filtered_dataset['questions'] = somelist[listlensplit:]
# print("Test: ",len(filtered_dataset['questions']))
# testImages = vqa.getImgIds(quesIds=[questionIds[0]])
# print("Test Images",len(testImages))
#json.dump(filtered_dataset, open("test_questions_yesno_arethere.json","w"))


# load and display QA annotations for given images
"""
Usage: vqa.getImgIds(quesIds=[], quesTypes=[], ansTypes=[])
Above method can be used to retrieve imageIds for given question Ids or given question types or given answer types.
"""

annIds = vqa.getQuesIds();
ids = vqa.getImgIds(quesIds=random.sample(annIds,5))
# anns = vqa.loadQA(annIds)
# randomAnn = random.choice(anns)
# vqa.showQA([randomAnn])
# imgId = randomAnn['image_id']
# imgFilename = 'COCO_' + dataSubType + '_'+ str(imgId).zfill(12) + '.jpg'
# if os.path.isfile(imgDir + imgFilename):
# 	I = io.imread(imgDir + imgFilename)
# 	plt.imshow(I)
# 	plt.axis('off')
# 	plt.show()
# else:
# 	print("Path: ",(imgDir + imgFilename))
# 	print("Image not found.")

# Calculate Majority Class and generate results file

# annIds = vqa.getQuesIds(ansTypes='yes/no', quesTypes=['are there']);
# anns = vqa.loadQA(annIds)
# print("Total Questions: ", len(annIds))
# yes = 0
# no = 0
# other = 0
# for ann in anns:
#     if ann['multiple_choice_answer'] == 'yes':
#         yes = yes + 1
#     elif ann['multiple_choice_answer'] == 'no':
#         no = no + 1
#     else:
#         other = other + 1
#         print(ann['multiple_choice_answer'])
#         print(ann['answers'])
#         print(vqa.qqa[ann['question_id']])
#
#     # print(ann['answers'])
# print("Yes Answers: ", yes)
# print("No Answers: ", no)
# print("Other Answers: ", other)
# if yes > no:
#     majorityClass = 'yes'
# else:
#     majorityClass = 'no'
# print("Majority Class: ", majorityClass)
# resultList = []
# # results = [result]
# #
# # result{
# # "question_id": int,
# # "answer": str
# # }
# for questionId in annIds:
#     tempDict = {"question_id": questionId, "answer": majorityClass}
#     resultList.append(tempDict)
# print(len(resultList))
# json.dump(resultList, open("results_val_yesno.json", "w"))
