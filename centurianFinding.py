import praw

#Filling these fields is not necessary. The program will just ask for login at runtime, instead.
username = '' #Century Club Member's Username
password = '' #Century Club Member's Password

print "Creating Client."
r = praw.Reddit("chrome")
print "Logging in."
r.login(username,password)

print "Getting /r/CenturyClub information."
cc = r.get_subreddit("CenturyClub")

print("Loading offline Centurian List.")
file = open("./Created_by_me/CC Lists/centurians.txt", "r")
centurians = []
for line in file:
    centurians.append(line.split("\n")[0])
file.close()

while(True):
	try:
		comments = r.get_comments("all",limit=25)
		for c in comments:
			candidated = c.author
			if(max(candidate.link_karma,candidate.comment_karma) >= 100000):
				if(! candidate in centurians):
					cc.send_message("New Centurian","/u/"+candidate.name)
					centurians.insert(0, candidate.name)
	except KeyboardInterrupt:
		break
				
file = open("./Created_by_me/CC Lists/centurians.txt", "w")
for name in centurians:
    file.write(name+"\n")
file.close()
