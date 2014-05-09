# coding: utf-8
from five import grok
from Products.CMFCore.utils import getToolByName

from vindula.tile.browser.baseview import BaseView
from vindula.tile.content.interfaces import ITileLibrary
from vindula.content.models.tag_content import TagContent

from collections import OrderedDict


grok.templatedir('templates')

class LibraryView(BaseView):
    grok.name('library-view')
    
    
    def getThemes(self):
        rs_themes = TagContent.getAllTagsByType('themesNews')

        themes = []
        
        if rs_themes and rs_themes.count():
            if self.context.getQtdThemesGlobal() and self.context.getQtdThemesGlobal() > 0:
                rs_themes = rs_themes[:self.context.getQtdThemesGlobal()]

            for theme in  rs_themes:
                themes.append(theme)
                
        return themes
    
class ThemeContentsView(BaseView):
    grok.context(ITileLibrary)
    grok.name('theme-contents')
    
    theme = None
    
    def update(self):
        if self.request.form.get('theme'):
            self.theme = TagContent.getTagById(self.request.form.get('theme'))
            
    def getTypologies(self, theme):
        p_catalog = getToolByName(self.context, 'portal_catalog')
        typologies = {}
        if theme:
            value = theme.value

            brains = p_catalog(ThemeNews=value)
            for brain in brains:
                if not brain.tipo or brain.portal_type == 'Image':
                    continue
                
                if typologies.get(brain.tipo):
                    typologies[brain.tipo].append(brain.getObject())
                else:
                    typologies[brain.tipo] = [brain.getObject()]
        
        od = OrderedDict(sorted(typologies.items(), key=lambda t: t[0]))
        typologies = od.items()
        
        typologies = OrderedDict(typologies)
        
        return typologies
    
    def getImageUrlByType(self, obj):
        base = self.context.portal_url() + "/++resource++vindula.content/images/"
        type = obj.portal_type
        url = ''
        
        if type == 'VindulaPhotoAlbum':
            photos = obj.contentValues()
            if photos:
                url = photos[0].absolute_url() + '/image_preview'
        elif type in ['VindulaVideo', 'VindulaStreaming']:
            if type == 'VindulaVideo':
                photo = obj.getImage_preview()
            else:
                photo = obj.getImage()

            if photo:
                url = photo.absolute_url()
        else:
            if self.context.getIconFileDefault():
                url = self.context.getIconFileDefault().absolute_url() + '/image_tile'
        
        if not url:
            url = base + "icon-default.png"

        return url
        
        
        
        
        
        
        
        
        
        
        