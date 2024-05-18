class Logger: 
    typ = ""

    def __init__(self, v: str = "") -> None:
        self.typ = v.lower()

    def info(self, txt: str):
        """
        [INFO] This is an info message. 
        Color displayed: Dark Cyan
        """
        if self.typ == "strict": print(f"\033[36m[INFO] {txt}\033[m")

    
    def warning(self, txt: str):
        """
        [WARN] This is an warning message. 
        Color displayed: Magenta
        """
        print(f"\033[35m[WARN] {txt}\033[m")
    
    def error(self, txt: str):
        """
        [ERROR] This is an error. 
        Color displayed: Red
        """
        print(f"\033[91m[ERROR] {txt}\033[m")

