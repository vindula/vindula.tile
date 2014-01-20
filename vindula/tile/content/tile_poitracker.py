# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.interfaces import ITilePoiTracker
from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TilePoiTracker_schema = BaseTile.schema.copy() + Schema((


	ReferenceField('poi_tracker',
	        multiValued=0,
	        allowed_types=('PoiTracker'),
	        relationship='PoiTracker',
	        widget=VindulaReferenceSelectionWidget(
	            label=_(u"Gerenciador de Ocorrências"),
	            description='Selecione o gerenciador de ocorrências, onde serão adicionadas as ocorrêcias.'
	        ),
	        review_state = ('published', 'internal','external'),
	        required=True,
	),

))

finalizeATCTSchema(TilePoiTracker_schema, folderish=False)

class TilePoiTracker(BaseTile):
    """ Reserve Content for TilePoiTracker """
    security = ClassSecurityInfo()

    implements(ITilePoiTracker)
    portal_type = 'TilePoiTracker'
    _at_rename_after_creation = True
    schema = TilePoiTracker_schema

    #tamanho do tile
    columns = 6

registerType(TilePoiTracker, PROJECTNAME)