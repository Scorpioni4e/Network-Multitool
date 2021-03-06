import os
import sys

def userInput(user_input):
    # user_input = raw_input("Please enter URL. Please do not include http://: ")
	user_input.lower()
	cwd = os.getcwd()

	# Check for protocol
	def checkString(forbidden, string, error_message):
		if forbidden in string:
			user_input = None
			sys.exit(error_message)

	checkString("http://", user_input, "Please don't include http://. Try again")
	checkString("https://", user_input, "Please don't include https://. Try again")

	os.system("scrapy runspider -a url=" + user_input + " -s LOG_ENABLED=0 " + cwd + "/crawler/crawler_prod.py")

# userInput()
