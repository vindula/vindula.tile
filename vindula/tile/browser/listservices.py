# -*- coding: utf-8 -*-
from five import grok
from vindula.tile.browser.baseview import BaseView
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class ListServicesView(BaseView, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('listservices-view')
    
    def getServicesCategory(self):
        context = self.context
        self.p_catalog = getToolByName(context, 'portal_catalog')
        self.p_workflow = getToolByName(context, "portal_workflow")
        self.p_membership = getToolByName(context, 'portal_membership')
        
        current_user = self.p_membership.getAuthenticatedMember()
        container = context.getServicesFolder()
        
        path = container.getPhysicalPath()
        path = "/".join(path)
        
        items = self.p_catalog(path={"query": path, "depth": 3},
                               review_state=['published', 'internally_published', 'external'],
                               sort_on="getObjPositionInParent",
                               sort_order="reverse",
                               portal_type=['ServicosCategory'])
        result = {}
        for item in items:
            item = item.getObject()
            services = self.getServicesFormCategory(current_user, item)
            if services:
                result[item] = services
        return result
            
    def getServicesFormCategory(self, current_user, category):
        path = category.getPhysicalPath()
        path = "/".join(path)
        
        items = self.p_catalog(path={"query": path, "depth": 3},
                               portal_type=['Servico'])
        
        result = []
        for item in items:
            item = item.getObject()
            if self.p_workflow.getInfoFor(item, 'review_state') in ['published', 'internally_published', 'external']:
                result.append(item)
            else:
                if self.hasPermission(current_user, item):
                    result.append(item)
                else:
                    continue
        return result
    
    def hasPermission(self, user, obj):
        user_roles = user.getRolesInContext(obj)
        if 'Reader' in user_roles or \
            'Manager' in user_roles:
            return True
        
        return False