import praw
import time

r = praw.Reddit('CenturyClub Approval Bot')

r.login()

print 'Loading subreddit...'
cc = r.get_subreddit('CenturyClub')

print 'Loading contrib list...'
contribs = cc.get_contributors(limit=None)
names = []
for c in contribs:
	names+=[c.name]
	
def push_to_seen(m):
	seen.insert(0,m)
	if(len(seen)>100):
		seen.pop()

print 'Buffering old mail...'
seen = []
mail = cc.get_mod_mail(limit=50)
for m in mail:
	push_to_seen(m.name)
		
print 'Scanning...'
running = True
while(running):
	try:
		mail = cc.get_mod_mail(limit=50)
		for m in mail:
			if(m.name not in seen):
				push_to_seen(m.name)
				karma = max(m.author.link_karma,m.author.comment_karma)
				if(karma >= 100000 and m.author.name not in names):
					cc.add_contributor(m.author.name)
					m.reply("You want karma?\n\nYou can't handle the truth.\n\nSon, we lurk in a website that has subreddits, and those subreddits have to be guarded by mods with banhammers. Who's gonna do it? You? You, /u/"+m.author.name+"? I have a greater responsibility than you could possibly fathom. You weep for /u/dw-im-here, and you curse the admins. You have that luxury. You have the luxury of not knowing what I know. That /u/dw-im-here's shadowban, while tragic, probably saved accounts. And my existence, while grotesque and incomprehensible to you, saves accounts. You don't want the truth because deep down in places you don't talk about at meetups, you want me modding that sub, you need me modding that sub. We use words like honor, code, loyalty. We use these words as the backbone of a \"life\" spent gaining karma. You use them as a punchline. I have neither the time nor the inclination to explain myself to a man who rises and sleeps under the blanket of the very moderation that I provide, and then questions the manner in which I provide it. I would rather you just said thank you, and went on your way, Otherwise, I suggest you pick up a subreddit, and remove a post. Either way, I don't give a damn what you think you are entitled to.\n\nYou're god damn right, I ordered the copy-pasta.")
					names+=[m.author.name]
					print m.author.name
					r.create_subreddit(candidate.name,"Personal Subreddit","Not yet active")
				elif(m.author.link_karma+m.author.comment_karma >= 100000 and karma < 100000):
					m.reply("/r/CenturyClub requires 100k link *or* comment karma for entry. The scores are not added together.")
				elif(m.author.name not in names):
					m.reply("You do not have enough karma for entry. /r/CenturyClub requires 100k link or comment karma for access. If you're messaging us for some other reason, then please disregard this response. If you thought you were clever, and figured you'd just click the link in our public description anyway, then you're stupid, and you should feel bad about yourself.\n\nHave a nice day.")
		time.sleep(300)
	except KeyboardInterrupt:
		running = False
	except Exception as e:
		pass
		
print 'Shutting down'