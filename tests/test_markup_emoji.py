#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
import os
import markdown
import unittest

EXTENSIONS = ['markdown_markup_emoji.markup_emoji']
TEST_FILES = (
    ('test01.md', 'output01.html'),
)

class MarkupEmojiTest(unittest.TestCase):
    def test01_simple(self):
        md_source = '中文😀😃😄😌😔😪Spacing'
        expected = '<p>中文<span class="emoji">😀😃😄😌😔😪</span>' + \
            'Spacing</p>'
        html_string = markdown.markdown(
            md_source, extensions=EXTENSIONS)
        self.assertEqual(html_string, expected)

    def test02_fromFile(self):
        for i, (infile, outfile) in enumerate(TEST_FILES):
            with self.subTest(i=i):
                with open(os.path.join(os.path.dirname(__file__), infile),
                          'r', encoding='utf-8') as f:
                    html_string = markdown.markdown(
                        f.read(), extensions=EXTENSIONS).replace('\n', '')
                with open(os.path.join(os.path.dirname(__file__), outfile),
                          'r', encoding='utf-8') as f:
                    expected = f.read().replace('\n', '')
                self.assertEqual(html_string, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
