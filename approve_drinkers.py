import praw

r = praw.Reddit('/r/CCGetsDrunk bot')

r.login()

cc = r.get_subreddit('CenturyClub')
ccgd = r.get_subreddit('CCGetsDrunk')

drinkers = []

for c in ccgd.get_contributors(limit=None):
    drinkers += [c]

submissions = cc.get_new(limit=100)

for post in submissions:
    if("drunk" in post.title.lower() or "drinking" in post.title.lower()):
	    if(post.author not in drinkers):
		    ccgd.add_contributor(post.author.name)