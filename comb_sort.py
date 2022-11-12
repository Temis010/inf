def comb(massiv):
    gap = len(massiv)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.27))
        swaps = False
        for i in range(len(massiv) - gap):
            j = i + gap
            if massiv[i] > massiv[j]:
                massiv[i], massiv[j] = massiv[j], massiv[i]
                swaps = True
    return massiv
