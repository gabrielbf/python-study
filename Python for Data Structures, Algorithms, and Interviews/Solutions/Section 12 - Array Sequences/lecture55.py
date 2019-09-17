def finder_errado(arr, arr2):
    if not arr and arr2:
        return

    return [item for item in arr if item not in arr2]


def finder(arr, arr2):
    # edge cases
    if not arr and arr2:
        return

    if len(arr) != (len(arr2) + 1):
        return

    resposta = arr.copy()
    for item in arr:
        if item in arr2:
            resposta.remove(item)
            arr2.remove(item)

    return resposta


def finder_dict(arr, arr2):
    # edge cases
    if not (arr and arr2):
        return

    if len(arr) != (len(arr2) + 1):
        return

    dicio = {}

    for item in arr:
        if item in dicio:
            dicio[item] += 1
        else:
            dicio[item] = 1

    for item in arr2:
        if item in dicio:
            dicio[item] -= 1
        else:
            return  # tem um item em arr2 que não tem em arr

    return [key for key, value in dicio.items() if value > 0]
