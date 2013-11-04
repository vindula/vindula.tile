# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

import json

grok.templatedir('templates')

class SortableView(BaseView):
	grok.name('sortable-view')

	retorno = {}

	def update(self):
		self.retorno = {}
		form = self.request.form
		context_UID = form.get('context_UID','')
		list_tiles = form.get('list_tiles[]', [])

		context = self.reference_catalog.lookupObject(context_UID)

		for ordem, id_tile in enumerate(list_tiles):
			context.moveObjectToPosition(id_tile,ordem)

		self.retorno['response'] = 'Objetos atualizados...'
		context.plone_utils.reindexOnReorder(context)


	def render(self):
		self.request.response.setHeader("Content-type","application/json")
		self.request.response.setHeader("charset", "UTF-8")
		print self.retorno
		return json.dumps(self.retorno,ensure_ascii=False)