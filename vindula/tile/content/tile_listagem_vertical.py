# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.CMFCore.utils import getToolByName
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileListagemVertical

from vindula.tile import MessageFactory as _
from vindula.tile.config import *


TileListagemVertical_schema = BaseTile.schema.copy() + Schema((

    StringField(
        name='kind',
        widget=SelectionWidget(
            label=_(u"Lista de Templates"),
            description=_(u"Selecione qual template deseja utilizar."),
            label_msgid='vindula_tile_label_layout',
            description_msgid='vindula_tile_help_layout',
            i18n_domain='vindula_tile',
            format = 'select',
         ),
         vocabulary=[("listagem_com_imagem",_(u"Listagem com imagem")),
                    ("listagem_sem_imagem",_(u"Listagem sem imagem")),
                    ("listagem_com_icones", _(u"Listagem com ícones e sem imagem")),
                    ("listagem_sem_icones", _(u"Destaque sem ícones e sem imagem")),
                    ("listagem_evento", _(u"Lista de Eventos")),
                    ("listagem_agenda", _(u"Lista da Agenda")),
                    ("listagem_tabular", _(u"Lista de Tabela")),
                    ("listagem_mais_recentes", _(u"Lista mais recentes")),
                    ],

         default='listagem_com_imagem',
         required=True,
     ),

    StringField(
        name='columns',
        widget=SelectionWidget(
            label=_(u"Tamanho do tile"),
            description=_(u"Selecione o tamanho do tile."),
            label_msgid='vindula_tile_label_columns',
            description_msgid='vindula_tile_help_columns',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=VOCABULARY_COLUNAS,
        default='6',
        required=True,
    ),

    IntegerField(
        name='numb_items',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        default=5,
        required=True,
    ),

    StringField(
        name='sorted_itens',
        widget=SelectionWidget(
            label=_(u"Tipo de ordenação"),
            description=_(u"Selecione qua será o tipo de ordenação dos conteúdos"),
            label_msgid='vindula_tile_label_sorted_itens',
            description_msgid='vindula_tile_help_sorted_itens',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=VOCABULARY_SORTED_ITENS,
        default='getObjPositionInParent',
        required=True,
    ),

    BooleanField(
        name='active_reserve',
        widget=BooleanWidget(
            label=_(u"Ordenação reversa"),
            description=_(u"Reverte a ordem dos conteúdos listados."),
            label_msgid='vindula_tile_label_active_reserve',
            description_msgid='vindula_tile_help_active_reserve',
            i18n_domain='vindula_tile',
        ),
        default=True
    ),

    # BooleanField(
    #     name='activeSort',
    #     default=False,
    #     widget=BooleanWidget(
    #         label=_(u"Ativa o campo de ordenação"),
    #         description=_(u"Ativa a opção de ordenar os conteúdos por data e mais acessados"),
    #         label_msgid='vindula_tile_label_activeSort',
    #         description_msgid='vindula_tile_help_activeSort',
    #         i18n_domain='vindula_tile',
    #       )
    # ),

    BooleanField(
        name='activeAutoReload',
        default=False,
        widget=BooleanWidget(
            label=_(u"Ativa o mecanismo de atualização automática"),
            description=_(u"Ativa a opção de atualizar automaticamente os itens da visualização e com ordenação randomica"),
            label_msgid='vindula_tile_label_activeAutoReload',
            description_msgid='vindula_tile_activeAutoReload',
            i18n_domain='vindula_tile',
          )
    ),

    ReferenceField('fixed_featured',
        multiValued=1,
        # allowed_types=('VindulaFolder','Folder', 'VindulaClipping'),
        label=_(u"Destaques Fixos"),
        relationship='fixed_featured',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Destaques Fixos"),
            description='Selecione os itens que ficaram em destaque na listagem do bloco'
        ),
        review_state = ('published', 'internal','external')
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
            allowed_types=('VindulaFolder','Folder', 'VindulaClipping','OrganizationalStructure'),
            label=_(u"Pastas"),
            relationship='path',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Pastas"),
                description='Selecione a pasta que deseja buscar os itens.'
            ),
            review_state = ('published', 'internal','external')
        ),

    ReferenceField('path_othernews',
            multiValued=0,
            allowed_types=('VindulaFolder','Folder', 'VindulaClipping','OrganizationalStructure'),
            label=_(u"Pastas"),
            relationship='path_othernews',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Listagem mais itens"),
                description='Selecione a pasta que deseja listar a visão dos "mais itens"'
            ),
            review_state = ('published', 'internal','external')
        ),

    # StringField(
    #     name='typesWorkflow',
    #     widget=SelectionWidget(
    #         label=_(u"Lista de Workflow"),
    #         description=_(u"Selecione por quais workflow deseja efetuar a busca."),
    #         label_msgid='vindula_tile_label_typesWorkflow',
    #         description_msgid='vindula_tile_help_typesWorkflow',
    #         i18n_domain='vindula_tile',
    #      ),
    #      vocabulary='voc_list_workflow',
    #      required=False,
    #  ),

    BooleanField(
        name='activeMoreButton',
        default=True,
        widget=BooleanWidget(
            label="Botão mais items",
            description='Caso selecionado, ativa o botão de mais items na visão do bloco.',
            label_msgid='vindula_tile_label_activeMoreButton',
            description_msgid='vindula_tile_help_activeMoreButton',
        ),
    ),

    BooleanField(
        name='activeSarchEvents',
        default=False,
        widget=BooleanWidget(
            label="Ativar busca de eventos",
            description='Caso selecionado, ativa a busca de eventos que estão acontecendo.',
            label_msgid='vindula_tile_label_activeSarchEvents',
            description_msgid='vindula_tile_help_activeSarchEvents',
        ),
    ),

    BooleanField(
        name='hideSharing',
        default=False,
        widget=BooleanWidget(
            label="Ocultar compartilhamento",
            description='Ocultar  a barra de compatilhamento por item no title.',
            label_msgid='vindula_tile_label_hideSharing',
            description_msgid='vindula_tile_help_hideSharing',
        ),
    ),

    BooleanField(
        name='hideEventInfo',
        schemata='settings',
        default=False,
        widget=BooleanWidget(
            label="Ocultar informações do evento",
            description='Selecione para ocultar as informações do evento na visão de eventos.',
            label_msgid='vindula_tile_label_hideEventInfo',
            description_msgid='vindula_tile_help_hideEventInfo',
        ),
    ),

))

finalizeATCTSchema(TileListagemVertical_schema, folderish=False)

class TileListagemVertical(BaseTile):
    """ Reserve Content for TileListagemVertical"""
    security = ClassSecurityInfo()

    implements(ITileListagemVertical)
    portal_type = 'TileListagemVertical'
    _at_rename_after_creation = True
    schema = TileListagemVertical_schema

    def voc_list_types(self):
        types = [('Pessoas','Pessoas')]
        for item in LIST_PLONETYPES:
            obj = self.portal_types[item]

            types.append(
                (item, obj.title)
            )

        return types

    def voc_list_workflow(self):
        #TODO: Implementar método que retorna todos os workflows
        return ['published','internal','external']

    #tamanho do tile
    columns = 6

    #Scripts js
    @property
    def scripts_js(self):
        L = []
        if self.getActiveAutoReload():
            L.append('/++resource++vindula.tile/js/ajax_auto_reload.js')

        return L

registerType(TileListagemVertical, PROJECTNAME)
