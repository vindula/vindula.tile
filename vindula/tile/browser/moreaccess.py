# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.content.models.content import ModelsContent

import string

grok.templatedir('templates')

class MoreAccessView(BaseView):
    grok.name('moreaccess-view')
    first_active = True

    def getItens(self):
        portal_type = self.context.getObject_type()
        cont = self.context.getNumb_items()

        result = self.list_files(portal_type)

        return result[:cont]

    def list_files(self, portal_type):
        list_files = []
        rs = True

        query = {'portal_type': portal_type}
        if 'File' in portal_type:
            rs=False

        result = ModelsContent().search_catalog_by_access(context=self.context,
                                                          rs=rs,
                                                          **query)
        return result

    def list_more(self):
        context = self.context
        path = context.portal_url.getPortalObject()

        portal_type = context.getObject_type_more()

        if portal_type == 'File':
            #Quando portal_type == File nao tem review_state
            itens = self.portal_catalog(portal_type = portal_type,
                                        #review_state = states,
                                        path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                        sort_on='effective',
                                        sort_order='descending',
                                        )
        else:
            itens = self.portal_catalog(portal_type = portal_type,
                                        review_state = ['published'],
                                        path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                        sort_on='effective',
                                        sort_order='descending',
                                        )
            #Forcar itens = published
            itens = [i for i in itens if i.review_state == 'published']


        return itens

    def is_first_active(self,has_content):
        if not has_content and self.first_active:
            self.first_active = False
            return 'active'
        else:
            return ''


    def getTitle(self,obj):
        str = ''
        if hasattr(obj, 'getSiglaunidade'):
            str = obj.getSiglaunidade().upper()

        if not str:
            str = obj.Title().upper()

        # print str
        return str

    def alphabet(self):
        #ABCDEFGHIJKLMNOPQRSTUVWYXZ
        L = []
        for i in string.ascii_uppercase:
            L.append(i)

        return L

    def constructor(self):
        letras = {}
        for i in self.alphabet():
            letras[i] = []

        for item in self.list_more():            
            #Todo: remover isso, colocado apenas para teste            
            try:
                obj = item.getObject()
                title = self.getTitle(obj)
                if len(title) > 0:
                    letras[title[0]].append(item)
            except KeyError:
                pass


        return letras
