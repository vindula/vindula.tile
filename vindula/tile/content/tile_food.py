# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.interfaces import ITileFood
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileFood_schema = BaseTile.schema.copy() + Schema((

    IntegerField(
        name='numb_items',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        default=5,
    ),


))

finalizeATCTSchema(TileFood_schema, folderish=False)

class TileFood(BaseTile):
    """ Reserve Content for TileFood """
    security = ClassSecurityInfo()

    implements(ITileFood)
    portal_type = 'TileFood'
    _at_rename_after_creation = True
    schema = TileFood_schema

    #tamanho do tile
    columns = 6


registerType(TileFood, PROJECTNAME)