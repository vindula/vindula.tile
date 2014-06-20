# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

grok.templatedir('templates')

class TileMultimediaView(BaseView):
    grok.name('tilemultimedia-view')
    
    
    def createScript(self, id):
        
        return '''
            flowplayer("%s", "flowplayer-3.1.2.swf", {
                clip: {
                    autoPlay: false,
                    autoBuffering: false,
                    showMenu: false,
                    autoRewind: true,
                    loop: false
                }
            });
        ''' % (id)