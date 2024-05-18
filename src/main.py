import sys
import regex as re
from logger import Logger

def catch_errors(fp: str, logger: Logger) -> str | None:
    with open(fp, "r") as f: 
        source = f.read()

    # Catch syntax errors. Note: Runtime errors like NameError and TypeError
    # aren't caught here since that would require the use of exec() which
    # ends up running the code. In the future, I will end up implementing
    # this by running in parallel to avoid blocking the main thread.

    try: 
        compile(source, fp, "exec")
        logger.info("Compiled source without syntax errors.")
    except Exception as e: 
        logger.error(f"{e.__class__.__name__}: {e}")
        return
    
    return source


def tokenize(code):
    KEYWORDS = {
    'if', 'else', 'while', 'for', 'def', 'return', 'in', 'import',
    'from', 'as', 'with', 'try', 'except', 'finally', 'class', 'pass',
    'print', 'and', 'or', 'not', 'is', 'None', 'True', 'False', 'lambda'
    }

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

def main(): 
    filename = sys.argv[1]
    logger = Logger()
    source = catch_errors(filename, logger)
    print(tokenize(source))
if __name__ == "__main__":
    main()