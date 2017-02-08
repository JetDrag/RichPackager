# coding=utf-8
import json
import logging
import os

from common_helper.helper_file_or_dir import dir_create
from common_helper.helper_logging import NORMAL_LOG_FORMAT_0

__author__ = 'lawrentwang'


class GlobalConfigs:
    DATA_PATH_ROOT = os.path.abspath(os.path.join('data'))
    APP_DATA_PATH_ROOT = os.path.abspath(os.path.join(DATA_PATH_ROOT, 'app_data'))
    WORKING_DATA_PATH_ROOT = os.path.abspath(os.path.join(DATA_PATH_ROOT, 'working_data'))
    TEMP_DATA_PATH_ROOT = os.path.abspath(os.path.join(DATA_PATH_ROOT, 'temp_data'))

    LOG_FORMAT = NORMAL_LOG_FORMAT_0

    ENV_TAG = None
    if os.path.isfile(os.path.join(APP_DATA_PATH_ROOT, "specific_config.json")):
        with open(os.path.join(APP_DATA_PATH_ROOT, "specific_config.json")) as fr:
            ENV_TAG = json.load(fr)['env']

    _sh = logging.StreamHandler()
    _sh.setFormatter(logging.Formatter(LOG_FORMAT))
    LOGGER_STEAMHANDLER = _sh


def module_setup():
    for config_cls in [GlobalConfigs]:
        for attr in dir(config_cls):
            if attr.endswith('_PATH'):
                dir_create(getattr(config_cls, attr))

module_setup()
