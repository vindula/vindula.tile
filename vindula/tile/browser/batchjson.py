# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView


import json

grok.templatedir('templates')

class BatchJsonView(BaseView):
    grok.name('batchjson-view')

    retorno = []

    def render(self):
        self.request.response.setHeader("Content-type","application/json")
        self.request.response.setHeader("charset", "UTF-8")

        return json.dumps(self.retorno,ensure_ascii=False)


    def update(self):
        context = self.context
        layout = context.getLayout()
        form = self.rquest.form

        dict_methods = form.get('methods',{})


        title_view = context.restrictedtraverse(layout, None)
        if title_view:

            for item in title_view.getItens():
                D = {}
                for method in dict_methods.keys():
                    attr = dict_methods.get(method)

                    try:
                        D[method] = getattr(item, attr)()

                    except AttributeError:
                        D[method] = ''

                self.retorno.append(D)





