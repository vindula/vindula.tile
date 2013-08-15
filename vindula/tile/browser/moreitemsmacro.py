# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class MoreItemsMacro(BaseView):
    grok.name('more-items-macro')