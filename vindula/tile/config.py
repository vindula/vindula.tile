# -*- coding: utf-8 -*-
import os

try: # New CMF
    from Products.CMFCore.permissions import setDefaultRoles
except ImportError: # Old CMF
    from Products.CMFCore.CMFCorePermissions import setDefaultRoles

from vindula.tile import MessageFactory as _

PROJECTNAME = "vindula.tile"

try:
    from Products.CMFPlone.migrations import v2_1
except ImportError:
    HAS_PLONE21 = False
else:
    HAS_PLONE21 = True

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))

#ADD_CONTENT_PERMISSIONS = {
#    'Layout': 'vindula.tile: Add Layout',
#    'TileBanner': 'vindula.tile: Add TileBanner',
#    'TileListagemVertical': 'vindula.tile: Add TileListagemVertical',}

product_globals = globals()

def getVariableEnvironment(var):
    '''
        Método para

        @var = ZOPE_HOME, INSTANCE_HOME, ... é o valor da variável do sistema
        @return = Retorna o valor da variavel do sistema
    '''
    environ = os.environ
    return environ.get(var, None)

BUILDOUT_PATH = getVariableEnvironment('INSTANCE_HOME') + '/../../'
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

VOCABULARY_COLUNAS=[('6', _(u"50%")),
                    ('12', _(u"100%")),]

VOCABULARY_SORTED_ITENS=[
    ('getObjPositionInParent','Posições dos objetos na pasta'),
    ('created','Data de Criação'),
    ('effective','Data de Publicação'),
    ('modified','Data de Modificação')
]


LIST_PLONETYPES = ['Event','File','Image','Link','OrganizationalStructure','Servico','VindulaNews','VindulaStreaming','VindulaVideo']

LIST_TYPES_TILES = ['TileAccordionContent','TileBanner',# 'TileBannerCompost',
                    'TileBirthdays', 'TileCalendar', 'TileFeatured','TileFood',
                    'TileHowDo','TileInfoStructure','TileJobOffer','TileLabel',
                    'TileListServices','TileLibrary','TileListagemHorizontal',
                    'TileListagemVertical','TileLoadReference',
                    'TileMacroList','TileMoreAccess','TileMultimedia',
                    'TileNewEmployee','TileOrganogram','TilePoll',
                    'TileReferenceList','TileSimpleMacro','TileTabularList',
                    'TileTeam','TileHtml','TilePoiTracker']