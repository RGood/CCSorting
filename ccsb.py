import praw

username = '' #Century Club Member's Username
password = '' #Century Club Member's Password

print "Creating Client."
r = praw.Reddit("chrome")

print "Logging in."
r.login(username,password)

print "Getting /r/CenturyClub information."
cc = r.get_subreddit("CenturyClub")

print "Opening Contributors List."
ccc = open("./Created_by_me/CCSorting/centurians.txt","r")

shadowbanned = open("./Created_by_me/CCSorting/shadowbanned.txt","w+")

print "Beginning Redditor Scan..."
for centurian in ccc:
	try:
		print r.get_redditor(centurian.split("\n")[0])
	except KeyboardInterrupt:
		print "Program stopped."
		break;
	except:
		print "***** " + centurian.split("\n")[0] + " has been Shadowbanned. *****"
		shadowbanned.write(centurian)

ccc.close()
shadowbanned.close()