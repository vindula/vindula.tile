# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from plone.app.folder.folder import ATFolder
from plone.contentrules.engine.interfaces import IRuleAssignable
from Products.ATContentTypes.content.schemata import finalizeATCTSchema


from vindula.tile.content.interfaces import ILayout
from vindula.tile import MessageFactory as _
from vindula.tile.config import *

Layout_schema = ATFolder.schema.copy() + Schema((



))

finalizeATCTSchema(Layout_schema, folderish=True)

class Layout(ATFolder):
    """ Reserve Content for Layout"""
    security = ClassSecurityInfo()

    implements(ILayout, IRuleAssignable)
    portal_type = 'Layout'
    _at_rename_after_creation = True
    schema = Layout_schema



registerType(Layout, PROJECTNAME)

