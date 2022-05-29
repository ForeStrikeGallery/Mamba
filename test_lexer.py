import unittest 
from peekable_stream import PeekableStream 
from lexer import tokenize
import logging 
from parser import parse 

class TestLexer(unittest.TestCase):

    def test_sample(self):
        self.assertTrue(True)

    def test_tokenize_int_declaration(self):
        source = "int a;"
        p = PeekableStream(iter(source))

        expected_tokens = [('symbol', 'int'), ('symbol', 'a'), (';', '')]
        actual_tokens = tokenize(p)

        self.assertEquals(expected_tokens, actual_tokens)

    def test_tokenize_empty_stream(self):

        source = "  "
        p = PeekableStream(iter(source))

        expected_tokens = []
        actual_tokens = tokenize(p)

        self.assertEquals(expected_tokens, actual_tokens)

    def test_tokenize_comments(self):

        source = "~"
        p = PeekableStream(iter(source))

        expected_tokens = []
        actual_tokens = tokenize(p)

        self.assertEquals(expected_tokens, actual_tokens)

    def test_fail_parsing_when_no_equals_after_identifier(self):
        
        source = "int a;\n a + 3;"
        p = PeekableStream(iter(source))

        tokens = tokenize(p)
        with self.assertRaises(ValueError):
            parse(0, tokens) 

    def test_fail_parsing_when_no_value_after_equals(self):

        source = "int a; a = + 4";
        p = PeekableStream(iter(source))

        tokens = tokenize(p)
        parse(0, tokens)
        with self.assertRaises(ValueError):
            parse(0, tokens) 


if __name__ == '__main__':
    unittest.main()





