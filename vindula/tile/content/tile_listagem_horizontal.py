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

BLACK_LIST_PLONETYPES = ['ATBooleanCriterion', 'ATCurrentAuthorCriterion', 'ATDateCriteria', 'ATDateRangeCriterion',
                         'ATListCriterion', 'ATPathCriterion', 'ATPortalTypeCriterion', 'ATReferenceCriterion', 'ATRelativePathCriterion',
                         'ATSelectionCriterion', 'ATSimpleIntCriterion', 'ATSimpleStringCriterion', 'ATSortCriterion', 'Banner', 'BannerFlash',
                         'BlockReserve', 'Classified', 'Classifieds', 'ClassifiedsCategory', 'ContainerTopicsControlPanel', 'ContentRedirectUser', 
                         'ContentReserve', 'Discussion Item', 'Download', 'DownloadContainer','FieldSetMyvindula', 'FieldsetEnd',
                         'FieldsetFolder', 'FieldsetStart', 'FileAttachment', 'FooterTopic', 'FormBooleanField', 'FormCaptchaField',
                         'FormCustomScriptAdapter', 'FormDateField', 'FormFileField', 'FormFixedPointField', 'FormFolder', 'FormIntegerField',
                         'FormLabelField', 'FormLikertField', 'FormLinesField', 'FormMailerAdapter', 'FormMultiSelectionField', 'FormPasswordField',
                         'FormRichLabelField', 'FormRichTextField', 'FormSaveDataAdapter', 'FormSelectionField', 'FormStringField', 'FormTextField',
                         'FormThanksPage', 'ImageAttachment', 'Layout', 'LayoutLoad', 'Menu', 'ObjectsControlPanel', 'OrderedClassifieds',
                         'OrderedClassifiedsCategory', 'PlanosPrecos', 'PlanosPrecosContainer', 'Plone Site', 'PlonePopoll', 'Ploneboard',
                         'PloneboardComment', 'PloneboardConversation', 'PloneboardForum', 'PoiIssue', 'PoiPscTracker', 'PoiTracker', 
                         'RedirectUser', 'ServicosFolder', 'SocialNetwork', 'SubtopicControlPanel', 'TempFolder', 
                         'ThemeConfig', 'ThemeLoginConfig', 'TileAccordionContent', 'TileAccordionItem', 'TileBanner', 'TileBannerCompost', 
                         'TileBirthdays', 'TileCalendar', 'TileFeatured', 'TileFood', 'TileHowDo', 'TileInfoStructure', 'TileLabel', 
                         'TileListagemHorizontal', 'TileListagemVertical', 'TileMacroList', 'TileMoreAccess', 'TileNewEmployee', 'TileOrganogram', 
                         'TilePoll', 'TileReferenceList', 'TileSimpleMacro', 'TileTabularList', 'TileTeam', 'Topic', 'TopicControlPanel', 'Unit', 
                         'VindulaCategories', 'VindulaFile', 'VindulaPortlet', 'VindulaRevista', 'VindulaTeam',
                         'vindula.content.content.vindulacontentapi', 'vindula.content.content.vindulacontentmacro', 'vindula.contentcore.conteudobasico', 
                         'vindula.contentcore.formulariobasico', 'vindula.controlpanel.content.alertdisplay', 
                         'vindula.controlpanel.content.aniversariantesconfig', 'vindula.controlpanel.content.categories',
                         'vindula.controlpanel.content.vindulaconfigall', 'vindula.food.restaurantes', 'vindula.liberiuncontents.content.featureprofile',
                         'vindula.liberiuncontents.content.features', 'vindula.liberiuncontents.content.featuresection', 
                         'vindula.liberiuncontents.content.featuretopic', 'vindula.myvindula.vindulalistdocumentuser',
                         'vindula.reservacorporativa.content.reserve']

