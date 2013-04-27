# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import schemata, base
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget 

from vindula.tile.content.interfaces import ITileBanner
from vindula.tile.content.tile_schemaBase import BaseTile

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

	StringField(
        name='tipoPaginacao',
        widget=SelectionWidget(
            label=_(u"Tipo da paginação dos banners"),
            description=_(u"Selecione o tipo de paginação dos banners rotativos."),
            label_msgid='vindula_tile_label_tipoPaginacao',
            description_msgid='vindula_tile_help_tipoPaginacao',
            i18n_domain='vindula_tile',
            format='radio',
        ),
        vocabulary=[("number","Número"),("image","Imagem")],
        default="image",
        required=True,
    ),

	BooleanField(
        name='ativaUnidade',
        default=True,
        widget=BooleanWidget(
            label="Ativar o texto da Unidade no Banner.",
            description='Caso selecionado, ativa o texto para visualização no Banner',
            label_msgid='vindula_tile_label_ativaUnidade',
            description_msgid='vindula_tile_help_ativaUnidade',
        ),
    ),

    BooleanField(
        name='ativaData',
        default=True,
        widget=BooleanWidget(
            label="Ativar a Data no Banner.",
            description='Caso selecionado, ativa o data para visualização no Banner',
            label_msgid='vindula_tile_label_ativaData',
            description_msgid='vindula_tile_help_ativaData',
        ),
    ),

    BooleanField(
        name='ativaAutor',
        default=True,
        widget=BooleanWidget(
            label="Ativar o Autor no Banner.",
            description='Caso selecionado, ativa o nome do autor para visualização no Banner',
            label_msgid='vindula_tile_label_ativaAutor',
            description_msgid='vindula_tile_help_ativaAutor',
        ),
    ),

    TextField(
            name='textoBanner',
            widget=StringWidget(
                label=_(u"Texto para o Banner"),
                description=_(u"Texto adicionado na parte inferior do Banner."),
                label_msgid='vindula_tile_label_textoBanner',
            	description_msgid='vindula_tile_help_textoBanner',
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