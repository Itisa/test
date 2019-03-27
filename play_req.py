#coding:utf-8
import requests,time

r = requests.get(url)

raw = r.text
csrf = 'csrfmiddlewaretoken'
ind = raw.find(csrf)
nextstr = raw[ind + len(csrf) + 1:]
nn = nextstr.find('\'')
nextstr = nextstr[nn+1:]
nn = nextstr.find('\'')
nextstr = nextstr[:nn]

print(nextstr,'\n')
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36','Referer':url}
post_data ={'csrfmiddlewaretoken' : nextstr,'form_username':name,'form_password':passwd,'next': '/ '}

print(post_data)
r1 = requests.post(url1,data = post_data,headers = header)
print(r1,'\n')
# print(r1.reason,'\n')
# print('url:',r1.url)
print('his',r1.history)
# print(r1.headers,'\n')
# print(r1.request.headers,'\n')
# print(r1.encoding,'\n''\n')
print(r1.text)

