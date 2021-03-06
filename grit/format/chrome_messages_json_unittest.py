#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittest for chrome_messages_json.py.
"""

import os
import sys
if __name__ == '__main__':
  sys.path[0] = os.path.abspath(os.path.join(sys.path[0], '../..'))

import unittest
import StringIO

from grit import grd_reader
from grit import util
from grit.tool import build

class ChromeMessagesJsonFormatUnittest(unittest.TestCase):

  def testMessages(self):
    root = util.ParseGrdForUnittest(u"""
    <messages>
      <message name="IDS_SIMPLE_MESSAGE">
              Simple message.
      </message>
      <message name="IDS_QUOTES">
              element\u2019s \u201c<ph name="NAME">%s<ex>name</ex></ph>\u201d attribute
      </message>
      <message name="IDS_PLACEHOLDERS">
              <ph name="ERROR_COUNT">%1$d<ex>1</ex></ph> error, <ph name="WARNING_COUNT">%2$d<ex>1</ex></ph> warning
      </message>
      <message name="IDS_STARTS_WITH_SPACE">
              ''' (<ph name="COUNT">%d<ex>2</ex></ph>)
      </message>
      <message name="IDS_DOUBLE_QUOTES">
              A "double quoted" message.
      </message>
      <message name="IDS_BACKSLASH">
              \\
      </message>
    </messages>
    """)

    buf = StringIO.StringIO()
    build.RcBuilder.ProcessNode(root, DummyOutput('chrome_messages_json', 'en'), buf)
    output = buf.getvalue()
    test = u"""
{
  "IDS_SIMPLE_MESSAGE": {
    "message": "Simple message."
  },
  "IDS_QUOTES": {
    "message": "element\u2019s \u201c%s\u201d attribute"
  },
  "IDS_PLACEHOLDERS": {
    "message": "%1$d error, %2$d warning"
  },
  "IDS_STARTS_WITH_SPACE": {
    "message": "(%d)"
  },
  "IDS_DOUBLE_QUOTES": {
    "message": "A \\"double quoted\\" message."
  },
  "IDS_BACKSLASH": {
    "message": "\\\\"
  }
}
"""
    self.assertEqual(test.strip(), output.strip())

  def testTranslations(self):
    root = util.ParseGrdForUnittest("""
    <messages>
        <message name="ID_HELLO">Hello!</message>
        <message name="ID_HELLO_USER">Hello <ph name="USERNAME">%s<ex>
          Joi</ex></ph></message>
      </messages>
    """)

    buf = StringIO.StringIO()
    build.RcBuilder.ProcessNode(root, DummyOutput('chrome_messages_json', 'fr'), buf)
    output = buf.getvalue()
    test = u"""
{
  "ID_HELLO": {
    "message": "H\xe9P\xe9ll\xf4P\xf4!"
  },
  "ID_HELLO_USER": {
    "message": "H\xe9P\xe9ll\xf4P\xf4 %s"
  }
}
"""
    self.assertEqual(test.strip(), output.strip())


class DummyOutput(object):

  def __init__(self, type, language):
    self.type = type
    self.language = language

  def GetType(self):
    return self.type

  def GetLanguage(self):
    return self.language

  def GetOutputFilename(self):
    return 'hello.gif'


if __name__ == '__main__':
  unittest.main()
