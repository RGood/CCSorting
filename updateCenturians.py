import praw

r = praw.Reddit('Python get /r/CenturyClub contributors')

r.login()

cc = r.get_subreddit('CenturyClub')

contribs = cc.get_contributors(limit=None)

file = open('../CC Lists/Centurians.txt','w')

for c in contribs:
	file.write(c.name+"\n")
	
file.close()

print("Done")