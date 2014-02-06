# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView
from Products.CMFCore.utils import getToolByName

from zope.interface import Interface
from vindula.tile.config import ROOT_PATH

import os

grok.templatedir('templates')

class WizardLayout(BaseView):
    grok.context(Interface)
    grok.name('wizard-view')

    def get_list_modelos(self):
        black_list = ['capa-principal.zexp','capa-esquerda.zexp','capa-direita.zexp']

        L = [{'name':'Layout Padrão','id':'2','can_delete':False},
             {'name':'Layout Classico','id':'1','can_delete':False},
            ]   
        
        path_zexp = ROOT_PATH + '/../../docs/zexp'

        for iten in os.listdir(path_zexp):
            if not iten in black_list:
                name = iten.replace('.zexp','')
                txt = ''
                for t in name.replace('-','|').replace('_','|').split('|'):
                    txt += '%s ' %(t.title())

                L.append({'name':txt,'id':iten,'can_delete':True})

        return L


    def update(self):
        form = self.request.form

        if 'submitted' in form.keys():
            layout = form.get('layout','')

            context = self.context

            if context.portal_type in ['VindulaFolder', 'Folder', 'OrganizationalStructure']:

                path_zexp = ROOT_PATH + '/../../docs/zexp'
               

                if layout == '1':
                    context._importObjectFromFile(filepath=path_zexp+'capa-principal.zexp')
                    context._importObjectFromFile(filepath=path_zexp+'capa-esquerda.zexp')                
                    context._importObjectFromFile(filepath=path_zexp+'capa-direita.zexp')

                elif layout == '2':
                    context._importObjectFromFile(filepath=path_zexp+'capa-principal.zexp')

                else:
                    context._importObjectFromFile(filepath=path_zexp+layout)

                # portal_workflow = getToolByName(context, 'portal_workflow')

                # try:portal_workflow.doActionFor(context, 'publish')
                # except:portal_workflow.doActionFor(context, 'publish_internally')

                if 'defaut_view' in form.keys():
                    obj_layout = context['capa-principal']

                    if layout == '1':
                        obj_layout_B = context['capa-esquerda']
                        obj_layout_C = context['capa-direita']

                        context.invokeFactory('LayoutLoad', 
                                          id='layout_default_view', 
                                          title="Layout Padrão do Contexto", 
                                          obj_layout=obj_layout,
                                          obj_layout_B=obj_layout_B,
                                          obj_layout_C=obj_layout_C,
                                          type_layouts='classico')

                    else:

                        context.invokeFactory('LayoutLoad', 
                                              id='layout_default_view', 
                                              title="Layout Padrão do Contexto", 
                                              obj_layout=obj_layout)

                    context.setDefaultPage('layout_default_view')

                self.request.response.redirect(context.absolute_url(), lock=True)
