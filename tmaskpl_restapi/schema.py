from graphene import Schema, ObjectType
import base.schema

class Query(base.schema.Query, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(ObjectType):
    # This class will inherit from multiple Mutations
    # as we begin to add more apps to our project
    pass

schema = Schema(query=Query)