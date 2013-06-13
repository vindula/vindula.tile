# coding: utf-8
from five import grok
from Products.CMFCore.utils import getToolByName
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class ReferenceListView(BaseView):
    grok.name('referencelist-view')

    def getReferences(self):
        items = self.context.getReference_list()
        rtool = getToolByName(self.context, 'reference_catalog')
        L = []
        
        if items:
            for item in items:
                L.append({
                    'title':item.get('title',''),
                    'object': rtool.lookupObject(item.get('uid','')),
                })
        return L