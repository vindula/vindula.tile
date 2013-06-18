# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileNewEmployee

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileNewEmployee_schema = BaseTile.schema.copy() + Schema((

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
                   ],
        default='padrao',
        required=True,
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

finalizeATCTSchema(TileNewEmployee_schema, folderish=False)

class TileNewEmployee(BaseTile):
    """ Reserve Content for TileMoreAccess """
    security = ClassSecurityInfo()

    implements(ITileNewEmployee)
    portal_type = 'TileNewEmployee'
    _at_rename_after_creation = True
    schema = TileNewEmployee_schema



registerType(TileNewEmployee, PROJECTNAME)
