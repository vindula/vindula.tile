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
		context_UID = form.get('context_UID','')
		list_tiles = form.get('list_tiles[]', [])
		# list_uids = form.get('list_uids[]', [])
		# list_content = form.get('list_content[]', [])
		
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

				try:i_even = even_list.pop(0)
				except IndexError: i_even = None

				try:i_odd = odd_list.pop(0)
				except IndexError: i_odd = None				

				if i_even:
					man_list.append(i_even.replace('even|',''))
				if i_odd:
					man_list.append(i_odd.replace('odd|',''))

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