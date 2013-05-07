# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.tile.content.interfaces import ILayout

grok.templatedir('templates')

class LayoutView(BaseView):
    grok.context(ILayout)
    grok.name('layout-view')

    def getMacro(self, obj):
        macro = 'context/%s/macros/page' %(obj.getLayout())

        return macro