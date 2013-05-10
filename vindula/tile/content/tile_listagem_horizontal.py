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
                description='Selecione os destaques rotativos.'),
                review_state = ('published', 'internal','external'),
            required=True,
                ),


    StringField(
        name='typeNavigation',
        widget=SelectionWidget(
            label=_(u"Tipo da navegação do(s) destaque(s)"),
            description=_(u"Selecione o tipo de navegação para o(s) destaque(s)."),
            label_msgid='vindula_tile_label_typeNavigation',
            description_msgid='vindula_tile_help_typeNavigation',
            i18n_domain='vindula_tile',
            format='radio',
        ),
        vocabulary=[("number","Número"),("image","Imagem")],
        default="image",
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
                    ("destaque_multipla", _(u"Listagem Múltipla"))],
         default='destaque_unico',
         required=True,
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

registerType(TileListagemHorizontal, PROJECTNAME)
