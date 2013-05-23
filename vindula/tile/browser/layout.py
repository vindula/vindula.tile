# coding: utf-8
from five import grok
from vindula.tile.browser.baseview import BaseView

from vindula.tile.content.interfaces import ILayout

grok.templatedir('templates')

class LayoutView(BaseView):
    grok.context(ILayout)
    grok.name('layout-view')


    def getScripts_js(self):
        scripts_js = []

        #Coleta dos Script js dos tiles
        context = self.context
        tiles = context.values()

        for tile in tiles:
            if hasattr(tile, 'scripts_js'):
                for i in tile.scripts_js:
                    if not i in scripts_js:
                        scripts_js.append(i)

        return scripts_js



    def getItensTiles(self):
        """
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
        tiles = context.values()
        tiles_posicionados = []
        for i in range(len(tiles)):

            if posicionados == len(tiles) or posicao >= len(tiles):
                break

            tile = tiles[posicao]

            if tile.get_columns() == 12:
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



