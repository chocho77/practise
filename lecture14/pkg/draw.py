class DrawFigure:

    def __init__(self) -> None:
        pass

    def draw_figure(self, symbol, size):
        print(size * symbol)
        for i in range(size):
            print(symbol, end="")
            print((size - 2) * " ", end="")
            print(symbol)
        print(size * symbol)
    

    

