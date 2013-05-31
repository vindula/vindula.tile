# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface

from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class InformationView(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('information-view')


    def get_structure(self,context=None):
        if not context:
            context = self.context

        if context.portal_type != 'Plone Site' and\
            context.portal_type != 'OrganizationalStructure':

            return self.get_structure(context.aq_parent)
        else:
            return context
