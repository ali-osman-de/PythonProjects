
import requests


class Github:

    def __init__(self):
        self.api_url = 'https://api.github.com'


    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username) 
        return response.json()

    def getRepository(self,username):
        response = requests.get(self.api_url+'/users/'+username+'repos')
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
Followers: {result['followers']}""")

        elif choose == '2':
            username = input('username: ')
            result = github.getRepository(username)
            for repo in result:
                print(repo['name'])

        elif choose == '3':
            pass
        else:
            print("Something went wrong")