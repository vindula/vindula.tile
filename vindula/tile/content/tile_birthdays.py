# coding=utf-8
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from vindula.controlpanel.browser.at.widget import VindulaReferenceSelectionWidget
from vindula.tile.content.interfaces import ITileBirthdays
from vindula.tile.content.tile_schemaBase import BaseTile

from vindula.tile import MessageFactory as _
from vindula.tile.config import *

list_types_choice = [('1','Aniversariantes do dia'), ('7','Aniversariantes da semana'),  ('30','Aniversariantes do mês'), ('prox', 'Próximos Aniversariantes')]

TileBirthdays_schema = BaseTile.schema.copy() + Schema((


    IntegerField(
        name='numb_items',
        widget = IntegerWidget(
            label = 'Quantidade',
            description='Quantidade maxima de items.',
        ),
        default=5,
    ),

    ReferenceField('structures',
        multiValued=0,
        allowed_types=('OrganizationalStructure',),
        relationship='structures',
        widget=VindulaReferenceSelectionWidget(
            typeview='list',
            label=_(u"Escolha uma Unidade Organizacional"),
            description=_(u"Selecione uma Unidade Organizacional. "
                          u"Esta escolha fará com so apresente usuários desta Unidade Organizacional"),

            ),
        required=False
    ),

    StringField(
        name='type_search',
        widget=SelectionWidget(
            label=_(u"Tipo do filtro"),
            description=_(u"Selecione o filtro que será usado no portlet."),
            label_msgid='vindula_tile_label_type_search',
            description_msgid='vindula_tile_help_type_search',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=list_types_choice,
        default="prox",
        required=True,
    ),

    StringField(
        name='type_search_list',
        widget=SelectionWidget(
            label=_(u"Tipo de filtro para a listagem"),
            description=_(u"Selecione o fitro que sera usado na lista de aniversariantes."),
            label_msgid='vindula_tile_label_type_search_list',
            description_msgid='vindula_tile_help_type_search_list',
            i18n_domain='vindula_tile',
            format='select',
        ),
        vocabulary=list_types_choice,
        default="prox",
        required=True,
    ),

    TextField(
            name='principal_user',
            widget=StringWidget(
                label=_(u"Destaque do aniversariante"),
                description=_(u"Adicione o campo com a informação princial do aniversariante como\
                                'name' para Nome ou 'nickname' para Apelido ou outros."),
                label_msgid='vindula_tile_label_principal_user',
                description_msgid='vindula_tile_help_principal_user',
            ),
            default = u'name',
            required=True,
    ),

    TextField(
        name='details_user',
        widget=TextAreaWidget(
            label="Details",
            description="Adicione detalhes sobre o aniversariante como Empresa, Matricula e outros. \
                         Adicione um campo por linha, no formato [Label] | [Campo].",
            rows="10",
            label_msgid='Poi_label_details_user',
            description_msgid='Poi_help_details_user',
            i18n_domain='vindula_tile',
        ),
        default=u'[] | [departamento]',
        required=True,
    ),
    
    BooleanField(
        name='show_structure',
        widget=BooleanWidget(
            label="Mostrar unidade principal",
            description='Se selecionado mostrar a unidade principal do usuário no bloco de aniversariantes.',
        ),
    ),

))


finalizeATCTSchema(TileBirthdays_schema, folderish=False)

class TileBirthdays(BaseTile):
    """ Reserve Content for TileBirthdays"""
    security = ClassSecurityInfo()

    implements(ITileBirthdays)
    portal_type = 'TileBirthdays'
    _at_rename_after_creation = True
    schema = TileBirthdays_schema

    #tamanho do tile
    columns = 6

registerType(TileBirthdays, PROJECTNAME)