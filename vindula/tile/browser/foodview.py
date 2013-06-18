# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok
from datetime import date

grok.templatedir('templates')

class FoodView(BaseView):
    grok.name('food-view')


    def getItens(self):
        context = self.context
        numbers = context.getNumb_items()
        weekday = date.today().weekday()

        path = context.portal_url.getPortalObject()
        itens = self.portal_catalog(portal_type = ('Menu',),
                                    path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                    sort_on='effective',
                                    sort_order='descending',
                                    getDias=str(weekday)
                                    )

        return itens[:numbers]

    def aq_parent(self, obj):
        context = self.context
        return obj.aq_parent