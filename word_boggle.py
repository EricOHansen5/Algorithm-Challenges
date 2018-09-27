#https://practice.geeksforgeeks.org/problems/word-boggle/0

#-------------------

#Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. 
#Find all possible words that can be formed by a sequence of adjacent characters. 
#Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

#Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#       boggle[][]   = {{'G','I','Z'},
#                       {'U','E','K'},
#                       {'Q','S','E'}};

#Output:  Following words of dictionary are present
#         GEEKS, QUIZ

#-------------------

def word_boggle():
    dict_size = int(input())
    word_dict = input().split()
    mx_dims = [int(x) for x in input().split()]
    chars = input().split()
    
    char_mx = [""] * mx_dims[0]
    for i in range(mx_dims[0]):
        char_mx[i] = [""] * mx_dims[1]
    
    ix = 0
    for i in range(mx_dims[0]):
        for j in range(mx_dims[1]):
            char_mx[i][j] = chars[ix]
            ix += 1
    
    char_dict = {}
    final_list = []
    ix = 0
    while ix < len(word_dict):
        word = word_dict[ix]
        
        #----- Create Dict---------
        for i in range(mx_dims[0]):
            for j in range(mx_dims[1]):
                if char_mx[i][j] in word_dict[ix]:
                    #add to dict
                    if char_mx[i][j] in char_dict.keys():
                        char_dict[char_mx[i][j]].append((i,j))
                    else:
                        char_dict[char_mx[i][j]] = [(i,j)]
        #--------------------------
        
        #creates list to check if entire word in matrix with adj chars
        check_list = []

        pivot_list = []
        use_pivot = False
        
        #checks if first char in dictionary word in char dictionary
        if word[0] in char_dict.keys():
            #loops through the different starting points
            for first_index in char_dict[word[0]]:
                #adds first index to be checked
                check_list = [first_index]

                #index to enumerate dictionary word
                ix_word = 1
                #iterates over the rest of the word trying to find a path for entire word
                while ix_word < len(word):
                    #checks if next char in char dictionary
                    if word[ix_word] in char_dict.keys():
                        #bool to determine if this for loop added to checklist, if not no viable path
                        added_to_checklist = False
                        #loops through next char list to see if viable path
                        for next_index in char_dict[word[ix_word]]:
                            #grabs last index added to check_list
                            prev = check_list[-1]
                            #print(char_dict[word[ix_word]], next_index)
                            #checks if last index adj to current index
                            if (abs(prev[0] - next_index[0]) == 0 and abs(prev[1] - next_index[1]) == 1) or (abs(prev[0] - next_index[0]) == 1 and abs(prev[1] - next_index[1]) == 0) or (abs(prev[0] - next_index[0]) == 1 and abs(prev[1] - next_index[1]) == 1):
                                #adds remaining viable option paths to pivot_list and its index
                                if added_to_checklist == True:
                                    pivot_list.append(next_index)
                                else:
                                    #checks to make sure next index not already in check_list
                                    if next_index not in check_list and not use_pivot:
                                        #adds current index to check list if adj
                                        check_list.append(next_index)
                                        #sets flag to show added to check list
                                        added_to_checklist = True
                                    elif len(pivot_list) > 0 and use_pivot:
                                        pv_ix = pivot_list.pop()
                                        if pv_ix not in check_list:
                                            check_list.append(pv_ix)
                                            added_to_checklist = True
                        
                        #checks to make sure index was added to check list, if not no viable path was found for first index
                        if added_to_checklist == False:
                            break
                        #increment index of current word
                        ix_word += 1                    
                    else:
                        break
                
                #checks to see if while loop ended, if length of check_list equal to length of word append word to final_list
                #print(final_list, word_dict[ix], check_list)
                if len(check_list) == len(word_dict[ix]) and (word_dict[ix] not in final_list):
                    final_list.insert(0, word_dict[ix])
                    #break out of first for loop, since we are just checking for any viable path
                    break
                elif len(pivot_list) > 0:
                    use_pivot = True
                else:
                    use_pivot = False
        ix += 1
        char_dict = {}
        
    if len(final_list) > 0:
        final_list.sort()
        return " ".join(final_list)
    else:
        return -1

t = int(input())
for _ in range(t):
	print(word_boggle())