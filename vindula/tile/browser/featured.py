# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class FeaturedView(BaseView):
    grok.name('featured-view')

    def cont_text(self, text, size=100):
        return len(text) > size
