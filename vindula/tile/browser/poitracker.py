# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class PoiTrackerView(BaseView):
    grok.name('poitracker-view')


    def get_tracker(self):
    	context = self.context
    	return context.getPoi_tracker()