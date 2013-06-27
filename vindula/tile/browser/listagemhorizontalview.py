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
        # layout = context.getListTemplates()
        # navigation = context.getTypeNavigation()
        L = []

        for item in context.getHighlights():
            D={}

            D['title'] = self.limitTextSize(50,item.Title())
            D['description'] = self.limitTextSize(120,item.Description()[:120])
            D['url'] = item.absolute_url()

            if item.getActive_date():
                D['date'] = item.creation_date.strftime('%d/%m/%Y')
                D['hour'] = item.creation_date.strftime('%H:%M')
            else:
                D['date'] = ''
                D['hour'] = ''

            #TODO: Criar método para buscar a Unidade Organizacional
            if hasattr(item, 'getStructures') and item.getStructures():
                D['unidade'] = item.getStructures().getSiglaOrTitle()
            else:
                D['unidade'] = ''

            try:
                D['image'] = item.getImageRelac().absolute_url() + '/image_mini'
            except:
                D['image'] = ''

            D['alt'] = item.getImageCaption()

            if item.getActive_author():
                D['author'] = item.getOwner().getUserName()
            else:
                D['author'] = ''

            D['obj'] = item
            L.append(D)
        return L


    def limitTextSize(self, size, text):
        if len(text) > size:
            i = size
            while text[i] != " " and (i < len(text)):
                i += 1

            return text[:i]+'...'
        else:
            return text
