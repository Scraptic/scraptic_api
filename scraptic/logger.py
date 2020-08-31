#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8

import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pytz import timezone


def getLogger(name):
    # 로그 저장할 폴더 생성
    log_dir = './logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Timezone 설정
    tz = timezone('Asia/Seoul')  # UTC, Asia/Shanghai, Europe/Berlin

    def timezone_converter(*args):
        return datetime.now(tz).timetuple()

    logging.Formatter.converter = timezone_converter

    # 로거 생성
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s'
    )

    # 로거에 핸들러 추가
    # 자정마다 한 번씩 로테이션
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename='%s/scraptic.log' % log_dir, when='midnight', interval=1, encoding='utf-8'
    )
    file_handler.suffix = '%Y%m%d'  # 로그 파일명 날짜 기록 부분 포맷 지정
    file_handler.setFormatter(formatter)  # 핸들러에 로깅 포맷 할당
    logger.addHandler(file_handler)

    # 콘솔 핸들러 추가
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    # 로거에 콘솔 핸들러 추가
    logger.addHandler(console_handler)
    #
    return logger
