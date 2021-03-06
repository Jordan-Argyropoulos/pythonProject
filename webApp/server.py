import cherrypy
import random
import string


class HelloWorld(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return "Hello World!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))


if __name__ == "__main__":
    cherrypy.quickstart(HelloWorld())
