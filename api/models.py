from mongoengine import Document, StringField, PointField, MultiPolygonField


class Pdv(Document):
    trading_name = StringField(max_length=200, required=True)
    owner_name = StringField(max_length=100, required=True)
    document = StringField(max_length=20, required=True, unique=True)
    address = PointField(required=True)
    coverage_area = MultiPolygonField(required=True)
