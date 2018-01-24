#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jaylin Zhou
# 24 Jan 2018

import os
import re

def listFiles(dirPath):
    fileList = []
    for (dirPath, dirNames, fileNames) in os.walk(path):
        for fileName in fileNames:
            if fileName == 'metadata.yaml':
                fileList.append(os.path.join(dirPath, fileName))
    return fileList

def findString(filePath, regex):
    fileObj = open(filePath, 'r')
    for eachLine in fileObj:
        if re.search(regex, eachLine):
            return eachLine.rstrip('\n')

if __name__ == '__main__':
    path = raw_input('Input the path of dir: ')
    dictFileStatus = {}
    regex1 = 'status:'
    regex2 = 'publish_date:'
    fileList = listFiles(path)
    for fileObj in fileList:
        if findString(fileObj, regex1):
            dictFileStatus[fileObj] = [findString(fileObj, regex1)]
        else:
            dictFileStatus[fileObj] = ['null']
        if findString(fileObj, regex2):
            dictFileStatus[fileObj].append(findString(fileObj, regex2))
        else:
            dictFileStatus[fileObj].append('null')

    for key, value in dictFileStatus.items():
        print key + ';' + value[0] + ';' + value[1]
