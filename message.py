# Denise Irvin
# December 10, 2014


# This code uses a list of usernames, checks if they are 
# currently logged on, and for each logged on username, 
# opens a chat over a linux system, sends a precoded 
# message, and closes the chat.

# Uses the 'print' function, which does not exist in early versions of python

import subprocess
from subprocess import  Popen, PIPE 

a = subprocess.Popen("who", stdout = subprocess.PIPE, shell = True)
(output, err) = a.communicate()

# Lists used to store the usernames and places on the server of the people currently logged in
parsed_users = output.split("\n")
usn = []
spot = []

# people is a list of the people you wish to send a message to 
people = ["username ","username2"]	
are_people_on = []

#assigns list, assuming every username in people is logged off
for person in people:
	are_people_on.append(False)

#checks to see if people are logged in or not; kinda inefficient, but changes a corresponding bool value to true
for x in parsed_users:
	usn.append(x[0:9])
	spot.append(x[9:15])
	
#goes through to see if this username matches anyone in the list	
	for person in people:
		if usn[len(usn) - 1] == person:
			index = people.index(person)
			are_people_on[index] = True
			print 'User {0} is on.'.format(person)		# This line reports who is logged on to the console
			break

#calls people
index = 0
for bool_val in are_people_on:
	if bool_val:
		parsed_users_index = usn.index(people[index]) 
		p1 = Popen(["write", usn[parsed_users_index].strip(), spot[parsed_users_index]], stdin=PIPE, stdout=PIPE)
		
		p1.stdin.write('Hello World\n') # The actual message being sent
		
		p1.stdin.close()

	index += 1	

