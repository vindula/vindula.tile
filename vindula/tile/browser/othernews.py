# -*- coding: utf-8 -*-
from five import grok
from Products.CMFCore.utils import getToolByName

from vindula.tile.browser.baseview import BaseView


grok.templatedir('templates')

class OtherNewsView(BaseView):
    grok.name('outras-noticias')
    
    def getQuery(self):
        context = self.context
        query = {}
        portal_catalog = getToolByName(context, 'portal_catalog')
        path = context.portal_url.getPortalObject().getPhysicalPath()


        form = self.request.form
        
        
        if 'path' in form.keys():
            path = form.get('path', '')
            if path:
                path = eval(path)
        
        query.update({'path': {'query':'/'.join(path) } })
        
        
        if 'portal_type' in form.keys():
            portal_types = form.get('portal_type', '')
            
            try:
                portal_types = eval(portal_types)
            #Significa que o valor veio vazio 
            except SyntaxError: 
                portal_types = ''
            #Significa que nao veio uma tupla e sim um valor em string
            except NameError: 
                pass
                
            query.update({'portal_type': portal_types})
            
        else:
            query.update({'portal_type': ('VindulaNews', 'News Item') })
        


        query.update({'review_state': ['published', 'internally_published', 'external']})
        
        
        query.update({'sort_on':'created',
                      'sort_order':'descending',
                     })

        result = portal_catalog(**query)
        
        return result
        
        
        
        

