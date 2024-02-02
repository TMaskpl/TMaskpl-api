from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from models import Item

# 1. Each object becomes a "node"
class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node, )

class Query(ObjectType):
    item = relay.Node.Field(ItemNode)
    items = DjangoFilterConnectionField(ItemNode)