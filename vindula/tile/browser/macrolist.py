# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class MacroListView(BaseView):
    grok.name('macrolist-view')

    def get_macros(self):
        macros = self.context.getList_macros()
        L = []
        if macros:
            for macro in macros:
                L.append({'title':macro.get('title',''),
                          'macro': 'context/%s/macros/%s'%(macro.get('page',''),macro.get('macro',''))
                        })

        return L





