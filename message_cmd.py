# Denise Irvin
# December 12, 2014


# This code uses a list of usernames, checks if they are 
# currently logged on, and for each logged on username, 
# opens a chat over a linux system, sends a message 
# that is a commandline argument, and closes the chat.

# Uses the 'print' function, which does not exist in early versions of python


#!/usr/bin/env python
#!/usr/bin/python
import subprocess
from subprocess import  Popen, PIPE 
import sys

string_message = " ".join(sys.argv[1:]) # Gets the message from the commandline

a = subprocess.Popen("who", stdout = subprocess.PIPE, shell = True)
(output, err) = a.communicate()


parsed_users = output.split("\n")
usn = []
spot = []


people = ["username"]
are_people_on = []

#assigns list with assuming everyone is logged off
for person in people:
	are_people_on.append(False)

#checks to see if people are logged in or not; kinda inefficient, but changes a corresponding bool value to true
for x in parsed_users:
	
	usn.append(x[0:9])
	spot.append(x[9:15])
	
#goes through to see if this username matches anyone who currently logged on	
	for person in people:
		if usn[len(usn) - 1] == person:
			index = people.index(person)
			are_people_on[index] = True
			print person + " is on!"
			break


#calls people
index = 0
for bool_val in are_people_on:
	if bool_val:
		parsed_users_index = usn.index(people[index]) 
		p1 = Popen(["write", usn[parsed_users_index].strip(), spot[parsed_users_index]], stdin=PIPE, stdout=PIPE)
		p1.stdin.write(string_message)
		p1.stdin.close()
	
	index += 1	