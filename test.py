import unittest 
from peekable_stream import PeekableStream 
from lexer import tokenize

class Test(unittest.TestCase):

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

        source = "~ hey, this is a comments and it should be ignored"
        p = PeekableStream(iter(source))

        expected_tokens = []
        actual_tokens = tokenize(p)

        self.assertEquals(expected_tokens, actual_tokens)
    
    def test_tokenize_strings(self):
        
        source = "\"string between double quotes\", and \'string under single quotes\'"
        p = PeekableStream(iter(source))

        expected_tokens = [('string', 'this is a string')]
        actual_tokens = tokenize(p)

        print(actual_tokens)

if __name__ == '__main__':
    unittest.main()

