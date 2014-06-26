# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.tile.content.interfaces import ILayout


grok.templatedir('templates')

class LayoutView(BaseView):
    grok.context(ILayout)
    grok.name('layout-view')


    def getScripts_js(self):
        path_js = []

        #Coleta dos Script js dos tiles
        context = self.context
        tiles = context.values()

        for tile in tiles:
            if hasattr(tile, 'scripts_js'):
                for i in tile.scripts_js:
                    if not i in path_js:
                        path_js.append(i)
        
        scripts_js = []
        for scr in path_js:
            if scr:
                D = {}
                if scr.find('/') != -1:
                    D['name'] = scr.split('/')[-1]
                else:
                    D['name'] = scr
                
                if D.get('name'):
                    D['name'] = D['name'].replace('.js', '')
                D['path'] = scr
                
                scripts_js.append(D)
            
        return scripts_js
    
    def getStyleSheets_css(self):
        style_sheets = []

        #Coleta das folhas de estilo css dos tiles
        context = self.context
        tiles = context.values()

        for tile in tiles:
            if hasattr(tile, 'style_sheets'):
                for i in tile.style_sheets:
                    if not i in style_sheets:
                        style_sheets.append(i)

        return style_sheets


    def _get_catalog_tiles(self):
        context = self.context
        current_user = self.p_membership.getAuthenticatedMember()
        tiles = []

        itens = self.portal_catalog(**{'sort_on': 'getObjPositionInParent',
                                   'portal_type':['TileAccordionContent',
                                                  'TileBanner',
                                                  'TileBannerCompost',
                                                  'TileBirthdays',
                                                  'TileCalendar',
                                                  'TileFeatured',
                                                  'TileFood',
                                                  'TileHowDo',
                                                  'TileInfoStructure',
                                                  'TileJobOffer',
                                                  'TileLabel',
                                                  'TileListServices',
                                                  'TileLibrary',
                                                  'TileListagemHorizontal',
                                                  'TileListagemVertical',
                                                  'TileLoadReference',
                                                  'TileMacroList',
                                                  'TileMoreAccess',
                                                  'TileMultimedia',
                                                  'TileNewEmployee',
                                                  'TileOrganogram',
                                                  'TilePoll',
                                                  'TileReferenceList',
                                                  'TileSimpleMacro',
                                                  'TileTabularList',
                                                  'TileTeam',
                                                  'TilePoiTracker',],  
                                   # 'review_state':['published', 'internally_published', 'external'],
                                   'path':{'query':'/'.join(context.getPhysicalPath()), 'depth': 5}
                                })

        for t in itens:
            t = t.getObject()
            if not t.getExcludeFromNav() and\
                self.has_public_or_permission(current_user, t):
                tiles.append(t)

        return tiles



    def getItensTiles(self, size_global=False):
        """
        @size_global = Forsa retornar sempre um tile por linha, usado no carrega tile de
                        layout padrao

        Esse metodo retorna uma lista de listas, com os tiles
        organizados pelo numero de colunas que ocupa.

        Cada posicao da lista é uma linha que pode ter um tile de
        12 colunas , ou duas colunas com N tiles de 6 colunas em cada.

        Exemplo de retorno:
        [
         [<TileBanner at /vindula/home/banner-topo>], <--12 Colunas
         [<TileListagemHorizontal at /vindula/home/noticias>], <--12 Colunas
         [[<TileFeatured at /vindula/home/destques>], []], <--6 Colunas
         [<TileListagemHorizontal at /vindula/home/noticias-1>], <--12 Colunas
         [[<TileListagemVertical at /vindula/home/mais-populares>,<TileBirthdays at /vindula/home/aniversariantes-da-semana>],
          [<TileListagemVertical at /vindula/home/proximos-eventos>]] <--6 Colunas
        ]
        """
        context = self.context

        posicionados = 0
        posicao = 0
        
        tiles = self._get_catalog_tiles()
        # tiles = [ t for t in context.values() if t.portal_type != 'VindulaFolder' and not t.getExcludeFromNav()]

        tiles_posicionados = []
        for i in range(len(tiles)):

            if posicionados == len(tiles) or posicao >= len(tiles):
                break

            tile = tiles[posicao]

            if tile.get_columns() == 12 or size_global :
                tiles_posicionados.append([tile])
                posicionados += 1
                posicao+=1
            else:
                even = []
                odd = []
                contador_temp = 1
                for tile_6 in tiles[posicao:]:

                    if posicao >= len(tiles):
                        break

                    if tile_6.get_columns() == 6:
                        if contador_temp%2 == 0:
                            odd.append(tile_6)
                        else:
                            even.append(tile_6)

                        contador_temp+=1
                        posicionados+=1
                        posicao+=1
                    else:break
                tiles_posicionados.append([even,odd])

        return tiles_posicionados

    def getMacro(self, obj):
        macro = 'context/%s/macros/page' %(obj.getLayout())

        return macro


class LoadLayoutView(BaseView):
    grok.name('layout_load-view')



