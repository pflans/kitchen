# -*- coding: utf-8 -*-
import unittest
import unittest.mock
import logging
import gpsoauth

from gkeepapi import Keep, node

logging.getLogger(node.__name__).addHandler(logging.NullHandler())

def mock_keep(keep):
    k_api = unittest.mock.MagicMock()
    r_api = unittest.mock.MagicMock()
    m_api = unittest.mock.MagicMock()
    keep._keep_api._session = k_api
    keep._reminders_api._session = r_api
    keep._media_api._session = m_api

    return k_api, r_api, m_api

class KeepTests(unittest.TestCase):
    @unittest.mock.patch('gpsoauth.perform_master_login')
    def _test_sync(self, perform_master_login):
        keep = Keep()
        k_api, r_api, m_api = mock_keep(keep)
        k_api.request.return_value = {}
        keep.login('user', 'pass')
        keep.sync()
