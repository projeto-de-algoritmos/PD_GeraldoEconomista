import mongoengine as me

class Item(me.Document):

    name = me.StringField(unique=True)
    weight = me.IntField()
    value = me.IntField()
    image_url = me.StringField()

    def __str__(self):
        return f"Name={self.name}\nWeight={self.weight}\nValue={self.value}\nQuantity={self.quantity}\nUsed={self.qtd_used}"

    def to_json(self):
        return {
            "name": self.name,
            "weight": int(self.weight),
            "value": int(self.value),
            "image_url": self.image_url
        }

    @staticmethod
    def get_item(name):
        item = Item.objects(name__exact=name).first()

        if item is None:
            return None, f"There are no items with the name {name}"

        return item, None
