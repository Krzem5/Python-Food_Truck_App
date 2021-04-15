import server
import utils
import os



BASE_PATH="web/"
MIME_TYPES={"png":"image/png","otf":"font/otf"}



def install():
	@server.route("GET",r"/")
	def index(url):
		server.set_code(200)
		server.set_header("Content-Type","text/html")
		server.set_header("Cache-Control","public,max-age=31536000,immutable")
		return utils.cache("web/index.html")
	@server.route("GET",r"/about")
	def about(url):
		server.set_code(200)
		server.set_header("Content-Type","text/html")
		server.set_header("Cache-Control","public,max-age=31536000,immutable")
		return utils.cache("web/about.html")
	@server.route("GET",r"/menu")
	def menu(url):
		server.set_code(200)
		server.set_header("Content-Type","text/html")
		server.set_header("Cache-Control","public,max-age=31536000,immutable")
		return utils.cache("web/menu.html")
	@server.route("GET",r"/contact")
	def contact(url):
		server.set_code(200)
		server.set_header("Content-Type","text/html")
		server.set_header("Cache-Control","public,max-age=31536000,immutable")
		return utils.cache("web/contact.html")
	@server.route("GET",r"/rsrc/.*")
	def rsrc(url):
		server.set_header("Content-Type",MIME_TYPES[url.split(".")[-1]])
		if (os.path.exists(BASE_PATH+url)):
			server.set_code(200)
			server.set_header("Cache-Control","public,max-age=31536000,immutable")
			return utils.cache(BASE_PATH+url)
		server.set_code(404)
		server.set_header("Content-Type","text/plain")
		return b"Not Found"
	@server.route("GET",None)
	def not_found(url):
		server.set_code(307)
		server.set_header("Location","https://foodtruck853.herokuapp.com/")
		return b""
