# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface

from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class InfoStructureView(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('infostructure-view')
    
    def getSuperStructure(self,context):
        if context.portal_type == 'OrganizationalStructure':
            return context
        if context.portal_type == 'Plone Site':
            return None
        else:
            return self.getSuperStructure(context.aq_parent)
        
    
    def getStructure(self):
        item = self.context.getStructure()
        if not item:
            item = self.getSuperStructure(self.context)
        return item