# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile.content.interfaces import ITileBanner
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *


from Products.CMFCore.permissions import setDefaultRoles
EditGobalBanner = 'Edit Global Banner'
setDefaultRoles(EditGobalBanner, ('Manager', 'Site Administrator'))


TileBanner_schema = BaseTile.schema.copy() + Schema((

	ReferenceField('imageBanner',
	        multiValued=1,
	        allowed_types=('Banner'),
	        label=_(u"Banner"),
	        relationship='Banner',
	        widget=VindulaReferenceSelectionWidget(
	            label=_(u"Banners"),
	            description='Selecione os banners.'),
                review_state = ('published','internal','external'),
            required=True,
    ),

    ReferenceField('imageBanner_admin',
            multiValued=1,
            allowed_types=('Banner'),
            label=_(u"Banner"),
            relationship='Banner_admin',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Banners - Global"),
                description='Selecione os banners globais.'),
                review_state = ('published','internal','external'),
            required=False,
            write_permission=EditGobalBanner,
    ),



    IntegerField(
        name='timeTransitionBanner',
        widget=IntegerWidget(
            label=_(u"Velocidade da rotação do banner"),
            description=_(u"Tempo em milissegundos que a imagem do banner leva para rotacionar, \
                          insira apenas números inteiros."),

            label_msgid='vindula_tile_label_timeTransitionBanner',
            description_msgid='vindula_tile_help_timeTransitionBanner',
            i18n_domain='vindula_tile',
        ),
        default=8000,
        required=True,
    ),

	StringField(
        name='typeNavigation',
        widget=SelectionWidget(
            label=_(u"Tipo da paginação dos banners"),
            description=_(u"Selecione o tipo de navegação dos banners rotativos."),
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
        name='activeUnit',
        default=True,
        widget=BooleanWidget(
            label="Ativar o texto da Unidade no Banner.",
            description='Caso selecionado, ativa o texto para visualização no Banner',
            label_msgid='vindula_tile_label_activeUnit',
            description_msgid='vindula_tile_help_activeUnit',
        ),
    ),

    BooleanField(
        name='activeDate',
        default=True,
        widget=BooleanWidget(
            label="Ativar a Data no Banner.",
            description='Caso selecionado, ativa o data para visualização no Banner',
            label_msgid='vindula_tile_label_activeDate',
            description_msgid='vindula_tile_help_activeDate',
        ),
    ),

    BooleanField(
        name='activeAuthor',
        default=True,
        widget=BooleanWidget(
            label="Ativar o Autor no Banner.",
            description='Caso selecionado, ativa o nome do autor para visualização no Banner',
            label_msgid='vindula_tile_label_activeAuthor',
            description_msgid='vindula_tile_help_activeAuthor',
        ),
    ),

))


finalizeATCTSchema(TileBanner_schema, folderish=False)


# invisivel = {'view':'visible','edit':'visible',}
# TileBanner_schema['effectiveDate'].widget.visible = invisivel
# TileBanner_schema['expirationDate'].widget.visible = invisivel


class TileBanner(BaseTile):
    """ Reserve Content for TileBanner"""
    security = ClassSecurityInfo()

    implements(ITileBanner)
    portal_type = 'TileBanner'
    _at_rename_after_creation = True
    schema = TileBanner_schema

    #tamanho do tile
    columns = 12

registerType(TileBanner, PROJECTNAME)