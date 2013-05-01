# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class SimpleMacroView(BaseView):
    grok.name('simplemacro-view')

    def getMacro(self):
        page = self.context.getPage()
        macro = self.context.getMacro()
        if page:
            return 'context/'+page+'/macros/'+macro
        else:
            return None