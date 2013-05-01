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

    IntegerField(
        name='numb_items',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        default=5,
    ),

    StringField(
        name='layout',
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
                    ("lista_ver", _(u"Listagem vertical"))
                   ],
        default='padrao',
        required=True,
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

registerType(TileMoreAccess, PROJECTNAME)
