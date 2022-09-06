import mongoengine as me

class Item(me.Document):

    name = me.StringField(unique=True)
    weight = me.IntField()
    value = me.DecimalField(precision=2)
    image_url = me.StringField()

    def to_json(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "value": float(self.value),
            "image_url": self.image_url
        }

    @staticmethod
    def get_by_name(name):
        item = Item.objects(name__exact=name).first()

        if item is None:
            return None, f"There are no items with the name {name}"

        return item, None

    def __str__(self):
        return f"Name={self.name}\nWeight={self.weight}\nValue={self.value}\nImageUrl={self.image_url}"
