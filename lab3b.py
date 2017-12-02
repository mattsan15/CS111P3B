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
    RETURNVALUE = 0
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
    # inode summary.
    inodeValues = getInodeValues(fd)

    # Same as above, a list of lists. For dirValues[i][j], i represents the 'i'th
    # directory entry. The j represents the 'j'th element in the directory entry.
    dirValues = getDirEntries(fd)

    # Same as above, a list of lists. For indirectValues[i][j], i represents the
    # 'i'th indirect block. The j represents the 'j'th element about that indirect
    # block.
    indirectValues = getIndirectValues(fd)
    

    #Block Consistency Audits Algorithm
    #Inodes inconsistency
    for i in range(len(inodeValues)):
        for x in xrange(11,26):
            if (inodeValues[i][x] < 0 or inodeValues[i][x] > superBlockValues[0]):
                RETURNVALUE = 2
                if(x < 23):
                    sys.stdout.write("INVALID BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], x-11))
                elif (x == 23):
                    sys.stdout.write("INVALID INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], 12))    
                elif (x == 24):
                    sys.stdout.write("INVALID DOUBLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], 268))
                elif (x == 25):
                    sys.stdout.write("INVALID TRIPLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], 65804))
            #######################################################################################################################
            if (inodeValues[i][x] < ((superBlockValues[1]*superBlockValues[3])/superBlockValues[2])+5 and inodeValues[i][x] > 0):
                RETURNVALUE = 2
                if(x < 23):
                    sys.stdout.write("RESERVED BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], x-11))
                elif (x == 23):
                    sys.stdout.write("RESERVED INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], 12))    
                elif (x == 24):
                    sys.stdout.write("RESERVED DOUBLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], 268))
                elif (x == 25):
                    sys.stdout.write("RESERVED TRIPLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][x],inodeValues[i][0], 65804))
    ###############################################################################################################################
    #indirect block inconsistency
    for i in range(len(indirectValues)):
        if (indirectValues[i][4] < 0 or indirectValues[i][4] > superBlockValues[0]):
            RETURNVALUE = 2
            if(indirectValues[i][1] == 1):
                sys.stdout.write("INVALID INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(indirectValues[i][4],indirectValues[i][0],indirectValues[i][2]))
            elif (indirectValues[i][1] == 2):
                sys.stdout.write("INVALID DOUBLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(indirectValues[i][4],indirectValues[i][0],indirectValues[i][2]))
            elif (indirectValues[i][1] == 3):
                sys.stdout.write("INVALID TRIPLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(indirectValues[i][4],indirectValues[i][0],indirectValues[i][2]))
            #######################################################################################################################
        if (indirectValues[i][4] < ((superBlockValues[1]*superBlockValues[3])/superBlockValues[2])+5 and indirectValues[i][4] > 0):
            RETURNVALUE = 2
            if(indirectValues[i][1] == 1):
                sys.stdout.write("RESERVED INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(indirectValues[i][4],indirectValues[i][0],indirectValues[i][2]))    
            if(indirectValues[i][1] == 2):
                sys.stdout.write("RESERVED DOUBLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(indirectValues[i][4],indirectValues[i][0],indirectValues[i][2]))
            if(indirectValues[i][1] == 3):
                sys.stdout.write("RESERVED TRIPLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(indirectValues[i][4],indirectValues[i][0],indirectValues[i][2]))
    ###########################################################################################
    #UNREFRENCED
    UNREFRENCED_BLOCKS = {}
    for i in range(((superBlockValues[1]*superBlockValues[3])/superBlockValues[2])+5,superBlockValues[0]): #due to range implementation block 64 is not being checked for unrefrenced
        UNREFRENCED_BLOCKS[i] = False
        
    for i in range(len(inodeValues)):
        for j in xrange(11,26):
            UNREFRENCED_BLOCKS[inodeValues[i][j]] = True
    for i in range(len(indirectValues)):
        UNREFRENCED_BLOCKS[indirectValues[i][4]] = True
    for x in freeBlockValues:
        UNREFRENCED_BLOCKS[x] = True

    for i in range(((superBlockValues[1]*superBlockValues[3])/superBlockValues[2])+5,superBlockValues[0]): #due to range implementation block 64 is not being checked for unrefrenced
        if (UNREFRENCED_BLOCKS[i] == False):
            RETURNVALUE = 2
            sys.stdout.write("UNREFERENCED BLOCK {}\n".format(i))

    #ALLOCATED
    ALLOCATED_BLOCKS = {}
    for i in range(len(inodeValues)):
        for j in xrange(11,26):
            ALLOCATED_BLOCKS[inodeValues[i][j]] = False
    for i in range(len(indirectValues)):
        ALLOCATED_BLOCKS[indirectValues[i][4]] = False
    for x in freeBlockValues:
        if x in ALLOCATED_BLOCKS:
            RETURNVALUE = 2
            sys.stdout.write("ALLOCATED BLOCK {} ON FREELIST\n".format(x))

    #DUPLICATE_BLOCKS
    DUPLICATE_BLOCK = {}

    for i in range(len(inodeValues)):
        for j in xrange(11,26):
            if (inodeValues[i][j] > 0 and inodeValues[i][j] <= superBlockValues[0]):
                if inodeValues[i][j] in DUPLICATE_BLOCK:
                    DUPLICATE_BLOCK[inodeValues[i][j]] = True
                else:
                    DUPLICATE_BLOCK[inodeValues[i][j]] = False
    
    for i in range(len(indirectValues)):
        if (indirectValues[i][4] > 0 and indirectValues[i][4] <= superBlockValues[0]):
            if indirectValues[i][4] in DUPLICATE_BLOCK:
                DUPLICATE_BLOCK[indirectValues[i][4]] = True
            else:
                DUPLICATE_BLOCK[indirectValues[i][4]] = False
    
    for i in DUPLICATE_BLOCK:
        if (DUPLICATE_BLOCK[i] == True):
            for j in range(len(inodeValues)):
                for k in xrange(11,26):
                    if (inodeValues[j][k] == i):
                        RETURNVALUE = 2
                        if(k < 23):
                            sys.stdout.write("DUPLICATE BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[j][k],inodeValues[j][0], k-11))
                        elif (k == 23):
                            sys.stdout.write("DUPLICATE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[j][k],inodeValues[j][0], 12))    
                        elif (k == 24):
                            sys.stdout.write("DUPLICATE DOUBLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[j][k],inodeValues[j][0], 268))
                        elif (k == 25):
                            sys.stdout.write("DUPLICATE TRIPLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[j][k],inodeValues[j][0], 65804))
            
            for j in range(len(indirectValues)):
                if (indirectValues[i][4] == i):
                    RETURNVALUE = 2
                    if(indirectValues[i][1] == 1):
                        sys.stdout.write("DUPLICATE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][4],inodeValues[i][0],inodeValues[i][2]))
                    elif (indirectValues[i][1] == 2):
                        sys.stdout.write("DUPLICATE DOUBLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][4],inodeValues[i][0],inodeValues[i][2]))
                    elif (indirectValues[i][1] == 3):
                        sys.stdout.write("DUPLICATE TRIPLE INDIRECT BLOCK {} IN INODE {} AT OFFSET {}\n".format(inodeValues[i][4],inodeValues[i][0],inodeValues[i][2]))

##############################I-node Audits###################################

    #Allocation
    ALLOCATED_INODE = {}
    #Add all allocated nodes
    for i in range(len(inodeValues)):
        ALLOCATED_INODE[inodeValues[i][0]] = False


    for j in freeInodeValues:
        if j in ALLOCATED_INODE:
            ALLOCATED_INODE[j] = True

    for k in ALLOCATED_INODE:
        if (ALLOCATED_INODE[k] == True):
            RETURNVALUE = 2
            sys.stdout.write("ALLOCATED INODE {} ON FREELIST\n".format(k))

    #Un-Allocated
    UNALLOCATED_INODE = {}
    UNALLOCATED_INODE[2] = False
    for x in range(superBlockValues[6],superBlockValues[1]+1):
        UNALLOCATED_INODE[x] = False
    
    for j in freeInodeValues:
        if j in UNALLOCATED_INODE:
            UNALLOCATED_INODE[j] = True

    for i in range(len(inodeValues)):
        UNALLOCATED_INODE[inodeValues[i][0]] = True

    for i in UNALLOCATED_INODE:
        if (UNALLOCATED_INODE[i] == False):
            RETURNVALUE = 2
            sys.stdout.write("UNALLOCATED INODE {} NOT ON FREELIST\n".format(i))
###################################################################################################################
#####################Directory Audit########################################################
    #Directory Consistency Audits
    REFERENCE_COUNT = {}
    for i in range(len(dirValues)):
        if dirValues[i][2] in REFERENCE_COUNT:
            REFERENCE_COUNT[dirValues[i][2]] += 1
        else:
            REFERENCE_COUNT[dirValues[i][2]] = 1
          
    #Add all allocated nodes
    for i in range(len(inodeValues)):
        if(inodeValues[i][0] in REFERENCE_COUNT): 
            if(inodeValues[i][5] != REFERENCE_COUNT[inodeValues[i][0]]):
                RETURNVALUE = 2
                sys.stdout.write("INODE {} HAS {} LINKS BUT LINKCOUNT IS {}\n".format(inodeValues[i][0],REFERENCE_COUNT[inodeValues[i][0]],inodeValues[i][5]))
        else:
            if (inodeValues[i][5] != 0):
                RETURNVALUE = 2
                sys.stdout.write("INODE {} HAS 0 LINKS BUT LINKCOUNT IS {}\n".format(inodeValues[i][0],inodeValues[i][5]))

    #invalid inode
    for i in range(len(dirValues)):
        if (dirValues[i][2] < 1 or dirValues[i][2] > superBlockValues[1]):
            RETURNVALUE = 2
            sys.stdout.write("DIRECTORY INODE {} NAME {} INVALID INODE {}\n".format(dirValues[i][0],dirValues[i][5],dirValues[i][2]))

        if(dirValues[i][5] == '.'):
            if (dirValues[i][0] != dirValues[i][2]):
                RETURNVALUE = 2
                sys.stdout.write("DIRECTORY INODE {} NAME {} LINK TO INODE {} SHOULD BE {}\n".format(dirValues[i][0],dirValues[i][5],dirValues[i][2],dirValues[i][0]))

        if(dirValues[i][5]  == '\'..\''):
            if (dirValues[i][2] != 2):
                RETURNVALUE = 2
                sys.stdout.write("DIRECTORY INODE {} NAME {} LINK TO INODE {} SHOULD BE 2\n".format(dirValues[i][0],dirValues[i][5],dirValues[i][2]))
    
    #unallocated inode
    INODES = []
    for i in range(len(inodeValues)):
        INODES.append(inodeValues[i][0])

    for i in range(len(dirValues)):
        if ((dirValues[i][2] not in INODES) and dirValues[i][2] > 0 and dirValues[i][2] <= superBlockValues[1]):
            RETURNVALUE = 2
            sys.stdout.write("DIRECTORY INODE {} NAME {} UNALLOCATED INODE {}\n".format(dirValues[i][0],dirValues[i][5],dirValues[i][2]))

if __name__ == '__main__':  
   main()