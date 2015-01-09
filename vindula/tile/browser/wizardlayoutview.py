# coding: utf-8
import os

from five import grok
from zope.interface import Interface

from vindula.tile.browser.baseview import BaseView
from vindula.tile.config import ROOT_PATH, BUILDOUT_PATH


grok.templatedir('templates')

class WizardLayout(BaseView):
    grok.context(Interface)
    grok.name('wizard-view')

    def get_list_modelos(self):
        # black_list = ['capa-principal.zexp','capa-esquerda.zexp','capa-direita.zexp']

        L = [{'name':'Layout Padrão','id':'2','can_delete':False, 'path_img':'++resource++vindula.tile/images/miniatura-1.png'},
             # {'name':'Layout Classico','id':'1','can_delete':False, 'path_img':'++resource++vindula.tile/images/miniatura-2.png'},
             # {'name':'Layout Smart','id':'3','can_delete':False, 'path_img':'++resource++vindula.tile/images/miniatura-3.png'},
            ]   
        
        path_zexp = BUILDOUT_PATH + 'capas_customizadas/'

        for folder in os.listdir(path_zexp):
            items = os.listdir(path_zexp + folder)

            if 'title_model' in items:
                file_title = open(path_zexp + folder + '/title_model')
                txt = file_title.read()
                file_title.close()

            L.append({'name':txt, 'id':folder,'can_delete':True, 'path_img':'++resource++vindula.tile/images/miniatura-4.png'})

        return L


    def update(self):
        form = self.request.form

        if 'submitted' in form.keys():
            layout = form.get('layout','')
            # import pdb; pdb.set_trace()

            context = self.context

            if context.portal_type in ['VindulaFolder', 'Folder', 'OrganizationalStructure']:

                path_zexp = ROOT_PATH + '/../../docs/zexp/'
               
                if layout == '1':
                    context._importObjectFromFile(filepath=path_zexp+'capa-principal.zexp')
                    context._importObjectFromFile(filepath=path_zexp+'capa-esquerda.zexp')                
                    context._importObjectFromFile(filepath=path_zexp+'capa-direita.zexp')

                elif layout == '2':
                    context._importObjectFromFile(filepath=path_zexp+'capa-principal.zexp')

                else:
                    #Caso for layout customizado
                    path_zexp = BUILDOUT_PATH + 'capas_customizadas/' + layout
                    items = os.listdir(path_zexp)

                    for item in items:
                        if '.zexp' in item:
                            context._importObjectFromFile(filepath=path_zexp + '/' + item)

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