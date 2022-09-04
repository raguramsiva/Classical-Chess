from src.colour import colour

class Theme:

    def __init__(self, light_bg, dark_bg, 
                       light_trace, dark_trace,
                       light_moves, dark_moves):
        
        self.bg = colour(light_bg, dark_bg)
        self.trace = colour(light_trace, dark_trace)
        self.moves = colour(light_moves, dark_moves)