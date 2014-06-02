# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileMultimedia

from vindula.tile import MessageFactory as _
from vindula.tile.config import *


TileMultimedia_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('multimedia',
        multiValued=0,
        allowed_types=('VindulaVideo', 'VindulaStreaming',),
        relationship='relationMultimedia',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Vídeo"),
            description='Selecione o vídeo que será será mostrado no bloco.'
        ),
        required=True,
    ),
                                                         
                                                         
    IntegerField(
        name='width_video',
        widget = IntegerWidget(
            label = 'Largura',
            description='Largura em pixels do vídeo.',
        ),
        default=640,
        required=True,
    ),
                                                         
    IntegerField(
        name='height_video',
        widget = IntegerWidget(
            label = 'Altura',
            description='Altura em pixels do vídeo.',
        ),
        default=390,
        required=True,
    ),
                                                         
    StringField(
        name='columns',
        widget=SelectionWidget(
            label=_(u"Tamanho do bloco"),
            description=_(u"Selecione o tamanho do bloco."),
            label_msgid='vindula_tile_label_columns',
            description_msgid='vindula_tile_help_columns',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[('6',_(u"6 Colunas")),
                    ('12', _(u"12 Colunas")),
                    ],
        default='6',
        required=True,
    ),

))

finalizeATCTSchema(TileMultimedia_schema, folderish=False)

class TileMultimedia(BaseTile):
    """ Reserve Content for TileMultimedia"""
    security = ClassSecurityInfo()

    implements(ITileMultimedia)
    portal_type = 'TileMultimedia'
    _at_rename_after_creation = True
    schema = TileMultimedia_schema
    
    #tamanho do tile
    columns = 12

    # Scripts js
#     scripts_js = ['flowplayer-3.1.2.min.js']

registerType(TileMultimedia, PROJECTNAME)
