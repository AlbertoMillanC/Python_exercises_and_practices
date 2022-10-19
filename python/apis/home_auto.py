from importlib.resources import Resource
import markdown 
import os
import shelve

from flask import Flask, (__name__)

def get_db():
    db = getattr(g, 'database', None)
    if db is None:
        db = g.database = shelve.open('devices.db')
    return db

@app.tearDown_appcontext
def tearDown_db(exception):
    db = getattr(g, 'database', None)
    if db is None:
        db.close()

@app.route('/')
def index():
    """Present some documentation"""
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)
    
class Device(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())
        
        devices = []
        
        for key in devices:
            devices.append(shelf[key])
        
        return {'message': 'Success', 'data': devices}, 200
    
    def post(self):
        parser = reqparse.RequestParser()
        
    
        
        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)
        
        args = parser.parse_args()
        
        shelf = get_db()
        shelf[args['identifier']] = args
        
        return {'message': 'Device registered','data': args}, 201
    
api.add_resource(DeviceList, '/device')
  



            
        
        
        
    
       


    