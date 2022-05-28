import unittest 
from .. import peekable_stream
from lexer import tokenize

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

        source = "~ this is a comment"
        p = PeekableStream(iter(source))

        expected_tokens = []
        actual_tokens = tokenize(p)

        self.assertEquals(expected_tokens, actual_tokens)

         
if __name__ == '__main__':
    unittest.main()
