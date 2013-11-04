# -*- coding: utf-8 -*-
from five import grok
from vindula.tile.browser.baseview import BaseView
import DateTime, random

grok.templatedir('templates')

class ListagemVerticalView(BaseView):
    grok.name('listagemvertical-view')


    def getItens(self, is_date=False):
        context = self.context
        numbers = context.getNumb_items()

        types = context.getListTypes()
        # states = context.getTypesWorkflow()

        path = context.getPath()
        if not path:
            path = context.portal_url.getPortalObject()
            
        query = {'portal_type': types,
                # review_state : states,
                'path':{'query':'/'.join(path.getPhysicalPath()),'depth':99},
                'sort_on':'getObjPositionInParent',
                'sort_order':'descending',}
        
        if is_date:
            start = DateTime.DateTime() - 1  # ONTEM
            end = DateTime.DateTime() + 120   # Até quato meses no futuro
            date_range_query = {'query': (start, end), 'range': 'min:max'}
            
            query['start'] = date_range_query
            query['sort_on'] = 'start'
            query['sort_order'] ='ascending'
        
        itens = self.portal_catalog(query)

        if context.getActiveAutoReload():
            L = []
            L_tmp = []

            if len(itens) < numbers:
                numbers = len(itens)

            while len(L) < numbers:
                chosen = random.choice(itens)
                if not chosen.UID in L_tmp:
                    L_tmp.append(chosen.UID)
                    L.append(chosen)

            return L
        else:
            return itens[:numbers]
