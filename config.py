import os
import json
import logging


def prepare_cfg(filename='config.json'):
    cfg = load_config(filename=filename)
    check_default_dirs(cfg=cfg)
    return {
        'api_args': cfg['api_args'],
        'query_args': cfg['query_args'],
    }


def load_config(filename):
    with open(filename, 'r') as f:
        cfg = json.loads(f.read())
        return cfg


def check_default_dirs(cfg: dict):
    for key in cfg.keys():
        if 'dir' in key:
            directory = cfg[key]
            if not os.path.exists(directory):
                os.makedirs(directory)
