# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileSimpleMacro

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileSimpleMacro_schema = BaseTile.schema.copy() + Schema((

    TextField(
            name='page',
            widget=StringWidget(
                label=_(u"Página"),
                description=_(u"Utilizado para inserir o nome da pagina para visualização do conteudo."),
                label_msgid='vindula_tile_label_page',
                description_msgid='vindula_tile_help_page',
            ),
        required=True,
    ),

    TextField(
            name='macro',
            widget=StringWidget(
                label=_(u"Macro"),
                description=_(u"Utilizado para inserir a macro de visualização do conteudo."),
                label_msgid='vindula_tile_label_textoBanner',
                description_msgid='vindula_tile_help_textoBanner',
            ),
        default=u'page',
        required=True,
    ),

    IntegerField(
        name='columns',
        widget=SelectionWidget(
            label=_(u"Tamalho do tile"),
            description=_(u"Selecione o tamanho do tile."),
            label_msgid='vindula_tile_label_columns',
            description_msgid='vindula_tile_help_columns',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[('6',_(u"6 Colunas")),
                    ('12', _(u"12 Colunas")),
                    ],
        default=6,
        required=True,
    ),

))

finalizeATCTSchema(TileSimpleMacro_schema, folderish=False)

class TileSimpleMacro(BaseTile):
    """ Reserve Content for TileSimpleMacro """
    security = ClassSecurityInfo()

    implements(ITileSimpleMacro)
    portal_type = 'TileSimpleMacro'
    _at_rename_after_creation = True
    schema = TileSimpleMacro_schema

    #tamanho do tile
    columns = 12

registerType(TileSimpleMacro, PROJECTNAME)
