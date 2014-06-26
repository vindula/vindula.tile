# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileInfoStructure

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileInfoStructure_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('structure',
        multiValued=0,
        allowed_types=('OrganizationalStructure',),
        relationship='context_structure',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Escolha uma Unidade Organizacional"),
            description=_(u"Selecione uma Unidade Organizacional que deseja listar as informações."),
        ),
        required=False,
    ),

))

finalizeATCTSchema(TileInfoStructure_schema, folderish=False)

class TileInfoStructure(BaseTile):
    """ Reserve TileInfoStructure"""
    security = ClassSecurityInfo()

    implements(ITileInfoStructure)
    meta_type = portal_type = archetype_name = 'TileInfoStructure'
    _at_rename_after_creation = True
    schema = TileInfoStructure_schema

    #tamanho do tile
    columns = 12

    #Scripts js
    scripts_js = ['/++resource++vindula.myvindula.views/js/follow-cycle.js']


registerType(TileInfoStructure, PROJECTNAME)
