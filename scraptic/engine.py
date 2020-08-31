from pyppeteer import browser
from scraptic.template import Template
from scraptic.logger import getLogger

logger = getLogger(__name__)


class Engine(object):
    def __init__(self, _engineBrowser: browser.Browser):
        self.browser = _engineBrowser

    @staticmethod
    def create(_engineBrowser: browser.Browser) -> 'Engine':
        return Engine(_engineBrowser=_engineBrowser)

    async def newTemplate(self):
        return Template(page=await self.browser.newPage())
