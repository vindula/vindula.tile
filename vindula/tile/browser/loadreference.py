# coding: utf-8
from five import grok
from Products.CMFCore.utils import getToolByName

from vindula.tile.browser.baseview import BaseView
from vindula.tile.content.interfaces import ITileLibrary
from vindula.content.models.tag_content import TagContent

from collections import OrderedDict


grok.templatedir('templates')

class LoadReferenceView(BaseView):
    grok.name('load-reference-view')
    
    def getPathMacro(self, obj):
        macro = 'context/@@%s/macros/content-core' %(obj.getLayout())
        
        return macro