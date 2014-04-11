# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileMoreAccess

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

from zope.schema.interfaces import IVocabularyFactory
from zope.component import queryUtility

TileMoreAccess_schema = BaseTile.schema.copy() + Schema((

    StringField(
        name='object_type',
        widget=SelectionWidget(
            label=_(u"Tipo de conteudo"),
            description=_(u"Selecione o tipo de itens que sera apresentado no mais acessados."),
            format = 'select',
        ),
        vocabulary=u'voc_ContentTypes',
        required=True,
    ),

    StringField(
        name='object_type_more',
        widget=SelectionWidget(
            label=_(u"Listagem de mais"),
            description=_(u"Selecione o tipo do item que sera apresentado no link mais."),
            format = 'select',
        ),
        vocabulary=u'voc_ContentTypes',
        required=True,
    ),

    TextField(
            name='path_link',
            widget=StringWidget(
                label=_(u"Caminho adicional"),
                description=_(u"Adicione o caminho que sera adicionao ao objeto listada acima."),
                label_msgid='vindula_tile_label_path_link',
                description_msgid='vindula_tile_help_path_link',
            ),
            default = u'/',
            required=True,
    ),

    IntegerField(
        name='numb_items',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        default=5,
    ),

    StringField(
        name='kind',
        widget=SelectionWidget(
            label=_(u"Selecione o layout"),
            description=_(u"Selecione o layout desejado para esta areas."),
            label_msgid='vindula_tile_label_layout',
            description_msgid='vindula_tile_help_layout',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[("padrao",_(u"Tema Padrão")),
                    ("unidade", _(u"Unidade Mais Acessada")),
                    ("lista_ver", _(u"Listagem vertical")),
                    ("two_columns", _(u"Listagem de duas colunas"))
                   ],
        default='padrao',
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

))

finalizeATCTSchema(TileMoreAccess_schema, folderish=False)

class TileMoreAccess(BaseTile):
    """ Reserve Content for TileMoreAccess """
    security = ClassSecurityInfo()

    implements(ITileMoreAccess)
    portal_type = 'TileMoreAccess'
    _at_rename_after_creation = True
    schema = TileMoreAccess_schema

    def voc_ContentTypes(self):
        types = self.portal_types.listContentTypes()
        return types


    #Scripts js
    scripts_js = ['button-more.js','ajax_boll_batch.js']

registerType(TileMoreAccess, PROJECTNAME)
