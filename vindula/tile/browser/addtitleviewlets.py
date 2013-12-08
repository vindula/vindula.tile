# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IAboveContentBody #IBelowContentBody
from Products.CMFCore.utils import getToolByName

from zope.security import checkPermission

grok.context(Interface)
grok.templatedir('templates')

class AddTilesViewlet(grok.Viewlet):
	grok.name('vindula.tile.addtiles')
	grok.require('zope2.View')
	grok.viewletmanager(IAboveContentBody)

	list_tiles = ['TileAccordionContent',
				  # 'TileAccordionItem',
				  'TileBanner',
				  'TileBirthdays',
				  'TileFeatured',
				  'TileLabel',
				  'TileListagemHorizontal',
				  'TileListagemVertical',
				  'TileMacroList',
				  'TileMoreAccess',
				  'TileOrganogram',
				  'TilePoll',
				  'TileSimpleMacro',
				  'TileNewEmployee',
				  'TileFood',
				  'TileCalendar',
				  'TileTabularList',
				  'TileReferenceList']

	def get_types(self):
		context = self.get_context()
		portal_types = getToolByName(context, "portal_types")
		
		L = []
		for item in self.list_tiles:
			type_obj = portal_types[item]
			D = {}
			D['title'] = type_obj.title
			D['icone'] = '/%s' %(type_obj.getIcon())
			D['description'] = type_obj.description
			D['url_add'] = '%s/createObject?type_name=%s' %(context.absolute_url(),item)
			L.append(D)

		return L

	def get_context(self):
		context = self.context
		context_local = None
		if context.portal_type == 'OrganizationalStructure':
			default_value = context.get('home_principal')
			context_local = default_value or context.getLayout_content()

		elif context.portal_type == 'LayoutLoad':
			context_local = context.getObj_layout()

		if context_local:
			return context_local
		else:
			return context


	def isEnableViewlet(self):
		context = self.get_context()
		if context.portal_type == 'Layout' and\
			self.can_add_tile(context):
		   return True
		return False

	def isEnableLayout(self):
		context = self.get_context()
		if context.portal_type in ['VindulaFolder', 'Folder', 'OrganizationalStructure'] and\
			self.can_add_tile(context):
		   return True
		return False	


	def can_add_tile(self,obj_tile):
		return checkPermission('cmf.AddPortalContent', obj_tile)

