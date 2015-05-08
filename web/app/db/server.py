from wsgiref.simple_server import make_server
from myWSGI import application

# create a seerver, port:8000
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# start listening to the request of server
httpd.serve_forever()
