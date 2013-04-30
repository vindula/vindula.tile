# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileListagemVertical

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileListagemVertical_schema = BaseTile.schema.copy() + Schema((

	TextField(
            name='tituloTileListagemVertical',
            widget=StringWidget(
                label=_(u"Título para o Tile Listagem Vertical"),
                description=_(u"Título para o Tile Listagem Vertical"),
                label_msgid='vindula_tile_label_title_titleTileListagemVertical',
                description_msgid='vindula_tile_help_titleTileListagemVertical',
                i18n_domain='vindula_tile',
            ),
        required=True,
    ),

# ******************** Schemata Informações ********************
	StringField(
        name='ativaOrdenacao',
        widget=SelectionWidget(
            label=_(u"Ativa o campo de ordenação"),
            description=_(u"Ativa a opção de ordenar os conteúdos"),
            label_msgid='vindula_tile_label_ativaOrdenacao',
            description_msgid='vindula_tile_help_ativaOrdenacao',
            i18n_domain='vindula_tile',
            format = 'choice'
        ),
        vocabulary = ['Imagem',
        			  'Título',
        			  'Local',
        			  'Data',
        			  'Site',
        			  'Rede Social',
        			  'Link',
        			  'Ícones'],
        schemata = 'Informações',
        required=False,
    ),

# ******************** Fim Schemata Informações ********************

))

finalizeATCTSchema(TileListagemVertical_schema, folderish=False)

class TileListagemVertical(BaseTile):
    """ Reserve Content for TileListagemVertical"""
    security = ClassSecurityInfo()

    implements(ITileListagemVertical)
    portal_type = 'TileListagemVertical'
    _at_rename_after_creation = True
    schema = TileListagemVertical_schema

    def get_info(self):
        pass


registerType(TileListagemVertical, PROJECTNAME)
