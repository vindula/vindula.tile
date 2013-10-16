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
        vocabulary=[('6',_(u"6 Colunas")),
                    ('12', _(u"12 Colunas")),
                    ],
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
    ),

    BooleanField(
        name='activeSort',
        default=False,
        widget=BooleanWidget(
            label=_(u"Ativa o campo de ordenação"),
            description=_(u"Ativa a opção de ordenar os conteúdos por data e mais acessados"),
            label_msgid='vindula_tile_label_activeSort',
            description_msgid='vindula_tile_help_activeSort',
            i18n_domain='vindula_tile',
          )
    ),

    BooleanField(
        name='activeAutoReload',
        default=False,
        widget=BooleanWidget(
            label=_(u"Ativa o mecanismo de atualização automática"),
            description=_(u"Ativa a opção de atualizar altomaticamente os itens da visualização e com ordenação randomica"),
            label_msgid='vindula_tile_label_activeAutoReload',
            description_msgid='vindula_tile_activeAutoReload',
            i18n_domain='vindula_tile',
          )
    ),
                                                               
    BooleanField(
        name='activeListagemContexto',
        default=False,
        widget=BooleanWidget(
            label=_(u"Ativa Listagem de 'Mais Notícias' somente do contexto"),
            description=_(u"Ativa a opção de listar apenas os itens que estão dentro da pasta selecionada"),
            label_msgid='vindula_tile_label_activeListagemContexto',
            description_msgid='vindula_tile_activeListagemContexto',
            i18n_domain='vindula_tile',
          )
    ),
                                                               

    StringField(
        name='listTypes',
        widget=SelectionWidget(
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
            allowed_types=('VindulaFolder','Folder'),
            label=_(u"Pastas"),
            relationship='VindulaFolder',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Pastas"),
                description='Selecione a Pasta que deseja buscar os itens.'
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
        types = ['Pessoas']
        types += self.portal_types.listContentTypes()
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
            L.append('ajax_auto_reload.js')

        return L

registerType(TileListagemVertical, PROJECTNAME)