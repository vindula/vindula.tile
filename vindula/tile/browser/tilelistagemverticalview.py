# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok

grok.templatedir('templates')

class TileListagemVerticalView(BaseView):
    grok.name('tilelistagemvertical-view')

    def getTemplate(self):
        context = self.context
        return context.getListTemplate()

    def getItens(self):
        context = self.context
        layout = self.context.getListTemplate()
        if layout == 'listagem_com_imagem':
            types = context.getListTypes()
            states = context.getTypesWorkflow()
            path = context.getPath()
            recursion = context.activeRecursion
            itens = self.portal_catalog(portal_type = types,
                         review_state = states,
                         path={'query':'/'.join(path.getPhysicalPath()),'depth':99}
                       )
            return itens
        else:
            return []



