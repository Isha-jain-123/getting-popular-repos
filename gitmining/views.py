from django.shortcuts import render
from django.http import HttpResponse
from gitmining.ocs import *
from json2html import *
import json


# Create your views here.
def index(request):
    org_name = request.GET['org_name']
    repo_count = request.GET['repo_count']
    committer_count = request.GET['comm_count']
    print ("org=",org_name,repo_count)
    data=get_git_data(org_name,repo_count,committer_count)
    jsonString = json.dumps(data)
    tbl=json2html.convert(json = jsonString)
#print ("data in json=",jsonString)

#return JsonResponse(jsonString, safe=False)
    #data=print_table(4)
    #print ("data from git=",data)
    return HttpResponse(tbl)







    
'''    
jsonString = json.dumps(data)
print ("data in json=",jsonString)
return JsonResponse(jsonString, safe=False)
'''