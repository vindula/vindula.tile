# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.CMFCore.utils import getToolByName
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileListagemHorizontal

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileListagemHorizontal_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('highlights',
            multiValued=1,
            allowed_types=('VindulaNews'),
            label=_(u"Destaques"),
            relationship='VindulaNews',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Destaques"),
                description='Selecione os destaques rotativos.'
            ),
            review_state = ('published', 'internal','external'),
            required=True,
    ),


    BooleanField(
        name='activeSocial',
        default=True,
        widget=BooleanWidget(
            label="Barra social destaque(s).",
            description='Caso selecionado, ativa a barra social no(s) destaque(s)',
            label_msgid='vindula_tile_label_activeSocial',
            description_msgid='vindula_tile_help_activeSocial',
        ),
    ),

    StringField(
        name='listTemplates',
        widget=SelectionWidget(
            label=_(u"Lista de Templates"),
            description=_(u"Selecione qual template deseja utilizar."),
            label_msgid='vindula_tile_label_listTemplate',
            description_msgid='vindula_tile_help_listTemplate',
            i18n_domain='vindula_tile',
            format = 'select',
         ),
         vocabulary=[("destaque_unico",_(u"Listagem com um único Destaque")),
                    ("destaque_multipla", _(u"Listagem Múltipla")),
                    ('destaque_two_columns', _(u"Listagem de duas colunas")),
                    ('destaque_duplo', _(u"Listagem em duplas"))
                    ],
         default='destaque_unico',
         required=True,
     ),
     
    BooleanField(
        name='activeMoreButton',
        default=True,
        widget=BooleanWidget(
            label="Botão mais items.",
            description='Caso selecionado, ativa o botão de mais items na visão do bloco.',
            label_msgid='vindula_tile_label_activeMoreButton',
            description_msgid='vindula_tile_help_activeMoreButton',
        ),
    ),
    
    BooleanField(
        name='activeSubTitulo',
        default=False,
        widget=BooleanWidget(
            label="Editoriais",
            description='Caso selecionado, ativa o vição dos editorias das notícas ou pagínas.',
            label_msgid='vindula_tile_label_activeSubTitulo',
            description_msgid='vindula_tile_help_activeSubTitulo',
        ),
    ),


))

finalizeATCTSchema(TileListagemHorizontal_schema, folderish=False)

class TileListagemHorizontal(BaseTile):
    """ Reserve Content for TileListagemHorizontal"""
    security = ClassSecurityInfo()

    implements(ITileListagemHorizontal)
    portal_type = 'TileListagemHorizontal'
    _at_rename_after_creation = True
    schema = TileListagemHorizontal_schema

    #tamanho do tile
    columns = 12

    #Scripts js
    scripts_js = ['ajax_boll_batch.js']

registerType(TileListagemHorizontal, PROJECTNAME)
