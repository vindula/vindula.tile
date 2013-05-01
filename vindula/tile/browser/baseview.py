# coding: utf-8
from five import grok
from zope.interface import Interface

from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class BaseView(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.baseclass()


    def __init__(self,context,request):
        super(BaseView,self).__init__(context,request)
        self.portal_catalog = getToolByName(context, 'portal_catalog')

