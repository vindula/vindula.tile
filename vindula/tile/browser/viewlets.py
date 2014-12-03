# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalHeader
from Products.CMFCore.utils import getToolByName


grok.context(Interface)
grok.templatedir('templates')

class BannerCompostViewlet(grok.Viewlet):
	grok.name('vindula.tile.bannercompost')
	grok.require('zope2.View')
	grok.viewletmanager(IPortalHeader)

	def check_context(self):
		if self.context.portal_type == 'LayoutLoad':
			return True
		return False


	def get_tile_banner(self):
		return None
		# context = self.context
		# obj_banner = context.getObj_banner()

		# return obj_banner

