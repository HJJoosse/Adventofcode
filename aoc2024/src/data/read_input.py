class InputReader:

    def __init__(self,path_to_input) -> None:
        self.path_to_input = path_to_input

    def load_splitlines(self) -> list:
        with open(self.path_to_input,"r") as f:
            data = f.readlines()

        return data