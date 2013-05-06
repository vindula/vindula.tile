# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok

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
                                    sort_on='effective',
                                    sort_order='descending',
                                    )

        return itens[:numbers]



    def getImagem(self,obj):

        # nome dos campos de imagens dos tipos de conteudo
        fields = ['getImage', 'getImageRelac']
        for field in fields:
            if hasattr(obj, field):
                item = getattr(obj,field)
                return item.absolute_url() + '/image_mini'
