import logging

from bs4 import BeautifulSoup
from typing import Any, Dict, List, TYPE_CHECKING
from pyppeteer import browser

from scraptic.selector import Selector
from scraptic.logger import getLogger

logger = getLogger(__name__)


class Template:
    def __init__(self, page: browser.Page):
        self._selectors = []
        self._page = page

    def appendSelector(self, selector: str, name: str):
        self._selectors.append(
            Selector.create(selector, name)
        )

    async def contents(self, baseUrl: str) -> list:
        self._page.setDefaultNavigationTimeout(1000 * 60)
        await self._page.goto(baseUrl, waitUntil='networkidle2')
        html = await self._page.content()
        soup = BeautifulSoup(html, 'html.parser')
        for selector in self._selectors:
            selector.process(soup)
        await self._page.screenshot({'path': 'example.png'})
        await self._page.close()
        return []
