#https://practice.geeksforgeeks.org/problems/jumping-numbers/0

#----------------------------

#Print all Jumping Numbers smaller than or equal to a given value
#A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1.
#All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

#Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can be printed in any order.

#----------------------------

def jumping_numbers():
    
    input_str = input() #string value
    val = int(input_str)#value of string
    
    final = []          #final list of numbers
    final.append("0")   #adds first list item
    
    que = []            #creates child queue
    
    #iterate from 1 to 9 as the different roots for tree
    for i in range(1, 10):
        si = str(i)     #string value of i
        pos = str(i+1)  #string value of i+1
        neg = str(i-1)  #string value of i-1
        
        #add string value of i if less than input value
        if si not in final and i <= val:
            final.append(si)
            
        #insert children into queue
        que.insert(0, si + neg)
        que.insert(0, si + pos)
        
        while len(que) > 0:
            child = que.pop()       #gets child out of queue
            int_c = int(child)      #value of child string
            lst_c = int(child[-1])  #value of last character of string
            
            #checks value of child string is less or equal to input value and not in final list
            if int_c <= val and child not in final:
                final.append(child)
                
                #char integers -1 and +1 of original
                c_neg = lst_c - 1
                c_pos = lst_c + 1
                
                #strings of those integers
                s_neg = str(c_neg)
                s_pos = str(c_pos)
                
                #checks value doesn't equal -1, value of full is less or equal than input value and not already in final list
                if c_neg >= 0:
                    val_neg = int(child + s_neg)    #value of string
                    str_neg = str(val_neg)          #string of value
                    
                    #checks if value of appended string less or equal to input value and string not in final list
                    if val_neg <= val and str_neg not in final:
                        final.append(str_neg)   #adds to final list
                        que.insert(0, str_neg)  #adds new child to queue
                
                #checks value less or equal to 9, value of full is less or equal than input value and not already in final list
                if c_pos <= 9:
                    val_pos = int(child + s_pos)    #value of string
                    str_pos = str(val_pos)          #string of value
                    
                    #checks if value of appended string less or equal to input value and string not in final list
                    if val_pos <= val and str_pos not in final:
                        final.append(str_pos)   #adds to final list
                        que.insert(0, str_pos)  #adds new child to queue
    #returns final list
    print (len(final))
    return final
    
t = int(input())
for _ in range(t):
    print (" ".join(map(str,jumping_numbers())))
