# -*- coding: utf-8 -*-
from five import grok
from Acquisition import aq_inner, aq_parent
from zope.interface import Interface

from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class OrganogramMacro(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('organogram-macro')
    
    
    def get_org_pai(self, estruc):
        if estruc.portal_type == 'OrganizationalStructure':
            return estruc
        elif self.context.portal_url.getPortalObject() == estruc:
            return False
        else:
            result = self.get_org_pai(estruc.aq_parent)
        return result
    
    def get_org(self):
        return self.get_org_pai(self.context)
