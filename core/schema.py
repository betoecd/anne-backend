import graphene
import users.schema
class Query(users.schema.Query, graphene.ObjectType):
    """
    Projects main Query class, this will inherit multiple queries.
    """
    pass
schema = graphene.Schema(query=Query)
