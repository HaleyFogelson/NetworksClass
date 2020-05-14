# Author: Haley Fogelson
# Please fill in the following functions below
# - DO NOT change the function definitions
# - This assignment will be graded with an automated grading script
# - Be sure that you have the correct 
# return type listed in the assignment

#import numpy as np
#using a non coe computer you can use outside libraries like numpy by calling
#pip3 install numpy 
import os as os
#import the system
import sys


#problem_one: string->string
#function that reverses a string
#goes through a each number 0 to the length of the string -1 one then adds the charecter
#at that index to the result string which is returned after the loop
def problem_one(test_string):
	#contract checking to make sure input is a string
	if(type(test_string)==str):
		#intializes a variable to hold the result string
		result=""
		#loops through so i equals each numbers 0 to the strings length-1  
		for i in range(len(test_string)):
			#adds the letter i from spaces the back to the result
			result+=test_string[len(test_string)-i-1]
		#returns the result	
		return result	

#problem_two: string->ListOf[string]
# function that returns a sentence as a list of words 
#first makes sure the imput is a string that calls split on the default " " charecter
def problem_two(test_sentence):
	#contract checking to make sure input is a string
	if(type(test_sentence)==str):
		#calls the split function to split function on the space charecter
		return test_sentence.split()
	
#problem_three: int, ListOf[int]-->boolean
# says if a number is in a list
# first checks the input contract then goes through a loop to check each element returning true if it finds it
#if it goes through the entire loop and never finds it then returns false
def problem_three(in_number, in_list):
	#contract checking to make sure the 1st input is an int and the second is a list
	if(type(in_number)==int and type(in_list)==list):
		#goes through each element in a list
		for i in in_list:
			#sees if that element is the number we are trying to find
			if i==in_number:
				#returns true if the current element is the number then exits out of function
				return True
		#returns false because we went through each element already and none of them were equal to the number we're looking for	
		return False
#contains: X, ListOf[X]-->boolean
# says if a something is in a list and the second thing passed in is a list
#this function is a helper function I use later in the hw
def contains(in_thing, in_list):
	#contract checking to make sure the 2nd input is a list
	if(type(in_list)==list):
		#goes through each element in the list
		for i in in_list:
			#sees if the element is equal to the value we are looking for
			if i==in_thing:
				#returns true if it found that element
				return True	
		#returns false because we went through each element already and none of them were equal to the thing we're looking for	
		return False				

#problem_four: int --> int
# summation function that sums the numbers 1 to the number passed in
def problem_four(in_number):
	#contract checking to make sure input is an int
	if(type(in_number)==int):
		#intializes a temperary varaible to keep track of the sum
		sum= 0
		#goes through each element from one up to thatg number
		for i in range(1,in_number+1):
			#adds the current element to the sum
			sum+=i
		#returns the sum	
		return sum

#problem_five:listof[x], listof[x]--> listof[x]	
# concatenates two lists and removes duplicates
def problem_five(li_one, li_two):
	#contract checking to make sure 1st and 2nd inputs are lists
	if(type(li_one)==list and type(li_two)==list):
		#intializes a temporary list to hold the result
		temp_list=[]
		#loops through each element in the first list and adds it if it is not already in the result
		for i in li_one:
			#calls the helper function contains to see if an element is already in the list
			if not contains(i, temp_list):
				#adds the element if it is not already in the list
				temp_list.append(i)
		#loops through each element in the second list and adds it if it is not already in the result		
		for i in li_two:
			#calls the helper function contains to see if an element is already in the list
			if not contains(i, temp_list):
				#adds the element if it is not already in the lis
				temp_list.append(i)
		#returns the result		
		return temp_list				


#problem_six: float--> float
# commputes the area of a circle
#squares the radius and multiplies it by pi
def problem_six(radius):
	#contract check to make sure input is a float
	if(type(radius)==float):
	#this is the command I would call on my own computer where I have the libraries
	#return radius*radius*np.pi
	#since the coe computers dont have numpy and won't let me install call this instead
	# i copied and pasted the pi value from numpy library running it myself
		return radius*radius*3.141592653589793
	

