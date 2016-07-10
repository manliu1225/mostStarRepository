

import requests
import json
import csv
import collections
import types
import unicodedata
import sys

def convert(data):#unicode to dict
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


def Get_data(user_name):#get all repository about twitter
	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/orgs/"+user_name+"repos?per_page=100&page=%d" %(j)
		repo_twitter = requests.get(file_name)
		print repo_twitter#if success(200)
		raw_data=json.loads(repo_twitter.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	print len(data)#print the number of repository
	return data

def mostStar_repos(data):#find the most star repository
	starCount=[]
	for i in range(len(data)):
		starCount.append(data[i].get("stargazers_count"))

	mostStarPosition=starCount.index(max(starCount))
	return data[mostStarPosition]

def writeToCSV(repos):#write to csv
	f = csv.writer(open("mostStarRepos.csv", "wb+"))
	write_header = True
	item_keys    = []
	item_values = []

	 	
	for i in range(len(repos.keys())):
	 	if write_header:
	 		item_keys.append(repos.keys()[i])
	 		value=repos.get(repos.keys()[i])
	 		item_values.append(value)


	if write_header:
		#print item_values
	 	f.writerow(item_keys)
	 	#print item_values
	f.writerow(item_values)




def listContributors(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/contributors?per_page=100&page=%d" %(repos,j)
		repo_contributors = requests.get(file_name)
		#print repo_contributors#if success(200)
		raw_data=json.loads(repo_contributors.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	#print len(data)#print the number of repository
	return data


def writeContributorsToCSV(contributors):#write to csv
	f = csv.writer(open("mostStarReposContributors.csv", "wb+"))
	#write_header = True
	item_keys    = []
	item_values = []

	for i in range (len(contributors)):	
		singleContributor=contributors[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for j in range(len(singleContributor.keys())):

		 	if write_header:
		 		item_keys.append(singleContributor.keys()[j])
		 	value=singleContributor.get(singleContributor.keys()[j])
		 	item_values.append(value)

		

		if write_header:
			#print item_values
		 	f.writerow(item_keys)
		 	#print item_values
		f.writerow(item_values)


# def listTeams(user_name,repos):
# 	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
# 	#data=json.loads(request.text)
# 	#len(data)	

# 	data=[]

# 	page_n=100
# 	j=1

# 	while page_n == 100:
		
# 		file_name="http://api.github.com/repos/"+user_name+"%s/teams?per_page=100&page=%d" %(repos,j)
# 		repo_teams = requests.get(file_name)
# 		#print repo_contributors#if success(200)
# 		raw_data=json.loads(repo_teams.text)
# 		page_n=len(raw_data)
# 		for k in range(page_n):
# 			data.append(raw_data[k])

# 		j = j+1


# 	#print len(data)#print the number of repository
# 	return data


# def writeTeamsToCSV(teams):#write to csv
# 	f = csv.writer(open("mostStarReposTeams.csv", "wb+"))
# 	#write_header = True
# 	item_keys    = []
# 	item_values = []

# 	for i in range (len(teams)):	
# 		singleTeam=teams[i]
# 		if i == 0:
# 			write_header = True
# 		else: write_header = False

# 		item_values = []

# 		for j in range(len(singleTeam.keys())):

# 		 	if write_header:
# 		 		item_keys.append(singleTeam.keys()[j])
# 		 	value=singleTeam.get(singleTeam.keys()[j])
# 		 	item_values.append(value)


		

def listTags(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/tags?per_page=100&page=%d" %(repos,j)
		repo_tags = requests.get(file_name)
		#print repo_contributors#if success(200)
		raw_data=json.loads(repo_tags.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data


def writeTagsToCSV(tags):#write to csv
	f = csv.writer(open("mostStarReposTags.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(tags)):	
		singleTag=tags[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleTag.iteritems():
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

def listBranches(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/branches?per_page=100&page=%d" %(repos,j)
		repo_branch = requests.get(file_name)
		print repo_branch#if success(200)
		raw_data=json.loads(repo_branch.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data


def writeBranchesToCSV(branches):#write to csv
	f = csv.writer(open("mostStarReposBranches.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(branches)):	
		singleBranch=branches[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleBranch.iteritems():
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



def listPulls(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/pulls?per_page=100&page=%d" %(repos,j)
		repo_pulls = requests.get(file_name)
		#print repo_contributors#if success(200)
		raw_data=json.loads(repo_pulls.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writePullsToCSV(pulls):#write to csv
	f = csv.writer(open("mostStarReposPulls.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(pulls)):	
		singlePull=pulls[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singlePull.iteritems():
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




def listComments(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/comments?per_page=100&page=%d" %(repos,j)
		repo_comments = requests.get(file_name)
		#print repo_contributors#if success(200)
		#print repo_comments
		raw_data=json.loads(repo_comments.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeCommentsToCSV(comments):#write to csv
	f = csv.writer(open("mostStarReposComments.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(comments)):	
		singleComment=comments[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleComment.iteritems():
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

def listCommits(user_name,repos):
	#request = requests.get("https://api.github.com/repos/twitter/typeahead.js/contributors?per_page=100")
	#data=json.loads(request.text)
	#len(data)	

	data=[]

	page_n=100
	j=1

	while page_n == 100:
		
		file_name="http://api.github.com/repos/"+user_name+"%s/commits?per_page=100&page=%d" %(repos,j)
		repo_commits = requests.get(file_name)
		#print repo_commits
		raw_data=json.loads(repo_commits.text)
		page_n=len(raw_data)
		for k in range(page_n):
			data.append(raw_data[k])

		j = j+1


	return data

def writeCommitsToCSV(commits):#write to csv
	f = csv.writer(open("mostStarReposCommits.csv", "wb+"))
	item_keys    = []
	item_values = []

	for i in range (len(commits)):	
		singleCommit=commits[i]
		if i == 0:
			write_header = True
		else: write_header = False

		item_values = []

		for k , v in singleCommit.iteritems():
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

def listContents(user_name,repos):

	file_name="http://api.github.com/repos/"+user_name+"%s/readme?per_page=100" % repos
	repo_contents = requests.get(file_name)
	repo_contents
	#print "contents is %s" % repo_contents
	raw_data=json.loads(repo_contents.text)

	return raw_data


def writeContentsToCSV(contents):#write to csv
	f = csv.writer(open("mostStarReposContents.csv", "wb+"))
	item_keys    = []
	item_values = []


	write_header=True

	for k , v in contents.iteritems():

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


def main():
	reload(sys)
	sys.setdefaultencoding("utf-8")
	user_name='twitter/'
	data=Get_data(user_name)
	
	mostStarRepos=mostStar_repos(data)
	print(mostStarRepos.get("name"))#print the most star repository name
	print "mostStarRepos atrribute number is %d" % len(mostStarRepos)#69

	contributors=listContributors(user_name,mostStarRepos.get("name"))#list contributors
	print "contributors number is %d" % len(contributors)#71
	print "one contributor has atrribute number is %d" % len(contributors[1])#18

	tags = listTags(user_name, mostStarRepos.get("name"))
	print "tags number is %d" % len(tags)#15
	print "one tag has atrribute number is %d" % len(tags[1])#4

	pulls = listPulls(user_name, mostStarRepos.get("name"))
	print "pulls number is %d" % len(pulls)#84 
	print "one pull has atrribute number is %d" % len(pulls[1])#28


	branches = listBranches(user_name, mostStarRepos.get("name"))
	print "branches number is %d" % len(branches)#3 
	print "one branches has atrribute number is %d" % len(branches[1])#2

	comments = listComments(user_name, mostStarRepos.get("name"))
	print "comments number is %d" % len(comments)#33 
	print "one comments has atrribute number is %d" % len(comments[1])#11

	commits = listCommits(user_name, mostStarRepos.get("name"))
	print "commits number is %d" % len(commits)#594 
	print "one commits has atrribute number is %d" % len(commits[1])#8

	contents = listContents(user_name, mostStarRepos.get("name"))
	print "contents number is %d" % len(contents)#12 
	#print "one contents has atrribute number is %d" % len(contents[1])#8

	writeToCSV(mostStarRepos)
	writeContributorsToCSV(contributors)
	writeTagsToCSV(tags)
	writePullsToCSV(pulls)
	writeBranchesToCSV(branches)
	writeCommentsToCSV(comments)
	writeCommitsToCSV(commits)
	writeContentsToCSV(contents)


if __name__=="__main__":
	main()	


######collaborator not Authenticate

