# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.tile.content.interfaces import ITilePoll
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

from Products.CMFPlone.utils import safe_unicode
from Products.CMFCore.utils import getToolByName

TilePoll_schema = BaseTile.schema.copy() + Schema((


    StringField(
        name='selection_mode',
        widget=SelectionWidget(
            label=_(u"Enquete"),
            description=_(u"Selecione na lista abaixo a enquete desejada."),
            label_msgid='vindula_tile_label_selection_mode',
            description_msgid='vindula_tile_help_selection_mode',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary='voc_list_poll',
        required=True,
    ),


    IntegerField(
        name='number_of_polls',
        widget = IntegerWidget(
            label = 'Número de enquetes no portlet de enquete  ',
            description='Selecione o número de enquetes que serão apresentadas na caixa de enquete.\
                         O valor mínimo é 1. Se você informar 0, a caixa de enquete não será mostrada.',
        ),
        default=5,
    ),


))


finalizeATCTSchema(TilePoll_schema, folderish=False)

class TilePoll(BaseTile):
    """ Reserve Content for TilePoll"""
    security = ClassSecurityInfo()

    implements(ITilePoll)
    portal_type = 'TilePoll'
    _at_rename_after_creation = True
    schema = TilePoll_schema

    #tamanho do tile
    columns = 6

    def voc_list_poll(self):

        context = self
        portal_catalog = getToolByName(context, 'portal_catalog')

        # Basic options
        voc  = [('hidden', u'Oculta'),
                ('newest', u"Enquete mais nova"),
                ('branch', u"Primeira enquete na seção"),
                ('subbranches', u"Primeira enquete na seção e nas sub-seções")
            ]


        # Adding existing polls
        brains = portal_catalog.unrestrictedSearchResults(meta_type='PlonePopoll')
        for brain in brains: # Brains
            poll = brain.getObject()
            path = '/'.join(poll.getPhysicalPath())
            title = "%s (%s)" % (safe_unicode(brain.Title), safe_unicode(path))

            voc.append((poll.UID(), title))

        return voc



registerType(TilePoll, PROJECTNAME)