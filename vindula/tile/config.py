# -*- coding: utf-8 -*-
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

import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


VOCABULARY_COLUNAS=[('4',_(u"4 Colunas")),
                    ('6', _(u"6 Colunas")),
                    ('12', _(u"12 Colunas")),
                    ]

VOCABULARY_SORTED_ITENS=[
    ('getObjPositionInParent','Posições dos objetos na pasta'),
    ('created','Data de Criação'),
    ('effective','Data de Publicação'),
    ('modified','Data de Modificação')
]