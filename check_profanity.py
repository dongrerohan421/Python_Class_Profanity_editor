import urllib  

def read_text(): # define function to read text
	quotes = open("/media/rohan/3814F06A14F02C8E/Study/Udacity/Python/Python_Class_Profanity_editor/movie_quotes.txt") # opens file from location
	content_of_file = quotes.read() #allow to read all content from open file
	print (content_of_file)
	quotes.close() # close opened file
	check_profanity(content_of_file) # calling function

def check_profanity(text_to_check): # define function to check profanity
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check) # open connection from internet
	output = connection.read() # read response from website
	print(output)
	connection.close() # close the connection
	if "true" in output:
		print ("Profanity alert!!")
	elif "false" in output :
		print("This document has no curse words!")
	else :
		print ("Could not scan the document properly.")
read_text() # call function
