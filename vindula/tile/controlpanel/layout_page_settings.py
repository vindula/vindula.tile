# -*- coding: utf-8 -*-

from z3c.form import interfaces

from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.registry.browser import controlpanel

from vindula.tile import MessageFactory as _






class ILayoutPageSettings(Interface):
    """
    """

    colluns_blocked = schema.List(title=u"Colunas Bloqueadas",
                                    description=u"Selecione as colunas que serão Bloqueadas para a edição.",
                                    required=False,
                                    value_type=schema.Choice(vocabulary=SimpleVocabulary([SimpleTerm(value=u'direita', title=_(u'Direita')),
                                                                                          SimpleTerm(value=u'meio', title=_(u'Meio')),
                                                                                          SimpleTerm(value=u'esquerda', title=_(u'Esquerda')),
                                                                                        ]),
                                                            )

    )

    layout_available = schema.List(title=u"Layout Disponivel",
                                    description=u"Selecione os layouts disponiveis para o portão.",
                                    required=False,
                                    value_type=schema.Choice(vocabulary=SimpleVocabulary([SimpleTerm(value=u'1', title=_(u'1')),
                                                                                          SimpleTerm(value=u'2', title=_(u'2')),
                                                                                          SimpleTerm(value=u'3', title=_(u'3')),
                                                                                          SimpleTerm(value=u'4', title=_(u'4')),
                                                                                        ]),
                                                            )

    )


class LayoutPageSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ILayoutPageSettings
    label = u"Configuração do Layout"
    description = u""

    def updateFields(self):
        super(LayoutPageSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(LayoutPageSettingsEditForm, self).updateWidgets()


class LayoutPageSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
     form = LayoutPageSettingsEditForm
