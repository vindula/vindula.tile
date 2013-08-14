# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileHowDo

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

from zope.schema.interfaces import IVocabularyFactory
from zope.component import queryUtility

TileHowDo_schema = BaseTile.schema.copy() + Schema((

    LinesField(
        name='objectType',
        multiValued=1,
        widget=MultiSelectionWidget(
            label=_(u"Tipo de conteudo"),
            description=_(u"Selecione o tipo de conteúdo que sera apresentado."),
            format = 'select',
        ),
        vocabulary=u'vocabularyContentTypes',
        required=True,
    ),
    
    LinesField(
        name='subjects',
        multiValued=1,
        widget=MultiSelectionWidget(
            label=_(u"Tags"),
            description=_(u"Selecione a(s) tag(s) relacionadas aos conteúdos que deseja aparecer na listagem."),
            format = 'select',
        ),
        vocabulary=u'vocabularySubjects',
        required=True,
    ),

    IntegerField(
        name='numItems',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        default=5,
        required=True,
    ),

))

finalizeATCTSchema(TileHowDo_schema, folderish=False)

class TileHowDo(BaseTile):
    """ Reserve Content for TileHowDo """
    security = ClassSecurityInfo()

    implements(ITileHowDo)
    meta_type = portal_type = archetype_name = 'TileHowDo'
    _at_rename_after_creation = True
    schema = TileHowDo_schema

    def vocabularyContentTypes(self):
        types = self.portal_types.listContentTypes()
        return types
    
    def vocabularySubjects(self):
        catalog = self.portal_catalog
        return catalog.uniqueValuesFor('Subject')
    
    #tamanho do tile
    columns = 12

    #Scripts js
#    scripts_js = ['button-more.js','ajax_boll_batch.js']

registerType(TileHowDo, PROJECTNAME)
