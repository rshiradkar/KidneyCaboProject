import os
import dicom2nifti


# baseDir = 'C:\\Users\\rshirad\\OneDrive - Emory University\\Kidney_Cabo_project\\opt\\localdata\\Data\\hmtrive\\Rakesh_RCC_Cabo\\images\\anonymization_pipeline\\files_for_upload\\dicom-anon\\12034721\\1.2.846.113975.3.64.1.61585762.20200430.1071219'
# altDir = 'C:\\Users\\rshirad\\OneDrive - Emory University\\KIDNEY~1\\opt\\LOCALD~1\\Data\\hmtrive\\RAKESH~1\\images\\ANONYM~1\\FILES_~1\\DICOM-~1\\12034721\\128461~1.107\\131221~1.0'

wd = os.getcwd()
print(wd)
baseDir = input('Enter dir path: ')
output = 'D:\\Data\\Kidney Cabo\\12034721_2'
dirList = os.listdir(baseDir)
os.chdir(baseDir)
fileList = os.listdir()

print(fileList)
path = os.path.join(baseDir,fileList[1])

# fileList2 = os.listdir()
print(path)
timePoints = os.listdir(path)
pathtp = os.path.join(path,timePoints[1])
print(pathtp)

seqs = os.listdir(pathtp)
pathseq = os.path.join(pathtp,seqs[1])

print(pathseq)

dst1 = os.path.join(pathtp,"TP1")

os.rename(pathseq,dst1)

# imgs = os.listdir(pathseq)

# print(imgs)

# for i in dirList:
#     os.chdir(i)
#     folderList = os.listdir()
#     print(folderList)

# pathDir = os.path.join(baseDir,dirList[1])
# imgList = os.listdir(pathDir)

# print(imgList)
# dicom2nifti.convert_directory(pathseq,output)
