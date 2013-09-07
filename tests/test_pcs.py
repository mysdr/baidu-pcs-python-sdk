#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import pdb
import time

from baidupcs import PCS

logging.basicConfig(level=logging.WARN,
                    format='\n%(funcName)s - %(lineno)d\n%(message)s')
logger = logging.getLogger(__name__)

access_token = '3.3f56524f9e796191ce5baa84239feb15.2592000.1380728222.'
access_token += '570579779-1274287'
pcs = PCS(access_token)


def test_info():
    result = pcs.info()
    logger.warn(result)
    assert True


def test_upload():
    result = pcs.upload('/apps/test_sdk/test.txt', 'test')
    logger.warn(result)
    assert True


def test_superfile():
    f1_md5 = pcs.upload_tmpfile('abc')['md5']
    f2_md5 = pcs.upload_tmpfile('def')['md5']
    result = pcs.upload_superfile('/apps/test_sdk/super2.txt',
                                  [f1_md5, f2_md5])
    logger.warn(result)
    assert True


def test_download():
    result = pcs.download('/apps/test_sdk/super2.txt')
    logger.warn(result)
    assert 'abc' in result
    assert 'def' in result


def test_mkdir():
    result = pcs.mkdir('/apps/test_sdk/testmkdir')
    logger.warn(result)
    assert True


def test_meta():
    result = pcs.meta('/apps/test_sdk/superfile.txt')
    logger.warn(result)
    assert True


def test_multi_meta():
    result = pcs.multi_meta(['/apps/test_sdk/superfile.txt',
                            '/apps/test_sdk/testmkdir'])
    logger.warn(result)
    assert True


def test_file_list():
    result = pcs.file_list('/apps/test_sdk/testmkdir')
    logger.warn(result)
    assert True


def test_move():
    result = pcs.move('/apps/test_sdk/test.txt',
                      '/apps/test_sdk/testmkdir/a.txt')
    logger.warn(result)
    assert True


def test_multi_move():
    pcs.upload('/apps/test_sdk/test.txt', 'test')
    path_list = [
        {
            'from': '/apps/test_sdk/test.txt',
            'to': '/apps/test_sdk/testmkdir/b.txt',
        },
        {
            'from': '/apps/test_sdk/testmkdir/b.txt',
            'to': '/apps/test_sdk/testmkdir/a.txt',
        }
    ]
    result = pcs.multi_move(path_list)
    logger.warn(result)
    assert True


def test_copy():
    pcs.upload('/apps/test_sdk/test.txt', 'test')
    result = pcs.copy('/apps/test_sdk/test.txt',
                      '/apps/test_sdk/testmkdir/c.txt')
    logger.warn(result)
    assert True


def test_multi_copy():
    path_list = [
        {
            'from': '/apps/test_sdk/test.txt',
            'to': '/apps/test_sdk/testmkdir/d.txt',
        },
        {
            'from': '/apps/test_sdk/testmkdir/c.txt',
            'to': '/apps/test_sdk/testmkdir/e.txt',
        }
    ]
    result = pcs.multi_copy(path_list)
    logger.warn(result)
    assert True


def test_delete():
    pcs.upload('/apps/test_sdk/testmkdir/e.txt', 'test')
    result = pcs.delete('/apps/test_sdk/testmkdir/e.txt')
    logger.warn(result)
    assert True


def test_multi_delete():
    pcs.upload('/apps/test_sdk/testmkdir/e.txt', 'test')
    result = pcs.multi_delete(['/apps/test_sdk/testmkdir/e.txt',
                              '/apps/test_sdk/testmkdir/d.txt'])
    logger.warn(result)
    assert True


def test_search():
    result = pcs.search('/apps/test_sdk/testmkdir', 'a')
    logger.warn(result)
    assert True


def test_thumbnail():
    result = pcs.thumbnail('/apps/test_sdk/testmkdir/404.png', 20, 20)
    logger.warn(result)
    assert True

def test_diff():
    pcs.upload('/apps/test_sdk/testmkdir/h.txt', 'testabc', ondup='overwrite')
    result = pcs.diff()
    logger.warn(result)
    logger.warn('\n')
    new_cursor = result['cursor']
    time.sleep(60)
    pcs.upload('/apps/test_sdk/testmkdir/h.txt', str(time.time()),
               ondup='overwrite')
    result = pcs.diff(cursor=new_cursor)
    logger.warn(result)
    assert True

def test_video_convert():
    result = pcs.video_convert('/apps/test_sdk/testmkdir/test.mp4',
                               'M3U8_320_240')
    logger.warn(result)
    assert True
