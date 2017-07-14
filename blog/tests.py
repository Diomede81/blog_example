# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Post

class PostTest(TestCase):

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        test_title.content = "Bla Bla Bla"
        self.assertEqual(str(test_title.title),'My Latest Blog Post')
        self.assertEqual(str(test_title.content),'Bla Bla Bla')



# Create your tests here.
