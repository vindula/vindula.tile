# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileMacroList

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileMacroList_schema = BaseTile.schema.copy() + Schema((


    DataGridField('macros',
                searchable=True,
                columns=('title','page', 'macro'),
                allow_delete = True,
                allow_insert = True,
                allow_reorder = True,
                widget = DataGridWidget(label="Listagem de macros",
                                        label_msgid='vindula_tile_label_macros',
                                        description="Relacione, as listagem das macros com os titulo e das abas.",
                                        description_msgid='vindula_controlpanel_help_macros',
                                        columns= {
                                            "title" : Column(_(u"Titulo")),
                                            "page" : Column(_(u"Página")),
                                            "macro" : Column(_(u"Macro", default=u'page'))
                                        }),
                ),



))

finalizeATCTSchema(TileMacroList_schema, folderish=False)

class TileMacroList(BaseTile):
    """ Reserve Content for TileMacroList """
    security = ClassSecurityInfo()

    implements(ITileMacroList)
    portal_type = 'TileMacroList'
    _at_rename_after_creation = True
    schema = TileMacroList_schema

registerType(TileMacroList, PROJECTNAME)
