# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.interfaces import ITileCalendar
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileCalendar_schema = BaseTile.schema.copy() + Schema((


))

finalizeATCTSchema(TileCalendar_schema, folderish=False)

class TileCalendar(BaseTile):
    """ Reserve Content for TileCalendar """
    security = ClassSecurityInfo()

    implements(ITileCalendar)
    portal_type = 'TileCalendar'
    _at_rename_after_creation = True
    schema = TileCalendar_schema

    #tamanho do tile
    columns = 6
    
    #Scripts js
    scripts_js = ['/++resource++vindula.tile/js/ajax_calendar.js']


registerType(TileCalendar, PROJECTNAME)