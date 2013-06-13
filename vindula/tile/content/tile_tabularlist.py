# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileTabularList

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

from zope.schema.interfaces import IVocabularyFactory
from zope.component import queryUtility

TileTabularList_schema = BaseTile.schema.copy() + Schema((
                                                         
    ReferenceField('structure',
        multiValued=0,
        allowed_types=('OrganizationalStructure',),
        relationship='context_structure',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Escolha uma Unidade Organizacional"),
            description=_(u"Selecione uma Unidade Organizacional que deseja listar os documentos."),
        ),
        required=False,
    ),

    LinesField(
        name='object_type',
        multiValued=1,
        widget=MultiSelectionWidget(
            label=_(u"Tipo de conteudo"),
            description=_(u"Selecione o tipo de itens que sera apresentado na listagem."),
            format = 'select',
        ),
        vocabulary=u'voc_ContentTypes',
        required=True,
    ),

))

finalizeATCTSchema(TileTabularList_schema, folderish=False)

class TileTabularList(BaseTile):
    """ Reserve Content for TileTabularList """
    security = ClassSecurityInfo()

    implements(ITileTabularList)
    meta_type = portal_type = archetype_name = 'TileTabularList'
    _at_rename_after_creation = True
    schema = TileTabularList_schema

    def voc_ContentTypes(self):
        types = self.portal_types.listContentTypes()
        return types
    
    #tamanho do tile
    columns = 12

    #Scripts js
    #scripts_js = ['button-more.js','ajax_boll_batch.js']

registerType(TileTabularList, PROJECTNAME)
