# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content import schemata, base


from vindula.tile.content.interfaces import IBaseTile
from vindula.tile import MessageFactory as _
from vindula.tile.config import *

BaseTile_schema = schemata.ATContentTypeSchema.copy() + Schema((



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



))



schemata.finalizeATCTSchema(BaseTile_schema, folderish=False)

class BaseTile(base.ATCTContent):
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

registerType(BaseTile, PROJECTNAME)

