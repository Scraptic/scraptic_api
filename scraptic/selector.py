import re

from bs4 import BeautifulSoup
from scraptic.logger import getLogger

logger = getLogger(__name__)


def merge_selector_list(selectors: list) -> str:
    result = ''
    for idx, selector in enumerate(selectors):
        result += selector
        if idx is not len(selectors) - 1:
            result += ' > '

    return result


class Selector(object):
    def __init__(self, _selector: str, _name: str):
        self.selector = _selector
        self.name = _name

    @staticmethod
    def create(selector: str, name: str) -> 'Selector':
        return Selector(selector, name)

    def process(self, soup: BeautifulSoup) -> str:
        # 공백 제거, 구분
        selectors = self.selector.replace(' ', '').split('>')
        logger.info(selectors)

        is_list_selector = False
        # 마지막 리스트 요소만 반복
        last_index_count = 0
        for idx, selector in enumerate(selectors):
            # 리스트 일 경우
            if re.search(r'(\d+)', selector) is not None:
                is_list_selector = True
                last_index_count = idx

        if is_list_selector:
            # 리스트 요소 전
            a_selectors = selectors[0:last_index_count]
            a_selectors = merge_selector_list(a_selectors)
            # 모든 요소 검색
            a_selectors += ' > '
            a_selectors += selectors[last_index_count].split(':')[0]
            # 리스트 요소 후
            b_selectors = selectors[last_index_count + 1:len(selectors)]
            b_selectors = merge_selector_list(b_selectors)
            for selector in soup.select(a_selectors):
                select_selector = selector.select(b_selectors)
                if len(select_selector) > 0:
                    logger.info(
                        select_selector[0].attrs.keys()
                    )
                    logger.info(select_selector[0])

        return ''
