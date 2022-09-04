import mongoengine as me

class Item(me.Document):

    name = me.StringField(unique=True)
    weight = me.DecimalField(precision=1)
    value = me.DecimalField(precision=1)
    quantity = me.IntField()

    def __str__(self):
        return f"Name={self.name}\nWeight={self.weight}\nValue={self.value}\nQuantity={self.quantity}\nUsed={self.qtd_used}"

    def to_json(self):
        return {
            "name": self.name,
            "weight": float(self.weight),
            "value": float(self.value),
            "quantity": self.quantity
        }
