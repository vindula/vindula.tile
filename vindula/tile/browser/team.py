# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class TeamView(BaseView, UtilMyvindula):
    grok.name('team-view')
    
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

    def sorted_alfabetc(self,lst):
        return sorted(lst, key=str.lower)
        