# -*- coding: utf-8 -*-
from five import grok

from vindula.tile.browser.baseview import BaseView


grok.templatedir('templates')

class ListagemHorizontalView(BaseView):
    grok.name('listagemhorizontal-view')

    def getItens(self):
        context = self.context
        # navigation = context.getTypeNavigation()
        results = []
        
        items = context.getHighlights()
        types = context.getListTypes()
        path = context.getPath()
        layout = context.getListTemplates()
        if layout == 'destaque_multipla':
            img_size = '/image_thumb'
        else:
            img_size = '/image_mini'
        
        if path:
            ordination = getattr(context, 'getOrdination', '')
            if ordination:
                ordination = ordination()
                
            order = getattr(context, 'getOrder', '')
            if order:
                order = order()
            
            query = {'portal_type': types,
                     'path':{'query':'/'.join(path.getPhysicalPath()),'depth':99},}
            
            if ordination == 'creation_date':
                query['sort_on'] = 'created'
            elif ordination == 'title':
                query['sort_on'] = 'sortable_title'
                
            if order == 'desc':
                query['sort_order'] ='reverse'
            
            results_pc = self.portal_catalog(query)
            results_pc = [i.getObject() for i in results_pc if i]
            if results_pc:
                items += results_pc

        for item in items:
            D={}

            D['title'] = self.limitTextSize(item.Title(),50)
            D['description'] = self.limitTextSize(item.Description(),120)
            D['url'] = item.absolute_url()
            # D['subtitulo'] = item.getSub_titulo()

            if item.getActive_date():
                D['date'] = item.creation_date.strftime('%d/%m/%Y')
                D['hour'] = item.creation_date.strftime('%H:%M')
            else:
                D['date'] = ''
                D['hour'] = ''

            #TODO: Criar método para buscar a Unidade Organizacional
            if hasattr(item, 'getStructures') and item.getStructures():
                D['unidade'] = item.getStructures().getSiglaOrTitle()
            else:
                D['unidade'] = ''

            try:
                
                D['image'] = item.getImageRelac().absolute_url() + img_size
            except:
                D['image'] = ''

            D['alt'] = item.getImageCaption()

            if item.getActive_author():
                D['author'] = item.getOwner().getUserName()
            else:
                D['author'] = ''

            D['obj'] = item
            results.append(D)
            
        return results

