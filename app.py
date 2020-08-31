import asyncio
from scraptic import launch


async def main():
    engine = await launch()
    template = await engine.newTemplate()
    template.appendSelector(
        '#NM_NEWSSTAND_DEFAULT_THUMB > div._NM_UI_PAGE_CONTAINER > div:nth-child(3) > div > div.thumb_area > div:nth-child(1) > a > img',
        'image_link'
    )
    await template.contents('https://www.naver.com')

    template = await engine.newTemplate()
    template.appendSelector(
        '#content > div.article > div.section > div.news_area > div > ul > li:nth-child(1) > span > a',
        'image_link'
    )
    await template.contents('https://finance.naver.com/')


asyncio.get_event_loop().run_until_complete(main())
