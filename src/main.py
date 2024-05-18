import sys
from lexer import tokenize
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

def main(): 
    filename = sys.argv[1]
    logger = Logger()
    source = catch_errors(filename, logger)
    print(tokenize(source))
if __name__ == "__main__":
    main()