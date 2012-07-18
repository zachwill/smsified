#!/usr/bin/env python

"""
Unit tests for SMSified.
"""

import os
from unittest import main, TestCase
from mock import Mock

import smsified as sms


class SMS(TestCase):

    def setUp(self):
        os.environ['SMS_USER'] = ''
        os.environ['SMS_PASS'] = ''
        sms.api.req = Mock()
        self.post = sms.api.req.post

    def tearDown(self):
        os.environ['SMS_USER'] = ''
        os.environ['SMS_PASS'] = ''

    def test_auth(self):
        sms.auth('ohai', 'test')
        self.assertEquals(os.environ['SMS_USER'], 'ohai')
        self.assertEquals(os.environ['SMS_PASS'], 'test')

    def test_number(self):
        sms.number('123-456-7890')
        self.assertEquals(os.environ['SMSIFIED_NUMBER'], '1234567890')

    def test_integer_number(self):
        sms.number(1234567890)
        self.assertEquals(os.environ['SMSIFIED_NUMBER'], '1234567890')

    def test_send(self):
        sms.number('123-456-7890')
        sms.send('555-555-5555', 'ohai')
        self.assertTrue(self.post.called)


if __name__ == '__main__':
    main()
