# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileListServices

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileListServices_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('servicesFolder',
        multiValued=0,
        allowed_types=('ServicosFolder',),
        relationship='context_structure',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Selecione a pasta de serviços"),
            description=_(u"Selecione a pasta se serviços que será listada no bloco."),
        ),
        required=True,
    ),

))

finalizeATCTSchema(TileListServices_schema, folderish=False)

class TileListServices(BaseTile):
    """ Reserve TileListServices"""
    security = ClassSecurityInfo()

    implements(ITileListServices)
    meta_type = portal_type = archetype_name = 'TileListServices'
    _at_rename_after_creation = True
    schema = TileListServices_schema

    #tamanho do tile
    columns = 12

    #Scripts js
#    scripts_js = ['++resource++vindula.myvindula.views/js/follow-cycle.js']


registerType(TileListServices, PROJECTNAME)
