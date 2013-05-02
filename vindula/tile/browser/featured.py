# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class FeaturedView(BaseView):
    grok.name('featured-view')

    def limitTextSize(self, text, size=100):
        if len(text) > size:
            i = size
            try:
                while text[i] != " ":
                    i += 1
                return text[:i]+'...'
            except IndexError:
                return text
        else:
            return text

    def cont_text(self, text, size=100):
        return len(text) > size
