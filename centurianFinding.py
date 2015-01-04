import praw
import sys, traceback

#Filling these fields is not necessary. The program will just ask for login at runtime, instead.
username = '' #Century Club Member's Username
password = '' #Century Club Member's Password

print("Creating Client.")
r = praw.Reddit("chrome")
print("Logging in.")
r.login(username,password)

print("Getting /r/CenturyClub information.")
cc = r.get_subreddit("CenturyClub")

print("Loading offline Centurian List.")
file = open("C:/python27/personal/CC Lists/centurians.txt", "r")
centurians = []
for line in file:
    centurians.append(line.split("\n")[0])
file.close()

print("Loading approval-banned Centurians.")
ab = cc.get_wiki_page('index/approval-bans').content_md.split("\r\n\r\n")

old_comments = []

print("Scanning...")
while(True):
	try:
		comments = r.get_comments("all",limit=25)
		for c in comments:
			candidate = c.author
			if(c.name in old_comments):
				pass
			elif(max(candidate.comment_karma,candidate.link_karma) >= 100000):
				old_comments.insert(0,c.name)
				while(len(old_comments)>50):
					old_comments.pop()
				if(candidate.name not in centurians and candidate.name.lower() not in ab):
					centurians.insert(0,candidate.name)
					cc.add_contributor(candidate.name)
					print(candidate.name)
					r.create_subreddit(candidate.name,"Personal Subreddit","Not yet active")
	except KeyboardInterrupt:
		break
	except:
		pass
		
				
file = open("C:/python27/personal/CC Lists/centurians.txt", "w")
for name in centurians:
    file.write(name+"\n")
file.close()
