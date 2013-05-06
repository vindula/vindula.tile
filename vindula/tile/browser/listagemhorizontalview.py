# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok

grok.templatedir('templates')

class ListagemHorizontalView(BaseView):
    grok.name('listagemhorizontal-view')

    def getItens(self):
        context = self.context
        layout = context.getListTemplates()
        itens = context.getHighlights()
        navigation = context.getTypeNavigation()
        L = []
        if itens != None or itens !='':
            for item in itens:
                D={}
                D['title'] = item.Title()
                D['description'] = item.Description()[:200] + '...'
                D['url'] = item.absolute_url()
                if item.getActive_date():
                    D['date'] = item.creation_date.strftime('%d/%m/%Y')
                    D['hour'] = item.creation_date.strftime('%H:%M')
                else:
                    D['date'] = ''
                    D['hour'] = ''
                #TODO: Criar método para buscar a Unidade Organizacional
                D['unidade'] = 'ASCOM'
                try:
                    D['image'] = item.getImageRelac().absolute_url()
                except:
                    D['image'] = ''
                D['alt'] = item.getImageCaption()
                if item.getActive_author():
                    D['author'] = item.getOwner().getUserName()
                else:
                    D['author'] = ''
                L.append(D)
        return L



