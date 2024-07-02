class MyClass:
    def __init__(self) -> None:
        self.l = list(range(10))
        print("initialized")

    def print_list(self) -> None:
        print(*self.l)
