# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.myvindula.tools.utils import UtilMyvindula
from vindula.myvindula.models.dados_funcdetail import ModelsDadosFuncdetails


#import datetime
from DateTime.DateTime import DateTime
import calendar

grok.templatedir('templates')

class BirthdaysView(BaseView, UtilMyvindula):
    grok.name('birthdays-view')


    def parse_data(self, str_data):

        D={'day':'','month':''}

        date = str_data.split('/')
        obj_date = DateTime(int(date[2]),int(date[1]),int(date[0]))

        D['day'] = obj_date.day
        D['month'] = obj_date.pMonth()

        return D

    def get_birthdaysToday(self, type_filter):
        results = []
        now = DateTime()
        ops = False

        if type_filter == 1:
            date_start = date.today().strftime('%Y-%m-%d')
            date_end = date.today().strftime('%Y-%m-%d')
            ops = True
            # results = ModelsDadosFuncdetails().get_FuncBirthdays(date_start,date_end,True)

        elif type_filter == 7:

            dow = now.dow()
            date_start = (now + 1 - dow).strftime('%Y-%m-%d')
            date_end = (now + 1 - dow + 6).strftime('%Y-%m-%d')

            # results = ModelsDadosFuncdetails().get_FuncBirthdays(date_start,date_end)

        elif type_filter == 30:

            dia = calendar.monthrange(now.year(),now.month())[1]
            date_start = now.strftime('%Y-%m-1')
            date_end = now.strftime('%Y-%m-'+str(dia))

            # results = ModelsDadosFuncdetails().get_FuncBirthdays(date_start,date_end)

        elif type_filter == 'prox':

            date_start = ''
            date_end = ''
            ops = 'proximo'


        results = ModelsDadosFuncdetails().get_FuncBirthdays(date_start,date_end,ops)

        return results #results[:int(quant)]


    def birthdaysToday(self):
        type_filter = self.context.type_search
        #quant = self.data.quantidade_portlet


        results = self.get_birthdaysToday(type_filter)

        if results:
            return results #results[:int(quant)]
        else:
            return []