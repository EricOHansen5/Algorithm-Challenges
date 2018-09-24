#link to challenge: https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring/0
#------------------
#Given a string you need to print the size of the longest possible substring that has exactly k unique characters. 
#If there is no possible substring print -1.

#Example
#For the string aabacbebebe and k = 3 the substring will be cbebebe with length 7.

#The first line of input contains an integer T denoting the no of test cases then T test cases follow. 
#Each test case contains two lines . The first line of each test case contains a string s and the next line conatains an integer k.
#------------------


def longest_k_unique_chars_substring(inStr,k):
    inStrLen = len(inStr)
    charsSeen = []
    firstSeen = [None] * k
    lastSeen = [None] * k
    subStrLens = []
    subStrs = []    
    
    if len(inStr) < k:
        return -1
    
    idx = 0
    while idx < inStrLen:
        curChar = inStr[idx]
        if curChar in charsSeen:
            lastSeen[charsSeen.index(curChar)] = idx
            idx = idx + 1
        if curChar not in charsSeen and len(charsSeen) < k:
            charsSeen.append(curChar)
            firstSeen[charsSeen.index(curChar)] = lastSeen[charsSeen.index(curChar)] = idx
            idx = idx + 1
        if curChar not in charsSeen and len(charsSeen) == k:                           
            subStrLens.append(max(lastSeen)+1 - min(firstSeen))            
            lastSeenIdx = min(lastSeen)
            subStrs.append(inStr[min(firstSeen):max(lastSeen)+1])            
            charsSeen = []
            lastSeen = [None]*k
            firstSeen = [None]*k            
            idx = lastSeenIdx +1   
    if idx == inStrLen:
            subStrLens.append(max(lastSeen)+1 - min(firstSeen))        
            subStrs.append(inStr[min(firstSeen):max(lastSeen)+1])                       
                           
    if max(subStrLens) < k:
        return - 1
    
    return max(subStrLens)
            

    
    
    
T = int(input())
for _ in range(T):
    inputStr = input()
    k = int(input())
    print(longest_k_unique_chars_substring(inputStr,k))