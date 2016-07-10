from repo_twitter import *


def listAssignees(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/assignees?per_page=100&page=%d" %(repos,j)
		repo_assignees = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_assignees.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeAssigneesToCSV(assignees):#write to csv
	f = csv.writer(open("mostStarReposAssignees.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(assignees)):	
		singleassignees=assignees[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleassignees.iteritems():
			#if isinstance(v,basestring) == True:
				#print v
				#v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
				#v=convert(v)#convert unicode to str and dict
		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		#print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		#print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)

def listCommentsForRepos(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=45

	while page_n == 100 and j < 50:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/issues/comments?per_page=100&page=%d" %(repos,j)
		repo_ReposComments = requests.get(file_name)
		print repo_ReposComments#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_ReposComments.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeReposCommentsToCSV(reposcomments):#write to csv
	f = csv.writer(open("mostStarReposCommentsForRepos.csv", "a+"))
	item_keys    = []
	item_values = []

	for i in range (len(reposcomments)):	
		singlereposcomments=reposcomments[i]
		# if i == 0:
		# 	write_header = True
		# else: write_header = False
		write_header = False

		item_values = []

		for k , v in singlereposcomments.iteritems():
			#if isinstance(v,basestring) == True:
				#print v
				#v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
				#v=convert(v)#convert unicode to str and dict
		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		#print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		#print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)



def listIssuesEvents(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=40

	while page_n == 100 and j < 48:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/issues/events?per_page=100&page=%d" %(repos,j)
		repo_issuesEvents = requests.get(file_name)
		print repo_issuesEvents#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_issuesEvents.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeIssuesEventsToCSV(issuesEvents):#write to csv
	f = csv.writer(open("mostStarReposIssuesEvents.csv", "a+"))
	item_keys    = []
	item_values = []

	for i in range (len(issuesEvents)):	
		singleissuesEvents=issuesEvents[i]
		# if i == 0:
		# 	write_header = True
		# else: write_header = False
		write_header = False

		item_values = []

		for k , v in singleissuesEvents.iteritems():
			#if isinstance(v,basestring) == True:
				#print v
				#v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
				#v=convert(v)#convert unicode to str and dict
		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		#print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		#print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)


def listIssuesMilestones(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/milestones?per_page=100&page=%d" %(repos,j)
		repo_issuesmilestones = requests.get(file_name)
		print repo_issuesmilestones#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_issuesmilestones.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeIssuesMilestonesToCSV(issuesmilestones):#write to csv
	f = csv.writer(open("mostStarReposIssuesMilestones.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(issuesmilestones)):	
		singleissuesMilestones=issuesmilestones[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleissuesMilestones.iteritems():
			#if isinstance(v,basestring) == True:
				#print v
				#v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
				#v=convert(v)#convert unicode to str and dict
		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		#print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		#print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)


def listIssuesLabels(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/labels?per_page=100&page=%d" %(repos,j)
		repo_issuesLabels = requests.get(file_name)
		print repo_issuesLabels#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_issuesLabels.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeIssuesLabelsToCSV(issuesLabels):#write to csv
	f = csv.writer(open("mostStarReposIssuesLabels.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(issuesLabels)):	
		singleissuesLabels=issuesLabels[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleissuesLabels.iteritems():
			#if isinstance(v,basestring) == True:
				#print v
				#v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
				#v=convert(v)#convert unicode to str and dict
		 	
		 	if type(v) is not  types.DictType:#if it is not a dict
		 		#print k,v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		#print k,v
		 		for innerkey, innervalue in v.iteritems():
		 			if type(innervalue) is not types.DictType:
		 				if write_header:
		 					rowName=k+"/"+innerkey
		 					item_keys.append(rowName)	
		 				item_values.append(innervalue)
		 			else:
		 				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
							if type(innerinnervalue) is not types.DictType:
		 						if write_header:
		 							rowName=k+"/"+innerkey+"/"+innerinnerkey
		 							item_keys.append(rowName)	
		 						item_values.append(innerinnervalue)
		 					else:
		 						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
		 							if write_header:
		 								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
		 								item_keys.append(rowName)
		 							item_values.append(innerinnerinnervalue)




							

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)





def main():
	reload(sys)
	sys.setdefaultencoding("utf-8")
	user_name='twitter/'
	repos="typeahead.js"
	#data=Get_data(user_name)
	
	#mostStarRepos=mostStar_repos(data)
	# print(mostStarRepos.get("name"))#print the most star repository name
	# print "mostStarRepos atrribute number is %d" % len(mostStarRepos)#69

	#issues = listIssures(user_name, mostStarRepos.get("name"))
	#assignees = listAssignees(user_name, repos)
	# print "assignees number is %d" % len(assignees)#186
	# print "one assignees has atrribute number is %d" % len(assignees[1])#17

	#reposcomments = listCommentsForRepos(user_name, repos)
	#print "reposcomments number is %d" % len(reposcomments)#4710


	# issuesEvents = listIssuesEvents(user_name, repos)
	# print "issuesEvents number is %d" % len(issuesEvents)#4433
	# print "one issuesEvents has atrribute number is %d" % len(issuesEvents[1])#9

	# issuesmilestones = listIssuesMilestones(user_name, repos)
	# print "issuesmilestones number is %d" % len(issuesmilestones)#2
	# print "one issuesmilestones has atrribute number is %d" % len(issuesmilestones[1])#15

	issuesLabels = listIssuesLabels(user_name, repos)
	print "issuesLabels number is %d" % len(issuesLabels)#11
	print "one issuesLabels has atrribute number is %d" % len(issuesLabels[1])#3
	
	
	#writeReposCommentsToCSV(reposcomments)
	#writeAssigneesToCSV(assignees)
	#writeIssuesEventsToCSV(issuesEvents)
	writeIssuesLabelsToCSV(issuesLabels)




if __name__=="__main__":
	main()	




