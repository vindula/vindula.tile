# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile.content.interfaces import ITileBannerCompost
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileBannerCompost_schema = BaseTile.schema.copy() + Schema((


    ReferenceField('featured_news',
        multiValued=1,
        allowed_types=('VindulaNews', 'News Item'),
        label=_(u"Notícias"),
        relationship='featured_news',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Destaque Notícia"),
            description='Selecione as notícias.'),
            review_state = ('published','internal','external'),
        required=False,
    ),
                                                            
    ReferenceField('destaqueBanner',
        multiValued=1,
        allowed_types=('Banner'),
        label=_(u"Banner"),
        relationship='destaqueBanner',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Destaque Banner"),
            description='Selecione os Destaques Banners Principais.'),
            review_state = ('published','internal','external'),
        required=False,
    ),

    IntegerField(
        name='timeTransitionNews',
        widget=IntegerWidget(
            label=_(u"Velocidade da rotação das notícias"),
            description=_(u"Tempo em milissegundos que a notícia leva para rotacionar, \
                          insira apenas números inteiros."),

            label_msgid='vindula_tile_label_timeTransitionNews',
            description_msgid='vindula_tile_help_timeTransitionNews',
            i18n_domain='vindula_tile',
        ),
        default=8000,
        required=True,
    ),


    ReferenceField('banner',
        multiValued=1,
        allowed_types=('Banner'),
        label=_(u"Banner"),
        relationship='Banner',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Banners Laterais"),
            description='Selecione os Banners Laterais.'),
            review_state = ('published','internal','external'),
        required=True,
    ),

    ReferenceField('imageBackgroud',
        multiValued=0,
        allowed_types=('Image'),
        label=_(u"Image de Fundo"),
        relationship='imageBackgroud',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Image de Fundo"),
            description='Selecione a imagem de fundo do Bloco.'),
        required=False,
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
        vocabulary=[("destaque_noticia",_(u"Destaque Notícia")),
                    ("destaque_banner", _(u"Destaque Banner")),
                   ],
        default='destaque_noticia',
        required=True,
    ),

))





finalizeATCTSchema(TileBannerCompost_schema, folderish=False)

class TileBannerCompost(BaseTile):
    """ Reserve Content for TileBannerCompost"""
    security = ClassSecurityInfo()

    implements(ITileBannerCompost)
    portal_type = 'TileBannerCompost'
    _at_rename_after_creation = True
    schema = TileBannerCompost_schema

    #tamanho do tile
    columns = 12

registerType(TileBannerCompost, PROJECTNAME)