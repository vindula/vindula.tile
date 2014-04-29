# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileLoadReference

from vindula.tile import MessageFactory as _
from vindula.tile.config import *
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget


TileLoadReference_schema = BaseTile.schema.copy() + Schema((
                                                      
    ReferenceField('contentToLoad',
        multiValued=0,
        allowed_types=('VindulaNews',),
        relationship='content_to_load',
        widget=VindulaReferenceSelectionWidget(
            label=_(u"Conteúdo relacionado"),
            description=_(u"Selecione o conteúdo que deseja que aparece no bloco."),
        ),
        required=True,
    ),
                                                      
    BooleanField(
        name='useReferenceTitle',
        default=False,
        widget=BooleanWidget(
            label="Usar o título do conteúdo",
            description='Se selecionado irá usar o título do conteúdo referenciado ao invés do título do bloco.',
        ),
        required=False,
    ),
))

finalizeATCTSchema(TileLoadReference_schema, folderish=False)

class TileLoadReference(BaseTile):
    """ Reserve Content for TileLoadReference """
    security = ClassSecurityInfo()

    implements(ITileLoadReference)
    portal_type = 'TileLoadReference'
    _at_rename_after_creation = True
    schema = TileLoadReference_schema
    
    #tamanho do tile
    columns = 12

    #Scripts js
    scripts_js = []
    
    #Folhas de estilo css
    style_sheets = []

registerType(TileLoadReference, PROJECTNAME)