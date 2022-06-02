import unittest 
from peekable_stream import PeekableStream 
from lexer import tokenize
import logging 
from parser import parse 
import parser
import json


class TestLexer(unittest.TestCase):

    def get_tokens(self, source):
        return tokenize(PeekableStream(iter(source)))

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

    def test_fail_construct_assigment_when_no_equals_after_identifier(self):

        source = "a + 2"
        tokens = tokenize(PeekableStream(iter(source)))
    
        self.assertRaises(ValueError, parser.construct_assignment, tokens, 0) 

    def test_construct_simple_assigment(self):
        
        source = "a = 3;"
        tokens = self.get_tokens(source)
        
        assignment_sub_tree = json.loads('{"assignment": {"assignee": "a", "value": 3}}')
        assignment_sub_tree = dict(assignment_sub_tree)

        self.assertEquals(assignment_sub_tree, parser.construct_assignment(tokens, 0)[1])

if __name__ == '__main__':
    unittest.main()




