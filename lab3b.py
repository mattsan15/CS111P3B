#!/usr/bin/python

import sys  
import os

def getSuperBlockValues(fd):
    fd.seek(0, 0)
    line = fd.readline()
    superBlock = "SUPERBLOCK"
    comma = ","
    countComma = 0
    totalNumOfBlocks = ""
    totalNumOfInodes = ""
    blockSize = ""
    InodeSize = ""
    blocksPerGroup = ""
    InodesPerGroup = ""
    firstNonResInode = ""
    while line:
        if (line.find(superBlock) != -1):
            for i in range(len(line)):
                if (line[i] == "\n"):
                    break
                if (line[i] == comma):
                    countComma += 1
                elif (countComma == 1):
                    totalNumOfBlocks += line[i]
                elif (countComma == 2):
                    totalNumOfInodes += line[i]
                elif (countComma == 3):
                    blockSize += line[i]
                elif (countComma == 4):
                    InodeSize += line[i]
                elif (countComma == 5):
                    blocksPerGroup += line[i]
                elif (countComma == 6):
                    InodesPerGroup += line[i]
                elif (countComma == 7):
                    firstNonResInode += line[i]
        line = fd.readline()
    listValue = [int(totalNumOfBlocks), int(totalNumOfInodes), int(blockSize), int(InodeSize),
                 int(blocksPerGroup), int(InodesPerGroup), int(firstNonResInode)]
    return listValue

def getFreeBlocks(fd):
    fd.seek(0, 0)
    line = fd.readline()
    bFree = "BFREE"
    comma = ","
    listOfFreeBlocks = []
    while line:
        if (line.find(bFree) != -1):
            countComma = 0
            freeBlockNumber = ""
            for i in range(len(line)):
                if (line[i] == "\n"):
                    break
                if (line[i] == comma):
                    countComma += 1
                elif (countComma == 1):
                    freeBlockNumber += line[i]
            listOfFreeBlocks.append(int(freeBlockNumber))
        line = fd.readline()
    return listOfFreeBlocks

def getFreeInodes(fd):
    fd.seek(0, 0)
    line = fd.readline()
    iFree = "IFREE"
    comma = ","
    listOfFreeInodes = []
    while line:
        if (line.find(iFree) != -1):
            countComma = 0
            freeInodeNumber = ""
            for i in range(len(line)):
                if (line[i] == "\n"):
                    break
                if (line[i] == comma):
                    countComma += 1
                elif (countComma == 1):
                    freeInodeNumber += line[i]
            listOfFreeInodes.append(int(freeInodeNumber))
	line = fd.readline()
    return listOfFreeInodes

def getInodeValues(fd):
    fd.seek(0, 0)
    line = fd.readline()
    inode = "INODE"
    comma = ","
    listOfLists = []
    while line:
        if (line.find(inode) != -1):
            countComma = 0
            inodeNumber = ""
            fileType = ""
            mode = ""
            owner = ""
            group = ""
            linkCount = ""
            timeOfLastInodeChange = ""
            modTime = ""
            timeOfLastAccess = ""
            fileSize = ""
            numOfBlocks = ""
            directBlock1 = ""
            directBlock2 = ""
            directBlock3 = ""
            directBlock4 = ""
            directBlock5 = ""
            directBlock6 = ""
            directBlock7 = ""
            directBlock8 = ""
            directBlock9 = ""
            directBlock10 = ""
            directBlock11 = ""
            directBlock12 = ""
            indirectBlock = ""
            doubleIndirectBlock = ""
            tripleIndirectBlock = ""
            for i in range(len(line)):
                if (line[i] == "\n"):
                    break
                if (line[i] == comma):
                    countComma += 1
                elif (countComma == 1):
                    inodeNumber += line[i]
                elif (countComma == 2):
                    fileType += line[i]
                elif (countComma == 3):
                    mode += line[i]
                elif (countComma == 4):
                    owner += line[i]
                elif (countComma == 5):
                    group += line[i]
                elif (countComma == 6):
                    linkCount += line[i]
                elif (countComma == 7):
                    timeOfLastInodeChange += line[i]
                elif (countComma == 8):
                    modTime += line[i]
                elif (countComma == 9):
                    timeOfLastAccess += line[i]
                elif (countComma == 10):
                    fileSize += line[i]
                elif (countComma == 11):
                    numOfBlocks += line[i]
                elif (countComma == 12):
                    directBlock1 += line[i]
                elif (countComma == 13):
                    directBlock2 += line[i]
                elif (countComma == 14):
                    directBlock3 += line[i]
                elif (countComma == 15):
                    directBlock4 += line[i]
                elif (countComma == 16):
                    directBlock5 += line[i]
                elif (countComma == 17):
                    directBlock6 += line[i]
                elif (countComma == 18):
                    directBlock7 += line[i]
                elif (countComma == 19):
                    directBlock8 += line[i]
                elif (countComma == 20):
                    directBlock9 += line[i]
                elif (countComma == 21):
                    directBlock10 += line[i]
                elif (countComma == 22):
                    directBlock11 += line[i]
                elif (countComma == 23):
                    directBlock12 += line[i]
                elif (countComma == 24):
                    indirectBlock += line[i]
                elif (countComma == 25):
                    doubleIndirectBlock += line[i]
                elif (countComma == 26):
                    tripleIndirectBlock += line[i]
            listOfOneInode = [int(inodeNumber), fileType, int(mode), int(owner), int(group), int(linkCount),
                              timeOfLastInodeChange, modTime, timeOfLastAccess, int(fileSize), int(numOfBlocks),
                              int(directBlock1), int(directBlock2), int(directBlock3), int(directBlock4),
                              int(directBlock5), int(directBlock6), int(directBlock7), int(directBlock8),
                              int(directBlock9), int(directBlock10), int(directBlock11), int(directBlock12),
                              int(indirectBlock), int(doubleIndirectBlock), int(tripleIndirectBlock)]
            listOfLists.append(listOfOneInode)
        line = fd.readline()
    return listOfLists

