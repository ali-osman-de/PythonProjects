
import requests


class Github:

    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = 'YOUR ACCESS TOKEN'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username) 
        return response.json()

    def getRepository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()


    def createRepository(self,name):
        response = requests.post(self.api_url+'/user/repos?access_token'+ self.token, json={
            "name" : name,
            "description" : "This is your first repository",
            "homepage" : "https://YOUR ADDRESS.com",
            "private" : False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki" : True
        })
        return response.json()
        

github = Github()


while True:
    choose = input("""
                    1- Find User
                    2- Get Repositories
                    3- Create Repository
                    4- Exit
                    Your Choose: 
                    """)    

    if choose == '4':
        break
    else:
        if choose == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"""
                    Name: {result['name']}
                    Public repos: {result['public_repos']}
                    Followers: {result['followers']}
                    """)

        elif choose == '2':
            username = input('username: ')
            result = github.getRepository(username)
            i = 1
            for repo in result:
                print(f"{i} - {repo['name']}")
                i += 1

        elif choose == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("Something went wrong")