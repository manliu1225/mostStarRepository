from repo_twitter import *


def listIssures(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/issues?per_page=100&page=%d" %(repos,j)
		repo_issues = requests.get(file_name)
		print repo_issues#if success(200)
		raw_data=json.loads(repo_issues.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeIssuesToCSV(issues):#write to csv
	#f = csv.writer(open("mostStarReposIssues.csv", "wb+"))
	item_keys    = []
	item_values = []
	count = 0
	count1 = 0

	for i in range (len(issues)):	
		singleIssue=issues[i]
		

		item_values = []

		if singleIssue.keys()[0] == "body":
			count1 = count1 + 1
			writeIssuesToCSV2(singleIssue,count1,1,211)

			# if count == 559:
			# 	write_header = True
			# else: write_header = False

			# for k , v in singleIssue.iteritems():
			# 	#if isinstance(v,basestring) == True:
			# 		#print v
			# 		#v = unicodedata.normalize('NFKD',v).encode('ascii', 'ignore')
			# 		#v=convert(v)#convert unicode to str and dict
			 	
			#  	if type(v) is not  types.DictType:#if it is not a dict
			#  		#print k,v
			#  		if write_header:
			#  			item_keys.append(k)
			#  		item_values.append(v)
			#  	else:#it is a dict

			#  		#print k,v
			#  		for innerkey, innervalue in v.iteritems():
			#  			if type(innervalue) is not types.DictType:
			#  				if write_header:
			#  					rowName=k+"/"+innerkey
			#  					item_keys.append(rowName)	
			#  				item_values.append(innervalue)
			#  			else:
			#  				for innerinnerkey, innerinnervalue in innervalue.iteritems():#invervalue is dict
			# 					if type(innerinnervalue) is not types.DictType:
			#  						if write_header:
			#  							rowName=k+"/"+innerkey+"/"+innerinnerkey
			#  							item_keys.append(rowName)	
			#  						item_values.append(innerinnervalue)
			#  					else:
			#  						for innerinnerinnerkey, innerinnerinnervalue in innerinnervalue.iteritems():
			#  							if write_header:
			#  								rowName=k+"/"+innerkey+"/"+innerinnerkey+"/"+innerinnerinnerkey
			#  								item_keys.append(rowName)
			#  							item_values.append(innerinnerinnervalue)




								

			# if write_header:
			# 	f.writerow(item_keys)
			# f.writerow(item_values)
		else:
			count = count+1
			writeIssuesToCSV2(singleIssue,count,2,72)
	print count, count1
	


def writeIssuesToCSV2(singleIssue,count,j,title):
	# print count
	# print len(singleIssue)
	f1 = csv.writer(open("mostStarReposIssues%d.csv" % j, "a+"))
	item_keys    = []
	item_values = []

	if count == title:
		write_header = True
	else: write_header = False


	for k , v in singleIssue.iteritems():
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
		f1.writerow(item_keys)
	f1.writerow(item_values)





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
	issues = listIssures(user_name, repos)
	print "issues number is %d" % len(issues)#337
	print "one issues has atrribute number is %d" % len(issues[1])#21

	
	writeIssuesToCSV(issues)



if __name__=="__main__":
	main()	




