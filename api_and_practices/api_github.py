# aleatory name for the file in github
# import the module
import pandas as pd
import requests
# define the url
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# make the request and store the response
r = requests.get(url)
# print the status code
print("Status code:", r.status_code)
# store the API response in a variable
response_dict = r.json()
# process the results
print(response_dict.keys())
# print the total number of repositories
print("Total repositories:", response_dict['total_count'])
# explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
# examine the first repository
repo_dict = repo_dicts[0]
print("Keys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print("Selected information about first repository:")
print("Name:", repo_dict['name'])
print("Owner:", repo_dict['owner']['login'])
print("Stars:", repo_dict['stargazers_count'])
print("Repository:", repo_dict['html_url'])
print("Created:", repo_dict['created_at'])
print("Updated:", repo_dict['updated_at'])
print("Description:", repo_dict['description'])
# print the number of repositories
print("Number of repositories:", len(repo_dicts))
print("Selected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])
# print the number of repositories
print("Number of repositories:", len(repo_dicts))


