# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from collective.referencedatagridfield import ReferenceDataGridField, ReferenceDataGridWidget

from vindula.tile.content.tile_schemaBase import BaseTile
from vindula.tile.content.interfaces import ITileReferenceList

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileReferenceList_schema = BaseTile.schema.copy() + Schema((
    
    ReferenceDataGridField('reference_list',
        schemata='default',
        relationship="demo_relation",
        widget = ReferenceDataGridWidget(
            label = "Listagem de tiles",
            visible = {'edit' : 'visible', 'view' : 'visible'}
        )
    ),
        
#    ReferenceDataGridField('reference_list',
#                searchable=True,
#                columns=('title','page', 'macro'),
#                allow_delete = True,
#                allow_insert = True,
#                allow_reorder = True,
#                relationship="reference_list",
#                widget = ReferenceDataGridWidget(
#                    label = "Listagem de tiles",
#                    label_msgid='vindula_tile_reference',
#                    description="Relacione as listagem dos tiles referenciados com os título e das abas.",
#                    description_msgid='vindula_tile_reference',
#                    visible = {'edit' : 'visible', 'view' : 'visible'}
#                ),
#                widget = DataGridWidget(label="Listagem de macros",
#                                        label_msgid='vindula_tile_label_macros',
#                                        description="Relacione, as listagem das macros com os titulo e das abas.",
#                                        description_msgid='vindula_controlpanel_help_macros',
#                                        columns= {
#                                            "title" : Column(_(u"Titulo")),
#                                            "page" : Column(_(u"Página")),
#                                            "macro" : Column(_(u"Macro"),default='page')
#                                        }),

))

finalizeATCTSchema(TileReferenceList_schema, folderish=False)

class TileReferenceList(BaseTile):
    """ Reserve Content for TileReferenceList """
    security = ClassSecurityInfo()

    implements(ITileReferenceList)
    meta_type = portal_type = archetype_name = 'TileReferenceList'
    _at_rename_after_creation = True
    schema = TileReferenceList_schema

    #tamanho do tile
    columns = 12

registerType(TileReferenceList, PROJECTNAME)
