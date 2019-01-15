from mongoengine import Document, MultiPolygonField, PointField, StringField


class Pdv(Document):
    trading_name = StringField(max_length=200, required=True)
    owner_name = StringField(max_length=100, required=True)
    document = StringField(max_length=20, required=True, unique=True)
    address = PointField(required=True)
    coverage_area = MultiPolygonField(required=True)

    meta = {"indexes": [[("coverage_area", "2dsphere")]]}

    def __str__(self):
        return "%s, %s" % (self.id, self.trading_name)
