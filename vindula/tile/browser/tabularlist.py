# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.content.models.content import ModelsContent

import string

grok.templatedir('templates')

class TabularListView(BaseView):
    grok.name('tabularlist-view')
    
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