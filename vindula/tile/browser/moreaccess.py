# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.content.models.content import ModelsContent

grok.templatedir('templates')

class MoreAccessView(BaseView):
    grok.name('moreaccess-view')


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