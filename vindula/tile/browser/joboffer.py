# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

class JobOfferView(grok.View, UtilMyvindula):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('joboffer-view')