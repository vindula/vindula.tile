# -*- coding: utf-8 -*-
from zope.interface import Interface

class IBaseTile(Interface):
    """ Interface for BaseTile content type """

class ILayout(Interface):
    """ Interface for Layout content type """

class ITileBanner(Interface):
    """ Interface for BannerTile content type """

class ITileListagemVertical(Interface):
    """ Interface for TileListagemVertical content type """

class ITileListagemHorizontal(Interface):
    """ Interface for TileListagemHorizontal content type """

class ITileSimpleMacro(Interface):
    """ Interface for TileSimpleMacro content type """

class ITileMacroList(Interface):
    """ Interface for TileMacroList content type """

class ITileFeatured(Interface):
    """ Interface for TileFeatured content type """

class ITileAccordionContent(Interface):
    """ Interface for TileAccordionContent content type """

class ITileAccordionItem(Interface):
    """ Interface for TileAccordionItem content type """

class ITileMoreAccess(Interface):
    """ Interface for TileMoreAccess content type """

class ITileLabel(Interface):
    """ Interface for TileLabel content type """

class ITileBirthdays(Interface):
    """ Interface for TileBirthdays content type """

class ILayoutLoad(Interface):
    """ Interface for LayoutLoad content type """

class ITilePoll(Interface):
    """ Interface for TilePoll content type """

class ITileOrganogram(Interface):
    """ Interface for TileOrganogram content type """
