# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from plone.app.uuid.utils import uuidToObject

import json

grok.templatedir('templates')

class SortableView(BaseView):
	grok.name('sortable-view')

	retorno = {}

	def split_tile(self,string_tile):
		text = string_tile.split('|')
		# ID , UID, CONTEXTO
		try:
			return text[0], text[1], text[2]
		except:
			return '','',''


	def update(self):
		self.retorno = {}
		form = self.request.form
		json_data = form.get('data','')
		data = json.loads(json_data)
		context_UID = data.get('context_UID','')
		list_tiles = data.get('list_tiles', [])

		man_list = []

		for linha_tile in list_tiles:
			for columns_tile in linha_tile:
				man_list.append(columns_tile)

		context_global = uuidToObject(context_UID)
	
		if context_global:
			for ordem, id_tile in enumerate(man_list):
				title, uid, context_uid = self.split_tile(id_tile)

				if context_uid == context_UID:
					context_global.moveObjectToPosition(title,ordem)

				else:
					context_oring = uuidToObject(context_uid)

					if context_oring:
						clipboard = context_oring.manage_cutObjects([title])
						context_global.manage_pasteObjects(clipboard)
						context_global.moveObjectToPosition(title,ordem)

			context_global.plone_utils.reindexOnReorder(context_global)

			self.retorno['response'] = {'msg':'Objetos atualizados...', 'uid':context_UID}
		else:
			self.retorno['response'] = {'msg':'Erro ao obter o contexto dos Tiles', 'uid':''}


	def render(self):
		self.request.response.setHeader("Content-type","application/json")
		self.request.response.setHeader("charset", "UTF-8")
		return json.dumps(self.retorno,ensure_ascii=False)