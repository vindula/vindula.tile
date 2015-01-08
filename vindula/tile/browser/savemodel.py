# coding: utf-8
import os, json

from Products.statusmessages.interfaces import IStatusMessage
from five import grok
from plone.i18n.normalizer.interfaces import IIDNormalizer
from vindula.myvindula import MessageFactory as _
from zope.component import getUtility
from zope.interface import Interface

from vindula.tile.browser.baseview import BaseView
from vindula.tile.config import ROOT_PATH, BUILDOUT_PATH


grok.templatedir('templates')

class ErrorSavingModels(Exception):
     pass

class SaveModel(BaseView):
    grok.context(Interface)
    grok.name('savemodel-view')

    def update(self):
        # import pdb; pdb.set_trace()
        form = self.request.form

        if form.get('save_model', False):
            context = self.context

            try:
                if form.get('name_model', False):
                    title_model = form.get('name_model')
                    normalizer = getUtility(IIDNormalizer)
                    id_model = normalizer.normalize(title_model)

                    path_zexp = BUILDOUT_PATH + 'capas_customizadas/'

                    if os.path.exists(path_zexp+id_model):
                        raise ErrorSavingModels('O modelo %s já existe' % title_model)
                    else:
                        path_zexp = path_zexp + id_model
                        os.makedirs(path_zexp)

                    f = os.path.join(path_zexp, '%s.%s' % (context.id, 'zexp'))
                    context._p_jar.exportFile(context._p_oid, f)

                    title_file = open(path_zexp+'/title_model', 'w')
                    title_file.write(title_model)

                    IStatusMessage(self.request).addStatusMessage(_(u'Modelo salvo com sucesso.'),"info")
                    self.request.response.redirect(context.absolute_url())

                else:
                    raise ErrorSavingModels('O nome do modelo é obrigatório')

            except ErrorSavingModels as e:
                IStatusMessage(self.request).addStatusMessage(e.message,"info")


class RemoveModel(BaseView):
    grok.context(Interface)
    grok.name('removemodel-view')

    retorno = {}

    def render(self):
        self.request.response.setHeader("Content-type","application/json")
        self.request.response.setHeader("charset", "UTF-8")
        return json.dumps(self.retorno,ensure_ascii=False)

    def update(self):
        form = self.request.form
        path_zexp = ROOT_PATH + '/../../docs/zexp'

        if 'id_model' in form.keys():
            id_model = form.get('id_model')

            f = os.path.join(path_zexp, id_model)
            os.remove(f)
            self.retorno['status'] = True
        
        else:
            self.retorno['status'] = False