TileListagemHorizontal_schema = BaseTile.schema.copy() + Schema((

    ReferenceField('highlights',
            multiValued=1,
            allowed_types=('VindulaNews'),
            label=_(u"Destaques"),
            relationship='VindulaNews',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Destaques"),
                description='Selecione os destaques rotativos.'
            ),
            review_state=('published', 'internal', 'external'),
            required=False,
    ),
                                                                 
    LinesField(
        name='listTypes',
        multiValued=1,
        widget=MultiSelectionWidget(
            label=_(u"Lista Tipos de Conteúdo"),
            description=_(u"Selecione o tipo de conteúdo que deseja buscar."),
            label_msgid='vindula_tile_label_listTypes',
            description_msgid='vindula_tile_help_listTypes',
            i18n_domain='vindula_tile',
            format = 'select',
         ),
         vocabulary='voc_list_types',
         required=False,
     ),

    ReferenceField('path',
        multiValued=0,
        allowed_types=('VindulaFolder','Folder', 'VindulaClipping'),
        label=_(u"Pasta"),
        relationship='path',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Pasta"),
            description='Selecione a pasta de onde os conteúdos deverão ser listados.'
        ),
        review_state = ('published', 'internal','external')
    ),

    StringField(
        name='listTemplates',
        widget=SelectionWidget(
            label=_(u"Lista de Templates"),
            description=_(u"Selecione qual template deseja utilizar."),
            label_msgid='vindula_tile_label_listTemplate',
            description_msgid='vindula_tile_help_listTemplate',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[("destaque_unico", _(u"Listagem com um único Destaque")),
                    ("destaque_multipla", _(u"Listagem Múltipla")),
                    ('destaque_two_columns', _(u"Listagem de duas colunas")),
                    ('destaque_duplo', _(u"Listagem em duplas"))
                    ],
        default='destaque_unico',
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
    
    BooleanField(
        name='activeSubTitulo',
        default=False,
        widget=BooleanWidget(
            label="Editoriais",
            description='Caso selecionado, ativa a visão dos editoriais das notícias ou páginas.',
            label_msgid='vindula_tile_label_activeSubTitulo',
            description_msgid='vindula_tile_help_activeSubTitulo',
        ),
    ),
                                                                 
    StringField(
        name='ordination',
        widget=SelectionWidget(
            label=_(u"Ordenação"),
            description=_(u"Selecione o tipo de ordenação dos itens listados."),
            label_msgid='vindula_tile_label_ordination',
            description_msgid='vindula_tile_help_ordination',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[("creation_date", _(u"Data de cadastro")),
                    ("title", _(u"Título")),],
        default='creation_date',
    ),
                                                                 
    StringField(
        name='order',
        widget=SelectionWidget(
            label=_(u"Ordem"),
            description=_(u"Selecione qual ordem os itens listados devem assumir."),
            label_msgid='vindula_tile_label_order',
            description_msgid='vindula_tile_help_order',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[("desc", _(u"Decrescente")),
                    ("asc", _(u"Crescente")),],
        default='desc',
    ),
                                                                 
    BooleanField(
        name='hideSeparator',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Ocultar separador",
            description='Selecione para ocultar a linha pontilhada que separa as notícias na listagem múltipla.',
            label_msgid='vindula_tile_label_hideSeparator',
            description_msgid='vindula_tile_help_hideSeparator',
        ),
    ),
                                                                 
    BooleanField(
        name='hideImage',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Ocultar imagem",
            description='Selecione para ocultar a imagem dos itens da listagem.',
            label_msgid='vindula_tile_label_hideImage',
            description_msgid='vindula_tile_help_hideImage',
		),
	),
                                                                 
	BooleanField(
        name='hideDescription',
        default=False,
        schemata='settings',
        widget=BooleanWidget(
            label="Ocultar descrição",
            description='Selecione para ocultar a descrição dos itens da listagem.',
            label_msgid='vindula_tile_label_hideDescription',
            description_msgid='vindula_tile_help_hideDescription',
        ),
	),
                                                                 
    IntegerField(
        name='heightImage',
        schemata='settings',
        widget=IntegerWidget(
            label=_(u"Altura da imagem"),
            description=_(u"Altura da imagem a ser mostrada, caso estiver em branco será usado a altura padrão."),
            label_msgid='vindula_tile_label_heightImage',
            description_msgid='vindula_tile_help_heightImage',
            i18n_domain='vindula_tile',
        ),
        required=False,
    ),
																
    IntegerField(
        name='widthImage',
        schemata='settings',
        widget=IntegerWidget(
            label=_(u"Largura da imagem"),
            description=_(u"Largura da imagem a ser mostrada, caso estiver em branco será usado a largura padrão"),
            label_msgid='vindula_tile_label_widthImage',
            description_msgid='vindula_tile_help_widthImage',
            i18n_domain='vindula_tile',
        ),
        required=False,
    ),
                                                                 
    BooleanField(
        name='hidePagination',
        default=False,
        schemata='settings',
        widget=BooleanWidget(
            label="Ocultar paginação",
            description='Selecione para ocultar a paginação do bloco na listagem múltipla.',
            label_msgid='vindula_tile_label_hidePagination',
            description_msgid='vindula_tile_help_hidePagination',
        ),
    ),
      
    IntegerField(
        name='qtyItemsPage',
        schemata='settings',
        widget=IntegerWidget(
            label=_(u"Quantidade de itens por página"),
            description=_(u"Insira a quantidade de itens por página na listagem múltipla."),
            label_msgid='vindula_tile_label_qtyItemsPage',
            description_msgid='vindula_tile_help_qtyItemsPage',
            i18n_domain='vindula_tile',
        ),
        default = 7,
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
    
    def voc_list_types(self):
        types = []
        for item in self.portal_types.listContentTypes():
            if not item in BLACK_LIST_PLONETYPES:
                types.append(item)
        return types

    # tamanho do tile
    columns = 12

    # Scripts js
    scripts_js = ['ajax_boll_batch.js']

registerType(TileListagemHorizontal, PROJECTNAME)
