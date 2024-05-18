import unittest
from lexer import tokenize
class TestLexer(unittest.TestCase):
    def test_keywords_and_identifiers(self):
        code = "def foo(): pass"
        expected_tokens = [
            ('KEYWORD', 'def'),
            ('IDENTIFIER', 'foo'),
            ('LPAREN', '('),
            ('RPAREN', ')'),
            ('COLON', ':'),
            ('KEYWORD', 'pass')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_numbers_and_operators(self):
        code = "x = 42 + 3.14"
        expected_tokens = [
            ('IDENTIFIER', 'x'),
            ('OPERATOR', '='),
            ('NUMBER', '42'),
            ('OPERATOR', '+'),
            ('NUMBER', '3.14')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_strings_and_comments(self):
        code = """
        # This is a comment
        s = "hello" + 'world'
        """
        expected_tokens = [
            ('NEWLINE', '\n'),
            ('COMMENT', '# This is a comment'),
            ('NEWLINE', '\n'),
            ('IDENTIFIER', 's'),
            ('OPERATOR', '='),
            ('STRING', '"hello"'),
            ('OPERATOR', '+'),
            ('STRING', "'world'"),
            ('NEWLINE', '\n')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

    def test_delimiters(self):
        code = "(a, b) = {x: [1, 2, 3]}"
        expected_tokens = [
            ('LPAREN', '('),
            ('IDENTIFIER', 'a'),
            ('COMMA', ','),
            ('IDENTIFIER', 'b'),
            ('RPAREN', ')'),
            ('OPERATOR', '='),
            ('LBRACE', '{'),
            ('IDENTIFIER', 'x'),
            ('COLON', ':'),
            ('LBRACKET', '['),
            ('NUMBER', '1'),
            ('COMMA', ','),
            ('NUMBER', '2'),
            ('COMMA', ','),
            ('NUMBER', '3'),
            ('RBRACKET', ']'),
            ('RBRACE', '}')
        ]
        self.assertEqual(tokenize(code), expected_tokens)

if __name__ == '__main__':
    unittest.main()
