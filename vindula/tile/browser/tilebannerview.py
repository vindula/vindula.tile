# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok

grok.templatedir('templates')

class TileBannerView(BaseView):
    grok.name('tilebanner-view')

    def getTileBanner(self):
        L = []
        obj = self.context
        banners = obj.getImageBanner()
        if banners != None or banners != '':
            for banner in banners:
                D = {}
                D['title'] = banner.Title()
                D['text'] = banner.Description()
                D['image'] = banner.absolute_url() + '/imagem_banner_preview'
                D['target'] = banner.getTarget()
                D['url'] = banner.getLink()
                if obj.ativaData == True:
                    D['date'] = banner.creation_date.strftime('%d/%m/%Y')
                if obj.ativaAutor == True:
                    D['author'] = banner.getOwner().getUserName()
                #TODO: Criar método para buscar o nome da Unidade
                if obj.ativaUnidade == True:
                    D['unit']= 'Nome da Unidade'
                L.append(D)
        return L
        


        
        