import asyncio
import logging
import pyppeteer

from typing import Any, Dict, List, TYPE_CHECKING
from scraptic.engine import Engine
from scraptic.logger import getLogger

logger = getLogger(__name__)


class Launcher(object):
    def __init__(self, options: Dict[str, Any] = None):
        self.options = options

    async def launch(self) -> Engine:
        browser = await pyppeteer.launch(
            headless=True,
            args=[
                "--no-sandbox"
            ]
        )
        return Engine.create(browser)


async def launch(options: dict = None):
    return await Launcher(options=options).launch()
