import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from .models import Pdv as PdvModel


class Pdv(MongoengineObjectType):
    class Meta:
        model = PdvModel
        interfaces = (Node,)


class CreatePdv(graphene.relay.ClientIDMutation):
    pdv = graphene.Field(Pdv)

    class Input:
        trading_name = graphene.String(required=True)
        owner_name = graphene.String(required=True)
        document = graphene.String(required=True)

    def mutate_and_get_payload(self, info, **kwargs):

        new_pdv = PdvModel(**kwargs)
        new_pdv.save()

        return CreatePdv(pdv=new_pdv)


class RelayMutation(graphene.AbstractType, graphene.ObjectType):
    create_pdv = CreatePdv.Field()


class Query(graphene.ObjectType):
    node = Node.Field()
    all_pdvs = MongoengineConnectionField(Pdv)


schema = graphene.Schema(query=Query, mutation=RelayMutation, types=[Pdv])
