# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView
import string

grok.templatedir('templates')

class HowDoView(BaseView):
    grok.name('howdo-view')
    first_active = True

    def getItens(self):
        context = self.context
        numbers = context.getNumItems()
        types = context.getObjectType()
        subjects = context.getSubjects()
	

        path = context.portal_url.getPortalObject()

        itens = self.portal_catalog(portal_type = types,
                                    # review_state = states,
                                    path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                    Subject = subjects,
                                    sort_on='effective',
                                    sort_order='descending',
                                    )

        return itens[:numbers]

    def alphabet(self):
        #ABCDEFGHIJKLMNOPQRSTUVWYXZ + NUMBERS
        L = []
        for i in string.ascii_uppercase:
            L.append(i)
        
        for i in range(0,10):
            L.append(str(i))

        return L

    def constructor(self):
        letras_numeros = {}
        for i in self.alphabet():
            letras_numeros[i] = []
        
        for item in self.list_more():            
            #Todo: remover isso, colocado apenas para teste            
            try:
                obj = item.getObject()
                title = self.getTitle(obj)
                if len(title) > 0:
                    letras_numeros[title[0].upper()].append(item)
            except KeyError:
                pass


        return letras_numeros

    def list_more(self):
        context = self.context
        path = context.portal_url.getPortalObject()

        portal_type = context.getObjectType()

        subjects = context.getSubjects()


        itens = self.portal_catalog(portal_type = portal_type,
                                    # review_state = states,
                                    path={'query':'/'.join(path.getPhysicalPath()),'depth':99},
                                    sort_on='effective',
                                    Subject=subjects,
                                    sort_order='descending',
                                    )

        return itens


    def getTitle(self,obj):
        str = ''
        if hasattr(obj, 'getSiglaunidade'):
            str = obj.getSiglaunidade()

        if not str:
            str = obj.Title()

        # print str
        return str


    def is_first_active(self,has_content):
        if not has_content and self.first_active:
            self.first_active = False
            return 'active'
        else:
            return ''

