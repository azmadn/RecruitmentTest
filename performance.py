def intersect(bagA, bagB):
    setB = set(bagB)  # Mengubah bagB menjadi set untuk pencarian yang lebih cepat
    result = []
    for o in bagA:
        if o in setB:  # Menggunakan setB untuk pencarian
            result.append(o)
    return result
