from pieces import __all__

_TYPE_MAP = {
    '▣': Pharaoh,
    '/': Djed,
    '\\': Djed,
    '◪': Pyramid,
    '⬕': Pyramid,
    '⬔': Pyramid,
    '◩': Pyramid,
    '▨': Obelisk,
    '▩': Obelisk
}

class PieceFactory:
    def create(piece):
        color = piece[0]
        char = piece[1]
            
        activator = _TYPE_MAP.get(char)
        piece = activator(char, color)
        return piece
        
