# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.myvindula.models.funcdetails import FuncDetails

from vindula.myvindula.tools.utils import UtilMyvindula

from datetime import datetime

grok.templatedir('templates')

def por_admicao(item):
    return datetime.strptime(item.get('admission_date','01/01/1500'), '%d/%m/%Y')

class NewEmployeeView(BaseView, UtilMyvindula):
    grok.name('newemployee-view')

    def getItem(self,username):
    	return FuncDetails(username)

    def getItens(self,):
        qtd = 20
        if self.context.getQtdMembers():
            qtd = self.context.getQtdMembers()
        
        dados_users = FuncDetails.get_AllFuncUsernameList(sorted_by=por_admicao,reverse=True)[:qtd]
        return dados_users