# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class ListServicesView(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('listservices-view')
    
    def getServicesCategory(self):
        context = self.context
        self.p_catalog = getToolByName(context, 'portal_catalog')
        container = context.getServicesFolder()
        
        path = container.getPhysicalPath()
        path = "/".join(path)
        
        items = self.p_catalog(path={"query": path, "depth": 3},
                               portal_type=['ServicosCategory'])
        result = {}
        for item in items:
            item = item.getObject()
            
            result[item] = self.getServicesFormCategory(item)
            
        return result
            
    
    def getServicesFormCategory(self, category):
        path = category.getPhysicalPath()
        path = "/".join(path)
        
        return [i.getObject() for i in self.p_catalog(path={"query": path, "depth": 3}, portal_type=['Servico']) if i]
        
        