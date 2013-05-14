# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok

grok.templatedir('templates')

class BannerView(BaseView):
    grok.name('banner-view')

    def getTileBanner(self):
        L = []
        obj = self.context
        banners = obj.getImageBanner()
        if banners != None or banners != '':
            for banner in banners:
                D = {}
                D['title'] = banner.Title()
                D['text'] = banner.Description()
                D['image'] = banner.absolute_url() + '/image'
                D['target'] = banner.getTarget()
                D['url'] = banner.getLink()
                if obj.activeDate == True:
                    D['date'] = banner.creation_date.strftime('%d/%m/%Y')
                if obj.activeAuthor == True:
                    D['author'] = banner.getOwner().getUserName()
                #TODO: Criar método para buscar o nome da Unidade
                if obj.activeUnit == True:
                    D['unit']= 'Nome da Unidade'
                L.append(D)
        return L




