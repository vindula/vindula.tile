# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class OrganogramView(BaseView):
    grok.name('organogram-view')


    def estrutura_pai(self):
        context = self.context
        item = context.getEstrutura_principal()

        estrutura_pai = item.getStructures()
        if estrutura_pai:
            return estrutura_pai
        else:
            return item


    def get_estruturas_filho(self,estrutura_pai):
        L = []
        if estrutura_pai:
            refs = self.reference_catalog.getBackReferences(estrutura_pai, 'structures', targetObject=None) or []
            for ref in refs:
                obj = ref.getSourceObject()
                if obj.portal_type == 'OrganizationalStructure':
                    L.append(obj)

        return L

    def def_class(sef,estrutura, estruturas_filho):
        classe = 'tree-item'
        if hasattr(estrutura, 'getUnidadeEspecial') and estrutura.getUnidadeEspecial():
            classe += ' dashed'

        if len(estruturas_filho) > 0:
            classe += ' arrow'

        return classe