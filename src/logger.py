class Logger: 
    def __init__(self) -> None:
        pass

    def info(self, txt: str):
        """
        [INFO] This is an info message. 
        Color displayed: Yellow
        """
        print(f"\033[36m[INFO] {txt}\033[m")

    
    def warning(self, txt: str):
        """
        [WARN] This is an warning message. 
        Color displayed: Magenta
        """
        print(f"\033[35m[WARN] {txt}\033[m")
    
    def error(self, txt: str):
        """
        [WARN] This is an warning message. 
        Color displayed: Magenta
        """
        print(f"\033[91m[ERROR] {txt}\033[m")

