# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class HowDoView(BaseView):
    grok.name('howdo-view')

    def getItens(self):
        context = self.context
        numbers = context.getNumItems()
        types = context.getObjectType()
        subjects = context.getSubjects()
        

#        path = context.getPath()
#        if not path:
        path = context.portal_url.getPortalObject()

        itens = self.portal_catalog(portal_type = types,
                                    # review_state = states,
                                    path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                    Subject = subjects,
                                    sort_on='effective',
                                    sort_order='descending',
                                    )

        return itens[:numbers]