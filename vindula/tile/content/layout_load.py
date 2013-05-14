# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.content import schemata, base

from vindula.tile.content.interfaces import ILayoutLoad

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

LayoutLoad_schema = schemata.ATContentTypeSchema.copy() + Schema((

    ReferenceField('obj_layout',
            multiValued=0,
            allowed_types=('Layout',),
            label=_(u"Layout"),
            relationship='obj_layout',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Layout"),
                description='Selecione o objeto layout .'
            ),
            required=True,
            # review_state = ('published', 'internal','external')
        ),


))

#Oculta o campo padrao 'description'
invisivel = {'view':'invisible','edit':'invisible',}

finalizeATCTSchema(LayoutLoad_schema, folderish=False)

class LayoutLoad(base.ATCTContent):
    """ Reserve Content for LayoutLoad"""
    security = ClassSecurityInfo()

    implements(ILayoutLoad)
    portal_type = 'LayoutLoad'
    _at_rename_after_creation = True
    schema = LayoutLoad_schema


registerType(LayoutLoad, PROJECTNAME)