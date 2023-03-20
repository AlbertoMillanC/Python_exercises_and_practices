from flask import Flask
from flask_graphql import GraphQLView
from graphql_server import schema # Este es el esquema que definimos anteriormente

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()