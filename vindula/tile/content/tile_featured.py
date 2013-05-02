# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileFeatured

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileFeatured_schema = BaseTile.schema.copy() + Schema((


    ReferenceField('itens',
        multiValued=1,
        allowed_types=('VindulaNews', 'News Item'),
        label=_(u"Itens em Destaque"),
        relationship='itensFeatured',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Itens em Destaque"),
            description='Selecione os itens que serão destaque.'
        ),
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
        vocabulary=[("alerta_normal",_(u"Alerta Cinza Normal")),
                    ("alerta_importante", _(u"Alerta Amarelo Importante")),
                    ("destaque", _(u"Destaque de Noticia"))
                   ],
        default='destaque',
        required=True,
    ),


))

finalizeATCTSchema(TileFeatured_schema, folderish=False)

class TileFeatured(BaseTile):
    """ Reserve Content for TileFeatured """
    security = ClassSecurityInfo()

    implements(ITileFeatured)
    portal_type = 'TileFeatured'
    _at_rename_after_creation = True
    schema = TileFeatured_schema


registerType(TileFeatured, PROJECTNAME)
