import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from pdv.models import Pdv as PdvModel


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
        address = graphene.List(graphene.Float, required=True)
        coverage_area = graphene.List(
            graphene.List(graphene.List(graphene.List(graphene.Float))), required=True
        )

    def mutate_and_get_payload(self, info, **kwargs):

        new_pdv = PdvModel(**kwargs)
        new_pdv.save().reload()

        return CreatePdv(pdv=new_pdv)


class Mutation:
    create_pdv = CreatePdv.Field()


class Query:
    all_pdvs = MongoengineConnectionField(Pdv)
    nearest_pdv = MongoengineConnectionField(
        Pdv, coord=graphene.List(graphene.Float, required=True)
    )

    def resolve_nearest_pdv(self, info, coord):
        return PdvModel.objects.filter(coverage_area__near=coord)[:1]

    def resolve_all_pdvs(self, info, document=None):
        if document:
            return PdvModel.objects.filter(document=document)

        return PdvModel.objects.all()
