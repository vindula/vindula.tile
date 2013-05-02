# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok

grok.templatedir('templates')

class TileListagemHorizontalView(BaseView):
    grok.name('tilelistagemhorizontal-view')

    def getItens(self):
        pass