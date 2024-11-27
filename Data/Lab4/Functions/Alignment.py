def apply_alignment(line, width, alignment):
    if alignment == "left":
        return line.ljust(width)
    elif alignment == "center":
        return line.center(width)
    elif alignment == "right":
        return line.rjust(width)
