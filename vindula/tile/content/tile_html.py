# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.content import schemata, base

from Products.CMFCore.utils import getToolByName
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileHtml

from vindula.tile import MessageFactory as _
from vindula.tile.config import *


TileHtml_schema = BaseTile.schema.copy() + Schema((

    TextField(
        name='html',
        default_output_type='text/html',
        widget=TextAreaWidget(
            label="Texto Html",
            description="Informe o html a ser renderizado.",
            rows="10",
        ),
        required=True,
    ),
))

finalizeATCTSchema(TileHtml_schema, folderish=False)

class TileHtml(BaseTile):
    """ Reserve Content for TileHtml"""
    security = ClassSecurityInfo()

    implements(ITileHtml)
    portal_type = 'TileHtml'
    _at_rename_after_creation = True
    schema = TileHtml_schema

    def voc_list_workflow(self):
        #TODO: Implementar método que retorna todos os workflows
        return ['published','internal','external']

    #tamanho do tile
    columns = 6

registerType(TileHtml, PROJECTNAME)
