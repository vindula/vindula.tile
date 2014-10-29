# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.tile.content.interfaces import ILayout
from zope.security import checkPermission


grok.templatedir('templates')

class LayoutView(BaseView):
    grok.context(ILayout)
    grok.name('layout-view')


    def can_manage_tile(self,obj_tile):
        return checkPermission('cmf.ModifyPortalContent', obj_tile)


    def getScripts_js(self):
        path_js = []

        sdm = self.context.session_data_manager
        session = sdm.getSessionData(create=True)

        scripts_js = session.get("use_js_list", [])

        # #Adição do js de edição dos blocos via modal
        path_js.append('/++resource++vindula.tile/js/tile-edit.js')
        # #Adição do js de drag n drop dos blocos
        path_js.append('/++resource++vindula.tile/js/tile-sortable.js')


        #Coleta dos Script js dos tiles
        context = self.context
        tiles = context.values()
        
        for tile in tiles:
            if hasattr(tile, 'scripts_js'):
                for i in tile.scripts_js:
                    if not i in path_js:
                        path_js.append(i)
        
        for scr in path_js:
            if scr:
                if scr in scripts_js:
                    continue
                else:
                    scripts_js.append(scr)

        session.set("use_js_list", scripts_js)    
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
                                                  'TileHtml',
                                                  'TilePoiTracker'], 
                                        
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
                # TILES DE 6 COLUNAS
                tile_6 = tiles[posicao]

                if tile_6.get_columns() == 6 :

                    try: 
                        next_tile = tiles[posicao+1]
                        if next_tile.get_columns() == 6:
                            tiles_posicionados.append([[tile_6],[next_tile]])
                            posicao += 2
                        else:
                            tiles_posicionados.append([[tile_6],[]])
                            posicao+=1

                    except:
                        tiles_posicionados.append([[tile_6],[]])
                        posicao+=1

                    posicionados+=1
                    

                else: 
               
                    # TILES DE 4 COLUNAS
                    tile_4 = tiles[posicao]
                    if tile_4.get_columns() == 4:
                        
                        try: 
                            middle_tile = tiles[posicao+1]

                            if middle_tile.get_columns() == 4:
                                posicao += 2

                                odd_tile = tiles[posicao]
                                if odd_tile.get_columns() == 4:
                                    tiles_posicionados.append([[tile_4],[middle_tile],[odd_tile]])
                                    posicao += 1

                                else:
                                    tiles_posicionados.append([[tile_4],[middle_tile],[]])

                            else:
                                tiles_posicionados.append([[tile_4],[],[]])

                        except:
                            tiles_posicionados.append([[tile_4],[],[]])
                            posicao+=1

                        posicionados+=1

        return tiles_posicionados

    def getMacro(self, obj):
        macro = 'context/%s/macros/page' %(obj.getLayout())

        return macro
