# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.Archetypes.public import *

from Products.ATContentTypes.content.base import ATCTContent, ATContentTypeSchema
from Products.ATContentTypes.content import schemata


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
        schemata = 'Settings'
    ),

    BooleanField(
        name='bloquea_portlet',
        default=False,
        widget=BooleanWidget(
            label="Bloquear Vindula Portlets dos níveis superiores",
            description='Se selecionado, irá bloquear todos os portlets dos níveis superiores do portal.(Cautela para usar esta opção)',
        ),
        required=False,
        schemata = 'Settings'
    ),

    StringField(
        name='coluna',
        default=u'direita',
        widget=SelectionWidget(label=_(u"Coluna do Portlet"),
                               description=_(u"Selecione em qual coluna o portlet será carregado."),
                               ),
        required=True,
        vocabulary='voc_coluna',
        schemata = 'Settings'
    ),
    
    BooleanField(
        name='is_accessory',
        default=False,
        widget=BooleanWidget(
            label="Acessório",
            description='Selecione caso o tile for um tile acessório (irá mudar o layout do tile)',
        ),
        required=False,
        schemata = 'Settings'
    ),

))

schemata.finalizeATCTSchema(BaseTile_schema, folderish=False)

class BaseTile(ATCTContent):
    """ Reserve Content for BaseTile"""
    security = ClassSecurityInfo()

    implements(IBaseTile)
    portal_type = 'BaseTile'
    _at_rename_after_creation = True
    schema = BaseTile_schema

    def voc_coluna(self):
        return DisplayList(((u'direita', u'Coluna da Direita'),
                            (u'meio', u'Coluna do Meio'),
                            (u'esquerda', u'Coluna da Esquerda')))

    def get_columns(self):
        if hasattr(self, 'getColumns'):
            return self.getColumns()
        else:
            return self.columns


registerType(BaseTile, PROJECTNAME)

