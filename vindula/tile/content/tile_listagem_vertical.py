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

    BooleanField(
        name='activeSort',
        default=False,
        widget=BooleanWidget(
            label=_(u"Ativa o campo de ordenação"),
            description=_(u"Ativa a opção de ordenar os conteúdos por data e mais acessados"),
            label_msgid='vindula_tile_label_activeSort',
            description_msgid='vindula_tile_help_activeSort',
            i18n_domain='vindula_tile',
          )),
    
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

    ReferenceField('VindulaFolder',
            multiValued=0,
            allowed_types=('VindulaFolder','Folder'),
            label=_(u"Pastas"),
            relationship='VindulaFolder',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Pastas"),
                description='Selecione a Pasta que deseja buscar os itens.'),
                review_state = ('published', 'internal','external')),


    BooleanField(
        name='activeRecursion',
        default=False,
        widget=BooleanWidget(
            label=_(u"Ativa Recursividade"),
            description=_(u"Ativa a recursividade para buscar dentro das demais pastas."),
            label_msgid='vindula_tile_label_activeRecursion',
            description_msgid='vindula_tile_help_activeRecursion',
            i18n_domain='vindula_tile',
          )),
    
    StringField(
        name='typesWorkflow',
        widget=SelectionWidget(
            label=_(u"Lista de Workflow"),
            description=_(u"Selecione por quais workflow deseja efetuar a busca."),
            label_msgid='vindula_tile_label_typesWorkflow',
            description_msgid='vindula_tile_help_typesWorkflow',
            i18n_domain='vindula_tile',
         ),
         vocabulary='voc_list_workflow',
         required=False,
     ),

    StringField(
        name='listMacros',
        widget=SelectionWidget(
            label=_(u"Lista de Macros"),
            description=_(u"Selecione qual macro(template) deseja utilizar."),
            label_msgid='vindula_tile_label_listMacros',
            description_msgid='vindula_tile_help_listMacros',
            i18n_domain='vindula_tile',
            format = 'select',
         ),
         vocabulary='voc_list_macros',
         required=True,
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
        types = self.portal_types.listContentTypes()
        return types

    def voc_list_workflow(self):
        #TODO: Implementar método que retorna todos os workflows
        return ['published','internal','external']

    def voc_list_macros(self):
        return ['Listagem com imagem','Listagem sem imagem com ícones','Listagem sem imagem sem ícones']

    def query_catalog(self,type,path,depth):
        pass

registerType(TileListagemVertical, PROJECTNAME)
