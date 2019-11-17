# coding: utf-8
import json

import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options

# define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", IndexHandler),
			(r"/upload", UploadHandler)
		]
		tornado.web.Application.__init__(self, handlers)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("upload_form.html")

class UploadHandler(tornado.web.RequestHandler):
	def post(self):
		# print('in')
		file1 = self.request.files
		# print(file1)
		file = file1['upload_file'][0]
		text = file['body']
		# print(text)
		print(type(text))
		
		path = os.getcwd()
		ifhavedir=os.path.exists(path+'/'+'upload')
		if not ifhavedir:
			os.makedirs(path+'/'+'upload')

		filename = self.check(file['filename'],path)

		with open('upload/'+filename,'wb') as f:
			# word = str(text, encoding = "utf8")
			# print(word)
			f.write(text)

			f.close()



		# original_fname = file1['filename']
		# extension = os.path.splitext(original_fname)[1]
		# fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
		# final_filename= fname+extension
		# output_file = open("uploads/" + final_filename, 'w')
		# output_file.write(file1['body'])
		# self.finish("file" + final_filename + " is uploaded")

	def check(self,filename,path,depth=0):
		# print(path,filename)
		iaa=os.path.exists(path+'/upload/'+filename)
		# print(iaa)
		if not iaa:
			return filename
		else:
			index = filename.find('.')
			if depth == 0:
				newfilename = filename[:index]+'('+'%s' % depth +').'+filename[index+1:]
			else:
				newfilename = filename[:index-3]+'('+'%s' % depth +').'+filename[index+1:]
			print(newfilename)
			return self.check(newfilename,path,depth+1)



def main():
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(8001)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()