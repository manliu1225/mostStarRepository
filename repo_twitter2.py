from repo_twitter import *

def listDeployKeys(user_name,repos):

	file_name="http://api.github.com/repos/"+user_name+"%s/keys?per_page=100" % repos
	repo_DeployKeys = requests.get(file_name)
	repo_DeployKeys
	#print "contents is %s" % repo_contents
	raw_data=json.loads(repo_DeployKeys.text)

	return raw_data


def writeDeployKeysToCSV(deployKeys):#write to csv
	f = csv.writer(open("mostStarReposDeployKeys.csv", "wb+"))
	item_keys    = []
	item_values = []


	write_header=True

	for k , v in deployKeys.iteritems():

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
				if write_header:
		 			rowName=k+"/"+innerkey
		 			item_keys.append(rowName)	
		 		item_values.append(innervalue)
		 									

	if write_header:
		f.writerow(item_keys)
	f.writerow(item_values)



def listDeployment(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/deployments?per_page=100&page=%d" %(repos,j)
		repo_deployments = requests.get(file_name)
		print repo_deployments#if success(200)
		raw_data=json.loads(repo_deployments.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data


def writeDeploymentsToCSV(deployments):#write to csv
	f = csv.writer(open("mostStarReposDeployments.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(deployments)):	
		singleDeployment=deployments[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleDeployment.iteritems():
			v=convert(v)#convert unicode to str and dict
		 	
		 	if type(v) == type(""):#if it is not a dict
		 		#print v
		 		if write_header:
		 			item_keys.append(k)
		 		item_values.append(v)
		 	else:#it is a dict

		 		#print type(v)
		 		for innerkey, innervalue in v.iteritems():
		 			if write_header:
		 				rowName=k+"/"+innerkey
		 				item_keys.append(rowName)
		 			item_values.append(innervalue)

		if write_header:
			f.writerow(item_keys)
		f.writerow(item_values)


def listForks(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/forks?per_page=100&page=%d" %(repos,j)
		repo_forks = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_forks.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeForksToCSV(forks):#write to csv
	f = csv.writer(open("mostStarReposForks.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(forks)):	
		singleFork=forks[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleFork.iteritems():
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
	data=Get_data(user_name)
	
	mostStarRepos=mostStar_repos(data)
	print(mostStarRepos.get("name"))#print the most star repository name
	print "mostStarRepos atrribute number is %d" % len(mostStarRepos)#69

	deployKeys = listDeployKeys(user_name, mostStarRepos.get("name"))
	print "deployKeys number is %d" % len(deployKeys)#2


	deployments = listDeployment(user_name, mostStarRepos.get("name"))
	print "deployments number is %d" % len(deployments)#0
	#print "one deployments has atrribute number is %d" % len(deployments[1])#2

	forks = listForks(user_name, mostStarRepos.get("name"))
	print "forks number is %d" % len(forks)#2419
	print "one forks has atrribute number is %d" % len(forks[1])#68

	writeDeployKeysToCSV(deployKeys)
	writeDeploymentsToCSV(deployments)
	writeForksToCSV(forks)



if __name__=="__main__":
	main()	




