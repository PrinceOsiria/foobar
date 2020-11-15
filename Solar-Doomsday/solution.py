def answer(area):
    solution = []
    area_remaining = area

    def is_area_remaining(area, area_remaining):
        while area_remaining > 0:
            return True

    while is_area_remaining(area, area_remaining):
        i = area
        while i > 0:
            square = i * i
            if square <= area_remaining:
                solution.append(square)
                area_remaining = area_remaining - square
            i = i - 1
    return (solution)