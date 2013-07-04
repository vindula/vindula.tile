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
    
    def format_members(self, obj_list):
        lista = []
        L = None
        for count, obj in enumerate(obj_list):
            if count == 0 or count % 9 == 0:
                L = []
            L.append(obj)

            if (count + 1) % 9 == 0:
                lista.append(L)
                L = None
        if L:
            lista.append(L)

        return lista