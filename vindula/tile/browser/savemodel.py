# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView
from Products.CMFCore.utils import getToolByName

from vindula.myvindula import MessageFactory as _
from Products.statusmessages.interfaces import IStatusMessage

from zope.interface import Interface
from vindula.tile.config import ROOT_PATH
import os

grok.templatedir('templates')

class SaveModel(BaseView):
    grok.context(Interface)
    grok.name('savemodel-view')


    def render(self):
    	return '--OK--'

    def update(self):
		context = self.context
		path_zexp = ROOT_PATH + '/../../docs/zexp'
		
		f = os.path.join(path_zexp, '%s.%s' % (context.id, 'zexp'))
 		context._p_jar.exportFile(context._p_oid, f)

 		IStatusMessage(self.request).addStatusMessage(_(u'Modelo salvo com sucesso.'),"info")
		self.request.response.redirect(context.absolute_url())


class RemoveModel(BaseView):
	grok.context(Interface)
	grok.name('removemodel-view')


	def render(self):
		return '--OK--'

	def update(self):
		context = self.context
		form = self.request.form
		path_zexp = ROOT_PATH + '/../../docs/zexp'

		if 'id_model' in form.keys():
			id_model = form.get('id_model')

			f = os.path.join(path_zexp, id_model)
			os.remove(f)
		

	 	# 	IStatusMessage(self.request).addStatusMessage(_(u'Modelo remevido com sucesso.'),"info")
			# self.request.response.redirect(context.absolute_url())


