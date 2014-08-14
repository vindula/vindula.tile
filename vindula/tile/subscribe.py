# -*- coding: utf-8 -*-
from five import grok
from vindula.tile.content.interfaces import IBaseTile,ILayout,ILayoutLoad

from zope.lifecycleevent.interfaces import IObjectCreatedEvent, IObjectModifiedEvent

def permission_title(context, tipo):
    permissao = ['Reader']
    id_grupo = 'AuthenticatedUsers'
    context.manage_setLocalRoles(id_grupo, permissao)
    print tipo


#---------Criação de um objeto - BLOCO
@grok.subscribe(IBaseTile, IObjectCreatedEvent)
def add_permission_bloco(context, event):
    permission_title(context,'ADD')

#---------Edição de um objeto - BLOCO
@grok.subscribe(IBaseTile, IObjectModifiedEvent)
def edit_permission_bloco(context, event):
    permission_title(context,'EDIT')


#---------Criação de um objeto - CAPA
@grok.subscribe(ILayout, IObjectCreatedEvent)
def add_permission_capa(context, event):
    permission_title(context,'ADD')

#---------Edição de um objeto - CAPA
@grok.subscribe(ILayout, IObjectModifiedEvent)
def edit_permission_capa(context, event):
    permission_title(context,'EDIT')


#---------Criação de um objeto - CARREGA CAPA
@grok.subscribe(ILayoutLoad, IObjectCreatedEvent)
def add_permission_carregacapa(context, event):
    permission_title(context,'ADD')

#---------Edição de um objeto - CARREGA CAPA
@grok.subscribe(ILayoutLoad, IObjectModifiedEvent)
def edit_permission_carregacapa(context, event):
    permission_title(context,'EDIT')
