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
                         'vindula.reservacorporativa.content.reserve', 'TileJobOffer', 'TileLibrary', 'TileListServices', 'TileLoadReference',
                         'TileMultimedia', 'TilePoiTracker']

TileMoreAccess_schema = BaseTile.schema.copy() + Schema((

    StringField(
        name='object_type',
        widget=MultiSelectionWidget(
            label=_(u"Tipo de conteúdo"),
            description=_(u"Selecione o tipo dos conteúdos que serão listados."),
            format = 'select',
        ),
        vocabulary=u'voc_ContentTypes',
        required=True,
    ),

    StringField(
        name='object_type_more',
        widget=MultiSelectionWidget(
            label=_(u"Listagem de mais"),
            description=_(u"Selecione o tipo dos conteúdos que serão listados no link mais."),
            format = 'select',
        ),
        vocabulary=u'voc_ContentTypes',
        required=True,
    ),

#     TextField(
#         name='path_link',
#         widget=StringWidget(
#             label=_(u"Caminho adicional"),
#             description=_(u"Adicione o caminho que será adicionado ao objeto listada acima."),
#             label_msgid='vindula_tile_label_path_link',
#             description_msgid='vindula_tile_help_path_link',
#         ),
#         default = u'/',
#         required=True,
#     ),

    IntegerField(
        name='numb_items',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        required=True,
        default=5,
    ),
                                                         
    StringField(
        name='kind',
        widget=SelectionWidget(
            label=_(u"Selecione o layout"),
            description=_(u"Selecione o layout desejado para o bloco."),
            label_msgid='vindula_tile_label_layout',
            description_msgid='vindula_tile_help_layout',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[("padrao",_(u"Tema padrão")),
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
                                                         
    IntegerField(
        name='widthImage',
        widget = IntegerWidget(
            label = 'Largura da imagem',
            description='Largura da imagem do item listado no bloco.</br>Deixar o campo vazio para usar o valor padrão.',
        ),
        required=False,
    ),
                                                         
    IntegerField(
        name='heightImage',
        widget = IntegerWidget(
            label = 'Altura da imagem',
            description='Altura da imagem do item listado no bloco.</br>Deixar o campo vazio para usar o valor padrão.',
        ),
        required=False,
    ),
                                                         
    BooleanField(
        name='hideSubheader',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Ocultar subtítulo Mais Acessados",
            description='Selecione para ocultar o subtítulo "Mais Acessados" que aparece acima dos itens listados.',
            label_msgid='vindula_tile_label_hideSubheader',
            description_msgid='vindula_tile_help_hideSubheader',
        ),
    ),
                                                         
    BooleanField(
        name='hideDateTime',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Ocultar data e hora",
            description='Oculta a data em hora de cada item do bloco.',
            label_msgid='vindula_tile_label_hideDateTime',
            description_msgid='vindula_tile_help_hideDateTime',
        ),
    ),
                                                         
    BooleanField(
        name='showQtdAccess',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Mostrar quantidade de acessos",
            description='Mostra a quantidade de acessos de cada item do bloco.',
            label_msgid='vindula_tile_label_showQtdAccess',
            description_msgid='vindula_tile_help_showQtdAccess',
        ),
    ),
    
    BooleanField(
        name='showPagination',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Mostrar paginação no bloco",
            description='Ativar a paginação no bloco.',
            label_msgid='vindula_tile_label_showPagination',
            description_msgid='vindula_tile_help_showPagination',
        ),
    ),
                                                         
    IntegerField(
        name='qtdMaxPages',
        schemata='settings',
        widget = IntegerWidget(
            label = 'Quantidade maxima de páginas',
            description='Insira a quantidade máxima de páginas a ser mostrada na listagem.',
        ),
        required=True,
        default=5,
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
        types = []
        for item in self.portal_types.listContentTypes():
            if not item in BLACK_LIST_PLONETYPES:
                types.append(item)
        return types

    #Scripts js
    scripts_js = ['/++resource++vindula.tile/js/button-more.js', 
                  '/++resource++vindula.tile/js/ajax_boll_batch.js', 
                  '/++resource++vindula.content/js/ajax_list_file.js']

registerType(TileMoreAccess, PROJECTNAME)
