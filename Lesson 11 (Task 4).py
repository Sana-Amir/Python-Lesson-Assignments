import datetime as xy

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

        # write msg to the file
        with open("logs.txt", "a") as f:
            f.write(f"[{xy.datetime.now()}]: {msg}\n")

raise CustomException("Custom Exception!")