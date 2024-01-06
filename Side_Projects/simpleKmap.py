def simplify_kmap(kmap: list[list[int]]) -> str:
    simplified_f = []
    for a, row in enumerate(kmap):
        for b, item in enumerate(row):
            if item:
                term = ("A" if a else "A'") + ("B" if b else "B'")
                simplified_f.append(term)
    return " + ".join(simplified_f)


if __name__ == "__main__":
    kmap = [[1, 1], [1, 1]]
    # Manually generate the product of [0, 1] and [0, 1]
    for row in kmap:
        print(row)

    print("Simplified Expression:")
    kMap = simplify_kmap(kmap)
    print(f"The simplified kmap: {kMap}")