from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html>
    <head>
        <title>My First HTML server in python </title>
    </head>
    <body>
        <h1>Hello World!. With python.</h1>
    </body>


</html>

"""

def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    
    start_response('200 OK', headers)
    
    return [bytes(HTML, 'utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()

