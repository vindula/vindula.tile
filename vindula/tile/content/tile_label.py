# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.interfaces import ITileLabel
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileLabel_schema = BaseTile.schema.copy() + Schema((


))

#Oculta o campo padrao 'description'
invisivel = {'view':'invisible','edit':'invisible',}
TileLabel_schema['description'].widget.visible = invisivel

finalizeATCTSchema(TileLabel_schema, folderish=False)

class TileLabel(BaseTile):
    """ Reserve Content for TileLabel"""
    security = ClassSecurityInfo()

    implements(ITileLabel)
    portal_type = 'TileLabel'
    _at_rename_after_creation = True
    schema = TileLabel_schema

    #tamanho do tile
    columns = 6


registerType(TileLabel, PROJECTNAME)