import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from pdv.graphql.schema import custom_types
from pdv.models import Pdv as PdvModel


class Pdv(MongoengineObjectType):
    class Meta:
        model = PdvModel
        interfaces = (Node,)


class CreatePdv(graphene.relay.ClientIDMutation):
    pdv = graphene.Field(Pdv)

    class Input:
        trading_name = graphene.String(
            required=True, description="Name of trading store"
        )
        owner_name = graphene.String(required=True, description="Name of trading owner")
        document = custom_types.CNPJ(required=True, description="CNPJ of trading store")
        address = graphene.List(
            graphene.Float,
            required=True,
            description="Point coordinate in the form [lar, long]",
        )
        coverage_area = graphene.List(
            graphene.List(graphene.List(graphene.List(graphene.Float))),
            required=True,
            description="MultiPolygon format store coverage area",
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

    def resolve_all_pdvs(self, info, id=None, **kwargs):
        if id:
            return PdvModel.objects.filter(id=id)

        return PdvModel.objects.all()
