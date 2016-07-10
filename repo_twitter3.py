from repo_twitter import *





def listReleases(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/releases?per_page=100&page=%d" %(repos,j)
		repo_releases = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_releases.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeReleasesToCSV(releases):#write to csv
	f = csv.writer(open("mostStarReposReleases.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(releases)):	
		singleRelease=releases[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleRelease.iteritems():
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



def listStats(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/stats/contributors?per_page=100&page=%d" %(repos,j)
		repo_stats = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_stats.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeStatsToCSV(stats):#write to csv
	f = csv.writer(open("mostStarReposStats.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(stats)):	
		singleStat=stats[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleStat.iteritems():
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


def listStatsWeek(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/stats/commit_activity?per_page=100&page=%d" %(repos,j)
		repo_statsWeek = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_statsWeek.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeStatsWeekToCSV(statsWeek):#write to csv
	f = csv.writer(open("mostStarReposStatsWeek.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(statsWeek)):	
		singleStatWeek=statsWeek[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleStatWeek.iteritems():
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


def listWeekAddDel(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/stats/code_frequency?per_page=100&page=%d" %(repos,j)
		repo_weekAddDel = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_weekAddDel.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeWeekAddDelToCSV(weekAddDel):
  
	#f = csv.writer(open("mostStarReposStatsWeek.csv", "wb+"))

  	with open('mostStarReposWeekAddDel'+'.csv', 'wb') as csvfile:
  		userwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
		userwriter.writerow(['Week', 'Addition', 'Deletion'])
		for i in range(len(weekAddDel)):
			userwriter.writerow([weekAddDel[i][0],weekAddDel[i][1],weekAddDel[i][2]])

def listWeekAllOwner(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

		
	file_name="http://api.github.com/repos/"+user_name+"%s/stats/participation?per_page=100" %(repos)
	repo_weekAllOwner = requests.get(file_name)
		#print repo_contributors#if success(200)
	print repo_weekAllOwner
	raw_data=json.loads(repo_weekAllOwner.text)

	return raw_data

def writeWeekAllOwnerToCSV(weekAllOwner):
  
	#f = csv.writer(open("mostStarReposStatsWeek.csv", "wb+"))

  	f = csv.writer(open("mostStarReposWeekAllOwner.csv", "wb+"))
	item_keys    = []
	item_values = []

	f.writerow(weekAllOwner.keys())
	f.writerow(weekAllOwner.values())

def listHourDayCommits(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/stats/punch_card?per_page=100&page=%d" %(repos,j)
		repo_hourDayCommit = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_hourDayCommit.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeHourDayCommitToCSV(hourDayCommit):
  
	#f = csv.writer(open("mostStarReposStatsWeek.csv", "wb+"))

  	with open('mostStarReposHourDayCommit'+'.csv', 'wb') as csvfile:
  		userwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
		userwriter.writerow(['Day', 'Hour', 'Commits'])
		for i in range(len(hourDayCommit)):
			userwriter.writerow([hourDayCommit[i][0],hourDayCommit[i][1],hourDayCommit[i][2]])




def main():
	reload(sys)
	sys.setdefaultencoding("utf-8")
	user_name='twitter/'
	data=Get_data(user_name)
	
	mostStarRepos=mostStar_repos(data)
	print(mostStarRepos.get("name"))#print the most star repository name
	print "mostStarRepos atrribute number is %d" % len(mostStarRepos)#69

	statsWeek = listStatsWeek(user_name, mostStarRepos.get("name"))
	print "statsWeek number is %d" % len(statsWeek)#52


	stats = listStats(user_name, mostStarRepos.get("name"))
	print "stats number is %d" % len(stats)#70
	print "one stats has atrribute number is %d" % len(stats[1])#3

	releases = listReleases(user_name, mostStarRepos.get("name"))
	print "releases number is %d" % len(releases)#0
	#print "one releases has atrribute number is %d" % len(releases[1])#68

	weekAddDel = listWeekAddDel(user_name, mostStarRepos.get("name"))
	print "weekAddDel number is %d" % len(weekAddDel)#177

	weekAllOwner = listWeekAllOwner(user_name, mostStarRepos.get("name"))
	print "weekAllOwner attribute number is %d" % len(weekAllOwner)#2

	hourDayCommits = listHourDayCommits(user_name, mostStarRepos.get("name"))
	print "hourDayCommits  number is %d" % len(hourDayCommits)#168


	writeStatsWeekToCSV(statsWeek)
	writeStatsToCSV(stats)
	writeReleasesToCSV(releases)
	writeWeekAddDelToCSV(weekAddDel)
	writeWeekAllOwnerToCSV(weekAllOwner)
	writeHourDayCommitToCSV(hourDayCommits)



if __name__=="__main__":
	main()	




