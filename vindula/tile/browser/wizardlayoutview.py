# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView
from Products.CMFCore.utils import getToolByName

from zope.interface import Interface
from vindula.tile.config import ROOT_PATH

grok.templatedir('templates')

class WizardLayout(BaseView):
    grok.context(Interface)
    grok.name('wizard-view')


    def update(self):
        form = self.request.form

        if 'submitted' in form.keys():
            layout = form.get('layout','')

            context = self.context

            if context.portal_type in ['VindulaFolder', 'Folder', 'OrganizationalStructure']:

                path_zexp = ROOT_PATH + '/../../docs/'
                context._importObjectFromFile(filepath=path_zexp+'layout_default.zexp')

                if layout == '1':
                    context._importObjectFromFile(filepath=path_zexp+'layout_default02.zexp')                
                    context._importObjectFromFile(filepath=path_zexp+'layout_default03.zexp')

                # portal_workflow = getToolByName(context, 'portal_workflow')

                # try:portal_workflow.doActionFor(context, 'publish')
                # except:portal_workflow.doActionFor(context, 'publish_internally')

                if 'defaut_view' in form.keys():
                    obj_layout = context['home_principal']

                    if layout == '1':
                        obj_layout_B = context['home_principal02']
                        obj_layout_C = context['home_principal03']

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
