# -*- coding: utf-8 -*-
from five import grok
from vindula.tile.browser.baseview import BaseView
import DateTime, random
from datetime import datetime, date, timedelta


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
                'sort_order':'descending',}

        if is_date:
            activeSarchEvents = context.getActiveSarchEvents()

            if activeSarchEvents:
                today = DateTime.DateTime()
                query['start'] = {'query': today, 'range': 'max'}
                query['end'] = {'query': today, 'range': 'min'}
            else:
                start = DateTime.DateTime() - 1 # ONTEM
                end = DateTime.DateTime() + 120 # Até quato meses no futuro
                query['start'] = {'query': (start, end), 'range': 'min:max'}

            query['sort_on'] = 'start'
            query['sort_order'] ='ascending'

        else:

            query['sort_on'] = context.getSorted_itens()

            if context.getActive_reserve():
                query['sort_order'] = 'ascending'


        itens = self.portal_catalog(query)
        L = []
        L_tmp = []

        for fix in context.getFixed_featured():
            L.append(fix)
            L_tmp.append(fix.UID())

        if len(itens) + len(L) < numbers:
            numbers = len(itens) + len(L)

        if context.getActiveAutoReload():
            while len(L) < numbers:
                chosen = random.choice(itens)
                if not chosen.UID in L_tmp:
                    L_tmp.append(chosen.UID)
                    L.append(chosen)

        else:
            for item in itens:
                if len(L) < numbers:
                    L_tmp.append(item.UID)
                    L.append(item)
                else:
                    break

        return L

    def get_convert_data(self, str_data):
        months = ['XX','Jan','Fev','Mar','Abr','Maio','Jun',\
                       'Jul','Ago','Set', 'Out', 'Nov','Dez']

        list_date = str_data.split('/')
        obj_date = date(int(list_date[2]),int(list_date[1]),int(list_date[0]))
        mes = months[obj_date.month]
        return mes

    def get_path_other_new(self):
        path = self.context.getPath_othernews()
        if path:
            return path.absolute_url()

        return None


    def has_organization(self, obj):
        if hasattr(obj, 'getStructures'):
            return True
        return False

