# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from plone.app.folder.folder import ATFolder

from vindula.tile.content.interfaces import ITileAccordionContent
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

TileAccordionContent_schema = ATFolder.schema.copy() + BaseTile.schema.copy() + Schema((

    BooleanField(
        name='activ_recurcividade',
        default=False,
        widget=BooleanWidget(
            label="Ativar Recursividade",
            description='Se selecionado, ativa a opção de recursividade do portlet em níveis inferiores.',
        ),
        required=False,
        schemata = 'settings'
    ),

    BooleanField(
        name='bloquea_portlet',
        default=False,
        widget=BooleanWidget(
            label="Bloquear Vindula Portlets dos níveis superiores",
            description='Se selecionado, irá bloquear todos os portlets dos níveis superiores do portal.(Cautela para usar esta opção)',
        ),
        required=False,
        schemata = 'settings'
    ),
    
    BooleanField(
        name='load_open',
        default=False,
        widget=BooleanWidget(
            label="Carregar os itens sempre abertos",
            description="Selecione esta opção caso queira que os itens do accordion carreguem sempre abertos.",
        ),
        required=False,
        schemata = 'settings'
    ),
))

finalizeATCTSchema(TileAccordionContent_schema, folderish=True)

class TileAccordionContent(ATFolder, BaseTile):
    """ Reserve Content for TileAccordionContent """
    security = ClassSecurityInfo()

    implements(ITileAccordionContent)
    portal_type = 'TileAccordionContent'
    _at_rename_after_creation = True
    schema = TileAccordionContent_schema

    #tamanho do tile
    columns = 6

    #Scripts js
    scripts_js = ['tile-accordion.js']

registerType(TileAccordionContent, PROJECTNAME)
