# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *

from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.content import schemata, base

from vindula.tile.content.interfaces import ILayoutLoad
from plone.contentrules.engine.interfaces import IRuleAssignable

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget

LayoutLoad_schema = schemata.ATContentTypeSchema.copy() + Schema((

    ReferenceField('obj_layout',
            multiValued=0,
            allowed_types=('Layout',),
            label=_(u"Layout - Coluna A"),
            relationship='obj_layout',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Layout - Coluna A"),
                description='Selecione o objeto layout .'
            ),
            required=True,
            # review_state = ('published', 'internal','external')
        ),

        ReferenceField('obj_layout_B',
            multiValued=0,
            allowed_types=('Layout',),
            label=_(u"Layout - Coluna B"),
            relationship='obj_layout_B',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Layout - Coluna B"),
                description='Selecione o objeto layout para a coluna B, (Usado no layout Classico).'
            ),
            required=False,
            # review_state = ('published', 'internal','external')
        ),

        ReferenceField('obj_layout_C',
            multiValued=0,
            allowed_types=('Layout',),
            label=_(u"Layout - Coluna C"),
            relationship='obj_layout_C',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Layout - Coluna C"),
                description='Selecione o objeto layout para a coluna C, (Usado no layout Classico).'
            ),
            required=False,
            # review_state = ('published', 'internal','external')
        ),


        ReferenceField('obj_layout_topo',
            multiValued=0,
            allowed_types=('Layout',),
            label=_(u"Layout - Topo"),
            relationship='obj_layout_topo',
            widget=VindulaReferenceSelectionWidget(
                label=_(u"Layout - Topo"),
                description='Selecione o objeto layout para o Topo, (Usado no layout Smart).'
            ),
            required=False,
            # review_state = ('published', 'internal','external')
        ),


        StringField(
            name='type_layouts',
            widget=SelectionWidget(
                label=_(u"Tipo de Layout"),
                description=_(u"Selecione qual o tipo de layout que deseja utilizar."),
                label_msgid='vindula_tile_label_type_layouts',
                description_msgid='vindula_tile_help_type_layouts',
                i18n_domain='vindula_tile',
                format = 'select',
             ),
             vocabulary=[("padrao",_(u"Layout com uma coluna de capa")),
                        ("classico", _(u"Layout com três colunas de capa")),
                        ("smart", _(u"Layout com três colunas de capa e uma no topo")),],
             default='padrao',
             required=True,
         ),

        # ReferenceField('obj_banner',
        #     multiValued=0,
        #     allowed_types=('TileBannerCompost',),
        #     label=_(u"Banner Superior"),
        #     relationship='obj_banner',
        #     widget=VindulaReferenceSelectionWidget(
        #         label=_(u"Banner Superior"),
        #         description='Selecione o bloco de Banner Composto, utilizado na área supeio do portal .'
        #     ),
        #     required=False,
        #     # review_state = ('published', 'internal','external')
        # ),

))

LayoutLoad_schema.changeSchemataForField('obj_banner', 'Banner')

#Oculta o campo padrao 'description'
invisivel = {'view':'invisible','edit':'invisible',}

finalizeATCTSchema(LayoutLoad_schema, folderish=False)

class LayoutLoad(base.ATCTContent):
    """ Reserve Content for LayoutLoad"""
    security = ClassSecurityInfo()

    implements(ILayoutLoad,IRuleAssignable)
    portal_type = 'LayoutLoad'
    _at_rename_after_creation = True
    schema = LayoutLoad_schema


registerType(LayoutLoad, PROJECTNAME)