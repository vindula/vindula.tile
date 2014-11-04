# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class RedirectURLView(BaseView):
    grok.name('r')


    def get_url(self):
        return self.request.form.get('url','')