def getDirEntries(fd):
    fd.seek(0, 0)
    line = fd.readline()
    dirent = "DIRENT"
    comma = ","
    listOfLists = []
    while line:
        if (line.find(dirent) != -1):
            countComma = 0
            parentInodeNumber = ""
            logicalByteOffset = ""
            inodeNumOfRefFile = ""
            entryLength = ""
            nameLength = ""
            name = ""
            for i in range(len(line)):
                if (line[i] == "\n"):
                    break
                if (line[i] == comma):
                    countComma += 1
                elif (countComma == 1):
                    parentInodeNumber += line[i]
                elif (countComma == 2):
                    logicalByteOffset += line[i]
                elif (countComma == 3):
                    inodeNumOfRefFile += line[i]
                elif (countComma == 4):
                    entryLength += line[i]
                elif (countComma == 5):
                    nameLength += line[i]
                elif (countComma == 6):
                    name += line[i]
            listOfOneDir = [int(parentInodeNumber), int(logicalByteOffset), int(inodeNumOfRefFile),
                            int(entryLength), int(nameLength), name]
            listOfLists.append(listOfOneDir)
        line = fd.readline()
    return listOfLists

def getIndirectValues(fd):
    fd.seek(0, 0)
    line = fd.readline()
    indirect = "INDIRECT"
    comma = ","
    listOfLists = []
    while line:
        if (line.find(indirect) != -1):
            countComma = 0
            inodeNumber = ""
            levelOfIndirection = ""
            logicalBlockOffset = ""
            blockNumOfIndirectBlockBeingScanned = ""
            blockNumOfReferencedBlock = ""
            for i in range(len(line)):
                if (line[i] == "\n"):
                    break
                if (line[i] == comma):
                    countComma += 1
                elif (countComma == 1):
                    inodeNumber += line[i]
                elif (countComma == 2):
                    levelOfIndirection += line[i]
                elif (countComma == 3):
                    logicalBlockOffset += line[i]
                elif (countComma == 4):
                    blockNumOfIndirectBlockBeingScanned += line[i]
                elif (countComma == 5):
                    blockNumOfReferencedBlock += line[i]
            listOfOneIndirect = [int(inodeNumber), int(levelOfIndirection), int(logicalBlockOffset),
                                 int(blockNumOfIndirectBlockBeingScanned), int(blockNumOfReferencedBlock)]
            listOfLists.append(listOfOneIndirect)
        line = fd.readline()
    return listOfLists

def main():
    nameOfCSVfile = sys.argv[1]
    fd = open(nameOfCSVfile, "r")

    # This returns a list of elements in the superblock. To access a certain
    # type of element, use superBlockValues[i], where i is:
    # 0 = totalNumOfBlocks, 1 = totalNumOfInodes, 2 = blockSize, 3 = InodeSize,
    # 4 = blocksPerGroup, 5 = InodesPerGroup, 6 = firstNonResInode
    superBlockValues = getSuperBlockValues(fd)

    # These two return a list of free block/free inode numbers.
    freeBlockValues = getFreeBlocks(fd)
    freeInodeValues = getFreeInodes(fd)

    # This returns a list of lists. For inodeValue[i][j], i represents the 'i'th
    # inode summary. The j represents the 'j'th element in the inode summary. For
    # example, inodeValue[2][4] will return the group number (4) of the 3rd (2)
    # inode summary. To figure out which element number j corresponds to which
    # type of value, look near the end of the getInodeValues function.
    inodeValues = getInodeValues(fd)

    # Same as above, a list of lists. For dirValues[i][j], i represents the 'i'th
    # directory entry. The j represents the 'j'th element in the directory entry.
    # To figure out which element number j correspond to which type of value, look
    # near the end of the getDirEntries function.
    dirValues = getDirEntries(fd)

    # Same as above, a list of lists. For indirectValues[i][j], i represents the
    # 'i'th indirect block. The j represents the 'j'th element about that indirect
    # block. To figure out which element number j corresponds to which type of value,
    # look near the end of the getIndirectValues function.
    indirectValues = getIndirectValues(fd)
    
    # This is just test code to print out values of everything we just read in.
    # Feel free to modify/remove this.
    print superBlockValues
    print freeBlockValues
    print freeInodeValues
    for i in range(len(inodeValues)):
        print inodeValues[i]
    for i in range(len(dirValues)):
        print dirValues[i]
    for i in range(len(indirectValues)):
        print indirectValues[i]
    
    
if __name__ == '__main__':  
   main()
