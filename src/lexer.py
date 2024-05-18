import regex as re 

TOKEN_SPECIFICATION = [
        ('COMMENT',   r'#.*'),                      # Comments
        ('STRING',    r'\".*?\"|\'[^\']*\'|\'\'\'(?:.|\n)*?\'\'\''),  # Single and multi-line strings
        ('NUMBER',    r'\b\d+(\.\d*)?\b'),          # Integer or decimal numbers
        ('IDENTIFIER',r'\b[a-zA-Z_]\w*\b'),         # Identifiers
        ('OPERATOR',  r'[+\-*/%=<>!&|^~]+'),        # Operators
        ('LPAREN',    r'\('),                       # Left Parenthesis
        ('RPAREN',    r'\)'),                       # Right Parenthesis
        ('LBRACE',    r'\{'),                       # Left Brace
        ('RBRACE',    r'\}'),                       # Right Brace
        ('LBRACKET',  r'\['),                       # Left Bracket
        ('RBRACKET',  r'\]'),                       # Right Bracket
        ('COMMA',     r','),                        # Comma
        ('COLON',     r':'),                        # Colon
        ('SEMICOLON', r';'),                        # Semicolon
        ('NEWLINE',   r'\n'),                       # Line endings
        ('SKIP',      r'[ \t]+'),                   # Skip over spaces and tabs
        ('MISMATCH',  r'.'),                   # Any other character
]

KEYWORDS = {
    'if', 'else', 'while', 'for', 'def', 'return', 'in', 'import',
    'from', 'as', 'with', 'try', 'except', 'finally', 'class', 'pass',
    'print', 'and', 'or', 'not', 'is', 'None', 'True', 'False', 'lambda'
}

def tokenize(code):
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)
    tokens = []
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            tokens.append(('NEWLINE', '\n'))
        # elif kind == 'SKIP' or kind == 'COMMENT':
        elif kind == 'SKIP':
            continue
        elif kind == 'IDENTIFIER' and value in KEYWORDS:
            tokens.append(('KEYWORD', value))
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r}')
        else:
            tokens.append((kind, value))
    return tokens