# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.myvindula.models.funcdetails import FuncDetails

from vindula.myvindula.tools.utils import UtilMyvindula

grok.templatedir('templates')

def por_admicao(item):
    return item.get('admission_date','')

class NewEmployeeView(BaseView, UtilMyvindula):
    grok.name('newemployee-view')

    def getItens(self,):
        dados_users = FuncDetails.get_AllFuncDetails()
        result = sorted(dados_users, key=por_admicao)
        return result