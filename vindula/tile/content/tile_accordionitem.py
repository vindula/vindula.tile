# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.ATContentTypes.content.newsitem import ATNewsItemSchema
from Products.ATContentTypes.content.newsitem import ATNewsItem

from vindula.tile.content.interfaces import ITileAccordionItem

from vindula.tile import MessageFactory as _
from vindula.tile.config import *



TileAccordionItem_schema =  ATNewsItemSchema.copy()


invisivel = {'view':'invisible','edit':'invisible',}
TileAccordionItem_schema['image'].widget.visible = invisivel
TileAccordionItem_schema['imageCaption'].widget.visible = invisivel

finalizeATCTSchema(TileAccordionItem_schema)

class TileAccordionItem(ATNewsItem):
    """ TileAccordionItem """

    security = ClassSecurityInfo()
    implements(ITileAccordionItem)
    portal_type = 'TileAccordionItem'
    _at_rename_after_creation = True
    schema = TileAccordionItem_schema


registerType(TileAccordionItem, PROJECTNAME)