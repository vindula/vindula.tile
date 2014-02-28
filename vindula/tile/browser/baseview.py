# coding: utf-8
from five import grok
from zope.interface import Interface

from Products.CMFCore.utils import getToolByName
from collections import OrderedDict

grok.templatedir('templates')

class BaseView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.baseclass()


    def __init__(self,context,request):
        super(BaseView,self).__init__(context,request)
        self.portal_catalog = getToolByName(context, 'portal_catalog')
        self.reference_catalog = getToolByName(self.context, "reference_catalog")
        self.p_membership = getToolByName(context, 'portal_membership')
        self.p_workflow = getToolByName(context, "portal_workflow")


    def getKind(self):
        context = self.context
        return context.getKind()


    def limitTextSize(self, text, size=100):
        if len(text) > size:
            i = size
            try:
                while text[i] != " ":
                    i += 1
                return text[:i]+'...'
            except IndexError:
                return text
        else:
            return text

            
    def has_public_or_permission(self, current_user, object_plone):
        review_states = ['published', 'internally_published', 'external']
        
        if self.p_workflow.getInfoFor(object_plone, 'review_state') in review_states:
            return True
        elif self.hasPermission(current_user,object_plone):
            return True
        
        return False
    
    def hasPermission(self, user, obj):
        user_roles = user.getRolesInContext(obj)
        if 'Reader' in user_roles or \
            'Manager' in user_roles:
            return True
        
        return False            