# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.tile.content.interfaces import ILayoutLoad

grok.templatedir('templates')


class LoadLayoutView(BaseView):
    grok.context(ILayoutLoad)
    grok.name('layoutload-view')



