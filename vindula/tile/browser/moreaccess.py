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


        if self.context.getKind() == 'two_columns':
            return result
        else:
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

        itens = self.portal_catalog(portal_type = portal_type,
                                    # review_state = states,
                                    path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                    sort_on='effective',
                                    sort_order='descending',
                                    )

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
            obj = item.getObject()
            title = self.getTitle(obj)
            try:
                letras[title[0]].append(item)
            except KeyError:
                pass


        return letras