#problem_seven: string --> string
# makes a file with specific name and writes "Haley Fogelson" to that file
# reads from the file and deletes file then returns the files content
def problem_seven(file_name):
	#contract check to make sure input is a string
	if(type(file_name)==str):
		#makes a new file with the name passed in as teh file name
		f=open(file_name,"x")
		#writes "Haley Fogelson" to that file
		f.write("Haley Fogelson")
		#closes the file
		f.close()
		#opens the file with read permissions
		r=open(file_name,"r")
		#reads content from the file and stores it in the variable
		content=r.read()
		#closes the file
		f.close()
		#removes the file
		os.remove(file_name)
		#returns the content from the file
		return content

#problem_eight: string, char -->  int
# counts number of occurences of a specfic charecter in a string
def problem_eight(test_string, test_char):
	#contract checking to make sure the first input is a string and 2nd input is a char
	if(type(test_string)==str and type(test_char)==str and len(test_char)==1):
		#intializes a variable to keep track of repeates
		num=0
		#loops through each charecter in the string
		for i in test_string:
			#sees if the current element is equal to the charecter we are counting
			if i==test_char:
				#adds one to the counter if an instance of the charecter was found
				num+=1
		#returns the counter		
		return num;
		

#None-->string
# returns the version of python I am using 
def problem_nine():
	#calls the version function of system library
	return(sys.version)

#isListOfemails: listOf[string] --> boolean
#says if the thing passed in is a list of emails
def isListOfemails(email_list):
	#contract checking to make sure the input is a list
	if(type(email_list)!=list):
		#returns false if it is not a list and exits out of function
		return False
	#loops through each element in the list to make sure the elements of the list are strings that contain '@' charecter	
	for e in email_list:
		#sees if the element is either not a string or does not contain @
		if (type(e)!=str or e.find("@")== -1):
			#returns false if either of those statements above are true
			return False
	#returns true if were able to interate over entire list w/o returning false meaning all elements in the list are emails	
	return True		


#problem_ten: listOf[string]-->listof[string]
# takes a list of emails and returns the domain and extension of each with no repeates
def problem_ten(email_list):
	#input contract checking using the isListofemails helper function created above
	if(isListOfemails(email_list)):
		#intializes a list to hold the result
		domainList=[]
		#loops through each email in the list
		for e in email_list:
			#gets the substring of the current email from the spot after the @ to the end of the string
			string = e[e.find("@")+1:len(e)]
			#sees if that domain name is already in the list using the contains helper function
			if not contains(string,domainList):
				#adds the substring to the list of domain names
				domainList.append(string)
		#returns the result		
		return domainList
		



# Put main here:
#this is the main function where I call all the hw questions testing a case where should return none
#and where it actually works. These are kinda like check-expects but check the terminal output to make 
#sure they are equal to the comment below each
if __name__== '__main__':
	print(problem_one("hello"))
	#-->olleh
	print(problem_one("hello")=="olleh")
	print(problem_one(345678))
	#-->None
	print(problem_one(345678)==None)
	print(problem_two("this is a sentence")) 
	#-->['this', 'is', 'a', 'sentence']
	print(problem_two("this is a sentence")==['this', 'is', 'a', 'sentence'])
	print(problem_two(3456)) 
	#-->None
	print(problem_two(3456)==None) 
	print(problem_three(3,[1, 2]))
	#-->False
	print(problem_three(2,[1, 2]))
	#-->True
	print(problem_three("apple",[1, 2]))
	#-->None
	print(problem_four(3))	
	#-->6
	print(problem_four(3.0))	
	#-->None
	print(problem_five([1,2,2,3],["a",2, "hi"] ))
	#-->[1, 2, 3, 'a', 'hi']
	print(problem_five([1,2,2,3],45678 ))
	#-->None
	print(problem_six(1.0))
	#-->3.141592653589793
	print(problem_six(1))
	#-->None
	print(problem_seven("hello.txt"))
	#-->Haley Fogelson
	print(problem_seven(345678))
	#-->None
	print(problem_eight("hello",'l'))
	#-->2
	print(problem_eight("hello",'llo'))
	#-->None	
	print(problem_nine())
	#-->3.7.6 (default, Dec 30 2019, 19:38:28) 
	#-->[Clang 11.0.0 (clang-1100.0.33.16)]
	print(problem_ten(["test1@gmail.com", "test3@gmail.com", "@123"]))
	#-->['gmail.com', '123']
	print(problem_ten(["test1@gmail.com", "test3gmail.com", "@123"]))
	#-->None
	print(problem_ten(["test1@gmail.com", "test3gmail.com", 3]))
	#-->None

