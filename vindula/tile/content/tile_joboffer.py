# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileJobOffer

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileJobOffer_schema = BaseTile.schema.copy() + Schema((

    StringField(
        name='link_cadastro',
        widget=StringWidget(
            label=_(u"Link para Cadastro"),
            description=_(u"Adicione o link para o formulario de cadastro do usuário."),
        ),
        required=True,
    ),


))

finalizeATCTSchema(TileJobOffer_schema, folderish=False)

class TileJobOffer(BaseTile):
    """ Reserve TileInfoStructure"""
    security = ClassSecurityInfo()

    implements(ITileJobOffer)
    meta_type = portal_type = archetype_name = 'TileJobOffer'
    _at_rename_after_creation = True
    schema = TileJobOffer_schema

    #tamanho do tile
    columns = 12

    #Scripts js
#    scripts_js = ['++resource++vindula.myvindula.views/js/follow-cycle.js']


registerType(TileJobOffer, PROJECTNAME)
