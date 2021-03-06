# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.myvindula.tools.utils import UtilMyvindula
from vindula.myvindula.models.funcdetails import FuncDetails


#import datetime
from DateTime.DateTime import DateTime
from datetime import datetime, date, timedelta
import calendar
from vindula.myvindula.cache import *

grok.templatedir('templates')

class BirthdaysView(BaseView, UtilMyvindula):
    grok.name('birthdays-view')

    def getItem(self,username):
        return FuncDetails(username)

    def parse_data(self, str_data):
        D={'day':'','month':''}
        months = ['XX','Jan','Fev','Mar','Abr','Maio','Jun',\
                       'Jul','Ago','Set', 'Out', 'Nov','Dez']

        list_date = str_data.split('/')
        obj_date = date(int(list_date[2]),int(list_date[1]),int(list_date[0]))

        D['day'] = obj_date.day
        D['month'] = months[obj_date.month]

        return D

    def get_details_user(self,dado_user):
        context = self.context
        if context.getDetails_user():

            lines = context.getDetails_user().splitlines()
            L = []
            for line in lines:
                D = {}
                line = line.replace('[', '').replace(']', '').split(' | ')
                try:
                    D['label'] = line[0]
                    if line[1] == 'date_birth':
                        dado = dado_user.get(line[1])
                        dado = dado.split('/')
                        D['content'] = '/'.join(dado[:-1])
                    elif line[1] == 'unidadeprincipal':
                        structure = dado_user.get_unidadeprincipal()
                        result = ''
                        if structure:
                            result = structure.getSiglaOrTitle()
                        D['content'] = result
                    
                    elif line[1] == 'departamento':
                        texto = ''
                        departamentos = dado_user.get_department()
                        cont_dep = len(departamentos)

                        for cont, item in enumerate(departamentos, start=1):
                            texto += ' %s' % item.get('title')
                            if cont_dep != cont:
                                texto += ' /'

                        D['content'] = texto
                    else:
                        D['content'] = dado_user.get(line[1])
                    L.append(D)
                except :
                    pass
            return L

        return []

    def get_birthdaysToday(self, type_filter, filtro_OU):
        Z_now = DateTime()
        today = DateTime().asdatetime().date()

        if type_filter == '1':
            date_start = date_end = today

        elif type_filter == '7':
            day_of_weekday = Z_now.dow()
#            date_start = (Z_now + 1 - day_of_weekday).asdatetime().date()
            #Pega os aniversariantes da semana a partir de HOJE!
            #Acho que nao faz sentido listar os que ja passaram
            date_start = today
            date_end = (Z_now + 1 - day_of_weekday + 6).asdatetime().date()

        elif type_filter == '30':
            last_dia = calendar.monthrange(today.year,today.month)[1]
            date_start = date(today.year,today.month,1)
            date_end = date(today.year,today.month,last_dia)

        elif type_filter == 'prox':
            date_start = today
            date_end = today + timedelta(days=365)
        
        results = FuncDetails.get_FuncBirthdays(date_start,date_end)

        if filtro_OU:
            if not isinstance(filtro_OU, str):
                filtro_OU = filtro_OU.UID()
                
            results_OU = []
            for user in results:
                unidade_user = user.get('UO','')          
                if filtro_OU == unidade_user:
                    results_OU.append(FuncDetails(user.get('username', '')))
            return results_OU
        
        return results

    def birthdaysToday(self):
        type_filter = self.context.getType_search()
        filtro_OU = self.context.getStructures()

        results = self.get_birthdaysToday(type_filter,filtro_OU)
        return results


    def format_members(self,qtd_itens, obj_list):
        lista = []
        L = None
        
        for count, obj in enumerate(obj_list):
            if count == 0 or count % qtd_itens == 0:
                L = []
            L.append(obj)

            if (count + 1) % qtd_itens == 0:
                lista.append(L)
                L = None
        if L:
            lista.append(L)

        return lista