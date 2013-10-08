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

    TextField(
            name='text',
            default_content_type = 'text/html',
            default_output_type = 'text/x-html-safe',
            searchable = True,
            widget=RichWidget(
                label=_(u"Conteúdo"),
                description=_(u"Campo de preenchimento livre, seu conteúdo ficará posicionado abaixo da linha do titulo."),
                rows=10,
                label_msgid='vindula_themedefault_label_text',
                description_msgid='vindula_themedefault_help_text',
                i18n_domain='vindula_themedefault',
            ),
            required=False,
    ),

    BooleanField(
        name='line',
        default=True,
        widget=BooleanWidget(
            label="Mostrar linha abaixo o título",
            description='Caso selecionado mostrará uma linha abaixo o título.',
        ),
    ),

    IntegerField(
        name='columns',
        widget=SelectionWidget(
            label=_(u"Tamanho do tile"),
            description=_(u"Selecione o tamanho do tile."),
            label_msgid='vindula_tile_label_columns',
            description_msgid='vindula_tile_help_columns',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[('6',_(u"6 Colunas")),
                    ('12', _(u"12 Colunas")),
                    ],
        default=12,
        required=True,
    ),


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
    columns = 12


registerType(TileLabel, PROJECTNAME)