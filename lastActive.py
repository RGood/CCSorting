import praw
import time

r = praw.Reddit('Last public')\

r.login()

contribs = []
file = open('../CC Lists/Centurians.txt','r')
for line in file:
	contribs.append(line.strip())
file.close()

for c in contribs:
	try:
		user = r.get_redditor(c)
		activity = (time.time() - user.get_overview().__next__().created_utc) / (60 * 60 * 24)
		if(activity>10):
			print("/u/" + c + " was last visibly active " + str(activity) + " days ago.")
	except:
		pass