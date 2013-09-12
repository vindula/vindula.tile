# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from vindula.tile.browser.baseview import BaseView

from five import grok

grok.templatedir('templates')

class BannerCompostView(BaseView):
    grok.name('bannercompost-view')

    def get_static(self):
        ctx = self.context
        portal = getToolByName(ctx, 'portal_url').getPortalObject()
        url_portal = portal.absolute_url()
        return url_portal +'/++resource++vindula.tile/'

    def get_image_backgroud(self):
        obj = self.context
        itens_news = obj.getImageBackgroud()

        if itens_news:
            return itens_news.absolute_url()
        return ''

    def getNoticiasBanner(self):
        L = []
        obj = self.context
        itens_news = obj.getFeatured_news()
        if itens_news != None or itens_news != '':
            for news in itens_news:
                D = {}
                D['title'] = news.Title()
                D['text'] = news.Description()

                try:
                    D['image'] = news.getImageRelac().absolute_url() + '/image_mini'
                except:
                    try:
                        D['image'] = news.getImage().absolute_url() + '_mini'
                    except:
                        D['image'] = ''

                # D['target'] = news.getTarget()
                D['url'] = news.absolute_url()
                D['date'] = news.creation_date.strftime('%d/%m/%Y')
                D['author'] = news.getOwner().getUserName()
                # D['obj'] = news
                L.append(D)

        return L

    def getBanner(self):
        L = []
        obj = self.context
        itens_Banners = obj.getBanner()
        if itens_Banners != None or itens_Banners != '':
            for banner in itens_Banners:
                D = {}
                D['title'] = banner.Title()
                D['text'] = banner.Description()
                D['image'] = banner.absolute_url() + '/imagem_banner'
                D['target'] = banner.getTarget()
                D['url'] = banner.getLink()
                D['date'] = banner.creation_date.strftime('%d/%m/%Y')
                D['author'] = banner.getOwner().getUserName()
                # D['obj'] = banner
                L.append(D)

        return L


