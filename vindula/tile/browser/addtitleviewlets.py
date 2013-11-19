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

		context = self.context
		if context.portal_type == 'LayoutLoad':
			context = context.getObj_layout()

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

	def isEnableViewlet(self):
		context = self.context
		if (context.portal_type == 'LayoutLoad' or\
		   context.portal_type == 'layout') and self.can_add_tile(context):
		   return True
		return False


	def can_add_tile(self,obj_tile):
		return checkPermission('cmf.AddPortalContent', obj_tile)

