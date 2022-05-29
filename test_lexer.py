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

    def test_parser_int_assigment(self):
        
        source = "int a;\n a = 3;"
        p = PeekableStream(iter(source))

        expected_tokens = []
        logging.debug(tokenize(p))
        tokens = tokenize(p)

        executables = parse(0, tokenize(tokens))
        logging.debug(executables)


if __name__ == '__main__':
    unittest.main()





