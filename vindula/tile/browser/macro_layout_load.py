# -*- coding: utf-8 -*-
from five import grok
from zope.i18nmessageid import MessageFactory

from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class MacroLayoutLoadView(BaseView):
    grok.name('macro_layout_load')