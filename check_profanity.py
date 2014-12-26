def read_text(): # define function to read text
	quotes = open("/media/rohan/3814F06A14F02C8E/Study/Udacity/Python/Python_Class_Profanity_editor/movie_quotes.txt") # opens file from location
	content_of_file = quotes.read() #allow to read all content from open file
	print (content_of_file)
	quotes.close() # close opened file

read_text() # call function
