# -*- coding: utf-8 -*-
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class ListagemVerticalView(BaseView):
    grok.name('listagemvertical-view')


    def getItens(self):
        context = self.context
        numbers = context.getNumb_items()

        types = context.getListTypes()
        # states = context.getTypesWorkflow()

        path = context.getPath()
        if not path:
            path = context.portal_url.getPortalObject()

        itens = self.portal_catalog(portal_type = types,
                                    # review_state = states,
                                    path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                    sort_on='getObjPositionInParent',
                                    sort_order='descending',
                                    )
        return itens[:numbers]
