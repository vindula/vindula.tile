# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileLibrary

from vindula.tile import MessageFactory as _
from vindula.tile.config import *
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from zope.schema.interfaces import IVocabularyFactory
from zope.component import queryUtility

TileLibrary_schema = BaseTile.schema.copy() + Schema((
                                                      
    StringField(
        name='kind',
        widget=SelectionWidget(
            label=_(u"Selecione o layout"),
            description=_(u"Selecione o layout desejado."),
            label_msgid='vindula_tile_label_kind',
            description_msgid='vindula_tile_help_kind',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=[("padrao",_(u"Tema Padrão"))],
        default='padrao',
        required=True,
    ),

    IntegerField(
        name='qtdThemesGlobal',
        widget = IntegerWidget(
            label = 'Quantidade de temas a ser exibido',
            description='Quantidade máxima de temas a ser exibido no bloco',
        ),
        default=50,
    ),
                                                      
    IntegerField(
        name='qtdThemesPage',
        widget = IntegerWidget(
            label = 'Quantidade de temas por página',
            description='Quantidade máxima de temas a ser exibido por página',
        ),
        default=10,
    ),
                                                      
    ReferenceField('iconFileDefault',
        multiValued=0,
        allowed_types=('Image',),
        relationship='context_structure',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Selecione o ícone da listagem de arquivos"),
            description=_(u"Selecione o ícone que aparecerá na listagem dos arquivos."),
        ),
        required=True,
    ),
    
))

finalizeATCTSchema(TileLibrary_schema, folderish=False)

class TileLibrary(BaseTile):
    """ Reserve Content for TileLibrary """
    security = ClassSecurityInfo()

    implements(ITileLibrary)
    portal_type = 'TileLibrary'
    _at_rename_after_creation = True
    schema = TileLibrary_schema
    
    #tamanho do tile
    columns = 12

    #Scripts js
    scripts_js = ['/++resource++vindula.tile/js/ajax_boll_batch.js']
    
    #Folhas de estilo css
    style_sheets = ['/++resource++vindula.tile/css/library-tile.css']

registerType(TileLibrary, PROJECTNAME)
