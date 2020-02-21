from wsgiref.simple_server import make_server
from first import app
   	

# with make_server('',8800,app) as server:
# 	print(" serving on port 8800 ....\n Visit http://127.0.0.1:8800")

# 	server.serve_forever()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
