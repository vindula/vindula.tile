# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileTeam

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileTeam_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('structure',
        multiValued=0,
        allowed_types=('OrganizationalStructure',),
        relationship='context_structure',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Escolha uma Unidade Organizacional"),
            description=_(u"Selecione uma Unidade Organizacional que você deseja listar a equipe."),
        ),
        required=False,
    ),

))

finalizeATCTSchema(TileTeam_schema, folderish=False)

class TileTeam(BaseTile):
    """ Reserve TileTeam for TileFeatured """
    security = ClassSecurityInfo()

    implements(ITileTeam)
    portal_type = 'TileTeam'
    _at_rename_after_creation = True
    schema = TileTeam_schema

    #tamanho do tile
    columns = 12

    #Scripts js
    #scripts_js = []


registerType(TileTeam, PROJECTNAME)
