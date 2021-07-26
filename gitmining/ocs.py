from github import Github
import operator
from operator import itemgetter
from collections import OrderedDict
from itertools import islice
import itertools
def get_git_data(org, repo_ctr, comm_ctr):
    g = Github("c4f2a0ec3e123d531cdf70a52e0c9a711fdad344")
    repositories = g.search_repositories(query='org:' + org)

    # n=int(input("how many popular repositories do u want to see"))
    # m=int(input("enter the number of committers u want to see"))
    # name=input("please enter the name of the organization")
    lst_forks = []
    lst_names = []
    lst_name = []
    d = {}
    for repo in repositories:
        lst_forks.append(repo.forks)
        lst_names.append(repo.name)
    print("repo count=", len(lst_names))
    d = dict(zip(lst_names, lst_forks))
    # print(d)
    sorted_x = sorted(d.items(), key=lambda kv: kv[1])

    # print(sorted_x)
    for i in range(len(sorted_x) - 1, len(sorted_x) - int(repo_ctr) - 1, -1):
        # print(sorted_x[i][0],sorted_x[i][1])
        continue

    # repo_com = g.get_repo("Isha-jain-123/test")
    lst = []

    repo_dict = {}
    for i in range(len(sorted_x) - 1, len(sorted_x) - int(repo_ctr) - 1, -1):

        committers = {}

        repo_name = sorted_x[i][0]

        t = g.get_repo(org + "/" + sorted_x[i][0]).get_commits()
        # print(g.get_repo("MartinHeinz/" + sorted_x[i][0]).name)
        print("total commits=", t.totalCount)
        for j in range(t.totalCount):
            if t[j].committer is None:
                continue
            else:
                # print(t[j].committer.login)
                value = t[j].committer.login
                if value in committers:
                    committers[value] += 1
                else:
                    committers[value] = 1
        # print(committers)
        sorted_dict = {}
        sorted_dict = dict(sorted(committers.items(), key=operator.itemgetter(1)))
        res = OrderedDict(reversed(list(sorted_dict.items())))
        n_items = dict(itertools.islice(res.items(),0,int(comm_ctr)))
        repo_dict[repo_name] = n_items




    # lst.append(committers)

    return repo_dict


'''
g.get_repo("MartinHeinz/"+sorted_x[i][0]).get_commits()
g.get_repo("MartinHeinz/"+sorted_x[i][0]).get_commits()[j].committer.login

committers = {}
for i in range(len(sorted_x)-1,len(sorted_x)-n-1,-1):
	value = g.get_repo("freeCodeCamp/"+sorted_x[i][0]).get_commits()[0].committer.login
	if value in committers:
		committers[value] += 1
	else:
		committers[value] = 1

print(committers)

'''

# for repo in repositories:
# print(repo.get_commits().totalCount)
# print(repo.get_commits()[0].committer.login)
