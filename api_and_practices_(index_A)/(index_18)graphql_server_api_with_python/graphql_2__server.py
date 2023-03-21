import graphene
from graphql.execution.base import GraphQLResolveInfo

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    goodbye = graphene.String()

    def resolve_hello(self, info, name):
        return f"Hello {name}!"

    def resolve_goodbye(self, info):
        return "Goodbye, cruel world!"

schema = graphene.Schema(query=Query)

if __name__ == "__main__":
    query_string = '{ hello }'
    result = schema.execute(query_string)
    print(result.data['hello'])
