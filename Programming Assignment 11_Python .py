#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to find all string
# which are greater than given length k

# function find string greater than length k
def string_k(k, str):
	
	# create the empty string
	string = []
	
	# split the string where space is comes
	text = str.split(" ")
	
	# iterate the loop till every substring
	for x in text:
		
		# if length of current sub string
		# is greater than k then
		if len(x) > k:
			
			# append this sub string in
			# string list
			string.append(x)
			
	# return string list
	return string


# Driver Program	
k = 3
str ="geek for geeks"
print(string_k(k, str))


# In[2]:


# Python3 program for removing i-th
# indexed character from a string

# Removes character at index i
def remove(string, i):

	# Characters before the i-th indexed
	# is stored in a variable a
	a = string[ : i]
	
	# Characters after the nth indexed
	# is stored in a variable b
	b = string[i + 1: ]
	
	# Returning string after removing
	# nth indexed character.
	return a + b
	
# Driver Code
if __name__ == '__main__':
	
	string = "geeksFORgeeks"
	
	# Remove nth index element
	i = 5
	
	# Print the new string
	print(remove(string, i))


# In[3]:


# Python program to split a string and
# join it using different delimiter

def split_string(string):

	# Split the string based on space delimiter
	list_string = string.split(' ')
	
	return list_string

def join_string(list_string):

	# Join the string based on '-' delimiter
	string = '-'.join(list_string)
	
	return string

# Driver Function
if __name__ == '__main__':
	string = 'Geeks for Geeks'
	
	# Splitting a string
	list_string = split_string(string)
	print(list_string)

	# Join list of strings into one
	new_string = join_string(list_string)
	print(new_string)


# In[4]:


# Python program to check
# if a string is binary or not

# function for checking the
# string is accepted or not


def check(string):

	# set function convert string
	# into set of characters .
	p = set(string)

	# declare set of '0', '1' .
	s = {'0', '1'}

	# check set p is same as set s
	# or set p contains only '0'
	# or set p contains only '1'
	# or not, if any one condition
	# is true then string is accepted
	# otherwise not .
	if s == p or p == {'0'} or p == {'1'}:
		print("Yes")
	else:
		print("No")


# driver code
if __name__ == "__main__":

	string = "101010000111"

	# function calling
	check(string)


# In[7]:


# Python3 program to find a list of uncommon words

# Function to return all uncommon words
def UncommonWords(A, B):

	# count will contain all the word counts
	count = {}
	
	# insert words of string A to hash
	for word in A.split():
		count[word] = count.get(word, 0) + 1
	
	# insert words of string B to hash
	for word in B.split():
		count[word] = count.get(word, 0) + 1

	# return required list of words
	return [word for word in count if count[word] == 1]

# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

# Print required answer
print(UncommonWords(A, B))


# In[8]:


string = input("enter the string whose duplicate characters you want to find:")

def duplicates_char(s):
    elements = {}
    for char in s:
        if elements.get(char,None) != None:
            elements[char]+=1
        else:
            elements[char] = 1
    return [k for k,v in elements.items() if v>1]
print("the duplicate character in",string,"is")
print(duplicates_char(string))


# In[9]:


# Python3 program to check if a string
# contains any special character

# import required package
import re

# Function checks if the string
# contains any special character
def run(string):

	# Make own character set and pass
	# this as argument in compile method
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	
	# Pass the string in search
	# method of regex object.
	if(regex.search(string) == None):
		print("String is accepted")
		
	else:
		print("String is not accepted.")
	

# Driver Code
if __name__ == '__main__' :
	
	# Enter the string
	string = "Geeks$For$Geeks"
	
	# calling run function
	run(string)


# In[ ]:




