import praw

r = praw.Reddit('Approve to hangout')

r.login()

hangout_url = raw_input('Enter hangout url: ')

seen = []
in_hangout = []

def add_to_seen(mail):
	seen.insert(0,mail)
	if(len(seen)>=27):
	    seen.pop()

def check_file():
	file = open('in_hangout.txt','r')
	in_hangout = []
	for line in file:
		in_hangout += [line.strip().lower()]
	file.close()
	return in_hangout
	
in_hangout = check_file()
cur = None
update_list = False

while(True):
	inbox = r.get_inbox(limit = 3)
	if(update_list):
		file = open('in_hangout.txt','w')
		for user in in_hangout:
			file.write(user+'\n')
		file.close()
		update_list = False
	in_hangout = check_file()
	while(cur not in seen):
		try:
			cur = inbox.next()
		except:
			break
		add_to_seen(cur.name)
		if(cur.subject=='hangout' and cur.body=='request-url'):
			if(len(in_hangout)<12):
				if(cur.author.name.lower() not in in_hangout):
					cur.reply(hangout_url)
					in_hangout+=[cur.author.name.lower()]
					update_list = True
					print('Adding ' + cur.author.name)
			else:
				cur.reply("Hangout currently full. Standbye. Informing human-randy.")
				print('Rejecting ' + cur.author.name + ' due to capacity')