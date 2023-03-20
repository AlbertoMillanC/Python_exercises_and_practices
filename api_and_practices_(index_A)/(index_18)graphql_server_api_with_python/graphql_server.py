import graphene

class Query(graphene.ObjectType):
    letters = graphene.List(graphene.String)

    def resolve_letters(self, info):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

schema = graphene.Schema(query=Query)