# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileOrganogram

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileOrganogram_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('estrutura_principal',
        multiValued=0,
        allowed_types=('OrganizationalStructure',),
        relationship='context_structure',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Escolha uma Unidade Organizacional Principal"),
            description=_(u"Selecione uma Unidade Organizacional principal para o organograma."),
        ),
    ),

))

finalizeATCTSchema(TileOrganogram_schema, folderish=False)

class TileOrganogram(BaseTile):
    """ Reserve TileOrganogram for TileFeatured """
    security = ClassSecurityInfo()

    implements(ITileOrganogram)
    portal_type = 'TileOrganogram'
    _at_rename_after_creation = True
    schema = TileOrganogram_schema

    #tamanho do tile
    columns = 12

    #Scripts js
    scripts_js = ['org-tree.js']


registerType(TileOrganogram, PROJECTNAME)
