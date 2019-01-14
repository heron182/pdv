import graphene
from graphene.relay import Node

from .pdv import Query as PdvQuery, Mutation as PdvMutation, Pdv as PdvType


class Query(graphene.ObjectType, PdvQuery):
    node = Node.Field()


class Mutation(graphene.ObjectType, PdvMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, types=[PdvType])
