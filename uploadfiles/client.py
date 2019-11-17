
import requests

# SERVER_URL = 'http://127.0.0.1:8001/home'
def sendmsg(url):
	# files = {'upload_file': open('hi.txt','rb')}
	# files = {'upload_file': open('timg1.bmp','rb')}
	# files = {'upload_file': open('Excel.xlsx','rb')}
	path = 'hi.txt'

	with open (path,'rb') as f:
		text = f.read()
		f.close()

	# files = {'upload_file': ('foobar.txt', open('file.txt','rb'), 'text/x-spam')}
	files = {'upload_file': ('hi.txt',text)}
	# files = {'upload_file': text}
	# values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}

	r = requests.post(url, files=files)
	print(r)


if __name__ == '__main__':
	url = 'http://127.0.0.1:8001/upload'
	sendmsg(url)