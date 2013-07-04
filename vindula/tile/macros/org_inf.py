# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface

from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class OrgStrucInfView(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('orgstruc-info')


    def get_structure(self,context=None):
        if not context:
            context = self.context

        if context.portal_type != 'Plone Site' and\
            context.portal_type != 'OrganizationalStructure':

            return self.get_structure(context.aq_parent)
        else:
            return context
        
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
