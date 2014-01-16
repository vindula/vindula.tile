# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class AccordionView(BaseView):
    grok.name('accordion-view')


    def get_itens_abas(self):
        context = self.context	
        current_user = self.p_membership.getAuthenticatedMember()
        L = []

        itens = self.portal_catalog(**{'sort_on': 'getObjPositionInParent',
	                                   'portal_type':['TileAccordionItem',],  
	                                   'path':{'query':'/'.join(context.getPhysicalPath()), 'depth': 1}
                                	})

        for t in itens:
            t = t.getObject()
            if not t.getExcludeFromNav() and self.has_public_or_permission(current_user, t):
                L.append(t)

        return L
