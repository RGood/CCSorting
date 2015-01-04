import praw

print "Creating Client."
r = praw.Reddit("chrome")

print "Getting /r/CenturyClub information."
cc = r.get_subreddit("CenturyClub")

print "Opening Contributors List."
ccc = open("C:/python27/Created_by_me/CC Lists/centurians.txt","r")

shadowbanned = open("C:/python27/Created_by_me/CC Lists/shadowbanned.txt","w+")

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
