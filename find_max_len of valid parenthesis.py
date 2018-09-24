#https://practice.geeksforgeeks.org/problems/valid-substring/0

#------------------------

#Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid substring.

#NOTE: Length of smallest the valid substring ( ) is 2.

#Input
#The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
#The first line of each test case contains a string S consisting only of ( and ).

#Output
#Print out the length of the longest valid substring.

#Examples 

#Input
#4
#(()(
#()()((
#((()()())))
#()(())(

#Output
#2
#4
#10
#6

#------------------------

def find_max_len():
	#get string input "())()()()(()))(()((((()))()()()())))"
	arr = input()
	
	#stack of indexes, stores the indexes of the '(' chars
	stack_index = []
	stack_index.append(-1)
	
	#return value
	final_out = 0

	#traverse all chars of array
	for i in range(len(arr)):
		#checks if current index in the array is equal to '(' char, if so append to index stack
		if arr[i] == '(':
			stack_index.append(i)
		else:
		#else char is ')'
			#which pops the last index off to remove last index of '(' char
			stack_index.pop()
			
			#if ')' char received and stack is not empty stores max between current index
			# and the last substring end char index
			if len(stack_index) != 0:
				final_out = max(final_out, i - stack_index[-1])
			else:
				#if stack_index length equals 0 append end character substring index
				stack_index.append(i)
	return final_out

t = int(input())
for _ in range(t):
	print(find_max_len())