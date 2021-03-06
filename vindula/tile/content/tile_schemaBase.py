# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.Archetypes.public import *

from Products.ATContentTypes.content.base import ATCTContent, ATContentTypeSchema
from Products.ATContentTypes.content import schemata
from plone.contentrules.engine.interfaces import IRuleAssignable

from vindula.tile.content.interfaces import IBaseTile
from vindula.tile import MessageFactory as _
from vindula.tile.config import *

BaseTile_schema = ATContentTypeSchema + Schema((

    BooleanField(
        name='activ_recurcividade',
        default=False,
        widget=BooleanWidget(
            label="Ativar Recursividade",
            description='Se selecionado, ativa a opção de recursividade do portlet em níveis inferiores.',
        ),
        required=False,
        schemata = 'settings'
    ),

    BooleanField(
        name='bloquea_portlet',
        default=False,
        widget=BooleanWidget(
            label="Bloquear Vindula Portlets dos níveis superiores",
            description='Se selecionado, irá bloquear todos os portlets dos níveis superiores do portal.(Cautela para usar esta opção).',
        ),
        required=False,
        schemata = 'settings'
    ),

    StringField(
        name='coluna',
        default=u'direita',
        widget=SelectionWidget(label=_(u"Coluna do Portlet"),
                               description=_(u"Selecione em qual coluna o portlet será carregado."),
                               ),
        required=True,
        vocabulary='voc_coluna',
        schemata = 'settings'
    ),
    
    BooleanField(
        name='is_accessory',
        default=False,
        widget=BooleanWidget(
            label="Acessório",
            description='Selecione caso o tile for um tile acessório (irá mudar o layout do tile).',
        ),
        required=False,
        schemata = 'settings'
    ),
                                                
    BooleanField(
        name='hide_title',
        default=False,
        widget=BooleanWidget(
            label="Ocultar título",
            description='Oculta o título do bloco atual.',
        ),
        required=False,
        schemata = 'settings'
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
        default='12',
        required=True,
    ),
    

))

schemata.finalizeATCTSchema(BaseTile_schema, folderish=False)
invisivel = {'view':'invisible','edit':'invisible',}


hiddem = ['allowDiscussion','creators','contributors','rights','effectiveDate',\
          'expirationDate','subject','relatedItems','location','language',]

for i in hiddem:
    BaseTile_schema[i].widget.visible = invisivel


class BaseTile(ATCTContent):
    """ Reserve Content for BaseTile"""
    security = ClassSecurityInfo()

    implements(IBaseTile, IRuleAssignable)
    portal_type = 'BaseTile'
    _at_rename_after_creation = True
    schema = BaseTile_schema

    def voc_coluna(self):
        return DisplayList(((u'direita', u'Coluna da Direita'),
                            (u'meio', u'Coluna do Meio'),
                            (u'esquerda', u'Coluna da Esquerda')))

    def get_columns(self):
        if hasattr(self, 'getColumns'):
            return int(self.getColumns())
        else:
            return self.columns


registerType(BaseTile, PROJECTNAME)

