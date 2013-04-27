# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import schemata, base
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget 

from vindula.tile.content.interfaces import ITileBanner
from vindula.tile.content.tile_shemaBase import BaseTile

from Products.Archetypes.atapi import *

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileBanner_schema = schemata.ATContentTypeSchema.copy() + Schema((

	ReferenceField('imageBanner',
	        multiValued=0,
	        allowed_types=('Banner'),
	        label=_(u"Banner"),
	        relationship='Banner',
	        widget=VindulaReferenceSelectionWidget(
	            label=_(u"Banner "),
	            description='Selecione os banners.')),

	BooleanField(
        name='activeUnidade',
        default=True,
        widget=BooleanWidget(
            label="Ativar o texto da Unidade no Banner.",
            description='Caso selecionado, ativa o texto para visualização no Banner',
        ),
    ),

    BooleanField(
        name='activeData',
        default=True,
        widget=BooleanWidget(
            label="Ativar a Data no Banner.",
            description='Caso selecionado, ativa o data para visualização no Banner',
        ),
    ),

    BooleanField(
        name='activeAutor',
        default=True,
        widget=BooleanWidget(
            label="Ativar o Autor no Banner.",
            description='Caso selecionado, ativa o nome do autor para visualização no Banner',
        ),
    ),

    TextField(
            name='text_banner',
            widget=StringWidget(
                label=_(u"Texto para o Banner"),
                description=_(u"Texto adicionado na parte inferior do Banner."),
            ),
        required=False,
    ),

))


finalizeATCTSchema(TileBanner_schema, folderish=False)

class TileBanner(base.ATCTContent):
    """ Reserve Content for TileBanner"""
    security = ClassSecurityInfo()

    implements(ITileBanner)
    portal_type = 'TileBanner'
    _at_rename_after_creation = True
    schema = TileBanner_schema

    def get_tile_banners(self):
        pass


registerType(TileBanner, PROJECTNAME)