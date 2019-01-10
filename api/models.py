from mongoengine import Document, StringField


class Pdv(Document):
    trading_name = StringField(max_length=200, required=True)
    owner_name = StringField(max_length=100, required=True)
    document = StringField(max_length=15, required=True, unique=True)


# {
#         "id": 1,
#         "tradingName": "Adega da Cerveja - Pinheiros",
#         "ownerName": "Zé da Silva",
#         "document": "1432132123891/0001", //CNPJ
#         "coverageArea": {
#           "type": "MultiPolygon",
#           "coordinates": [
#             [[[30, 20], [45, 40], [10, 40], [30, 20]]],
#             [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
#           ]
#         }, //Área de Cobertura
#         "address": {
#           "type": "Point",
#           "coordinates": [-46.57421, -21.785741]
#         }, // Localização do PDV
#     }
