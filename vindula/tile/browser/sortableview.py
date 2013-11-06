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

		man_list = []
		even_list = []
		odd_list = []

		for i in list_tiles:

			if 'even|' in i:
				even_list.append(i)
			elif 'odd|' in i:
				odd_list.append(i)
		
		for i in list_tiles:

			if not "even|" in i and not "odd|" in i:
				man_list.append(i)
			else:
				try:
					i_even = even_list.pop(0)
					i_odd = odd_list.pop(0)
					man_list.append(i_even.replace('even|',''))
					man_list.append(i_odd.replace('odd|',''))

				except IndexError: pass

		context = self.reference_catalog.lookupObject(context_UID)
		if context:
			for ordem, id_tile in enumerate(man_list):
				context.moveObjectToPosition(id_tile,ordem)

			context.plone_utils.reindexOnReorder(context)
			self.retorno['response'] = 'Objetos atualizados...'
		else:
			self.retorno['response'] = 'Erro ao obter o contexto dos Tiles'


	def render(self):
		self.request.response.setHeader("Content-type","application/json")
		self.request.response.setHeader("charset", "UTF-8")
		return json.dumps(self.retorno,ensure_ascii=False)