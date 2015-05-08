# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View

from vindula.tile.browser.baseview import BaseView

from five import grok
from datetime import datetime
from dateutil.tz import tzlocal

grok.templatedir('templates')

class BannerView(BaseView):
    grok.name('banner-view')


    def get_list_banners(self):
        obj = self.context
        banners = obj.getImageBanner() or []
        banners_admin = obj.getImageBanner_admin() or []

        mergedlist = []
        mergedlist.extend(banners_admin)
        mergedlist.extend(banners)
        return mergedlist

    def getTileBanner(self):
        obj = self.context
        date_now = datetime.now(tzlocal())
        L = []
        
        banners = self.get_list_banners()
        for banner in banners:
            D = {}
            D['title'] = banner.Title()
            D['text'] = banner.Description()
            # D['image'] = banner.absolute_url() + '/imagem_banner_large'
            D['image'] = banner.absolute_url() + '/imagem_banner'
            D['target'] = banner.getTarget()
            D['url'] = banner.getLink()
            D['timeTransitionBanner'] = obj.getTimeTransitionBanner()
            if obj.activeDate == True:
                D['date'] = banner.creation_date.strftime('%d/%m/%Y')
            if obj.activeAuthor == True:
                D['author'] = banner.getOwner().getUserName()
            #TODO: Criar método para buscar o nome da Unidade
            if obj.activeUnit == True:
                title_structure = ''
                structure = self.getStructure(obj)
                if structure:
                    title_structure = structure.Title()
                D['unit']= title_structure

            D['obj'] = banner
            
            try:
                data_public = banner.getEffectiveDate().asdatetime()
            except AttributeError:
                #CASO ESSE OBJETO NÃO TENHA DATA DE EFETIVAÇÃO
                data_public = date_now

            try:
                data_expir = banner.getExpirationDate().asdatetime()
            except AttributeError:
                #CASO ESSE OBJETO NÃO TENHA DATA DE EXPIRAÇÃO
                data_expir = date_now

            if date_now >= data_public and date_now <= data_expir:
                L.append(D)
        
        return L

    def getStructure(self, context):
        if context.portal_type == 'OrganizationalStructure':
            return context
        if context.portal_type == 'Plone Site':
            return None
        else:
            return self.getStructure(context.aq_parent)
        


