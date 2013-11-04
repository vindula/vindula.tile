# -*- coding: utf-8 -*-
""" Liberiun Technologies Sistemas de Informação Ltda. """
""" Produto:                 """

from zope.interface import implements
from zope.formlib import form
from zope import schema

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget, UberMultiSelectionWidget

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from vindula.tile import MessageFactory as _

from zope.security import checkPermission

class ITileLoads(IPortletDataProvider):

    """A portlet
    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    tiles_list = schema.Choice(title=_(u"Layout "),
                               description=_(u"Selecione o Layout para renderização dos tiles."),
                               required=True,
                               source=SearchableTextSourceBinder({'portal_type': 'Layout'},
                                                                 default_query='path:')
                              )

# ('PoiTracker','TileBanner','TileFeatured','TileLabel','TileListagemHorizontal','TileListagemVertical', 'TileMacroList','TileMoreAccess','TileSimpleMacro')


class Assignment(base.Assignment):
    """Portlet assignment.
    This is what is actually managed through the portlets UI and associated
    with columns.
    """
    implements(ITileLoads)
    title = _(u'Vindula Carrega Tile')

    def __init__(self, tiles_list=[],):

        self.tiles_list = tiles_list


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """
    render = ViewPageTemplateFile('tileloads.pt')

    @property
    def available(self):
        return True

    def getTiles(self):
        context = self.context
        portal = context.portal_url.getPortalObject()
        catalog = portal.portal_catalog
        portal_path = '/'.join(portal.getPhysicalPath())

        data = self.data
        rid = catalog.getrid(portal_path + data.tiles_list)
        brain = catalog._catalog[rid]
        obj = brain.getObject()
        return obj.values()


    def getScripts_js(self):
        scripts_js = []

        #Coleta dos Script js dos tiles
        tiles = self.getTiles()

        for tile in tiles:
            if hasattr(tile, 'scripts_js'):
                for i in tile.scripts_js:
                    if not i in scripts_js:
                        scripts_js.append(i)

        return scripts_js


    def getMacro(self, obj):
        macro = 'context/%s/macros/page' %(obj.getLayout())

        return macro

    def can_manage_tile(self,obj_tile):
        return checkPermission('cmf.ModifyPortalContent', obj_tile)


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """

    form_fields = form.Fields(ITileLoads)
    form_fields['tiles_list'].custom_widget = UberSelectionWidget

    def create(self, data):
       return Assignment(**data)

class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(ITileLoads)
    form_fields['tiles_list'].custom_widget = UberSelectionWidget
