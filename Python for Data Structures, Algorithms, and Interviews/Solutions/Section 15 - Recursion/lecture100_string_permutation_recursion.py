def permute(s):
    out = []

    # Base case
    if len(s) == 1:
        out = [s]

    else:
        # for every letter in string
        for i, let in enumerate(s):
            print(f'i: {i} \nlet: {let}\n')
            # for every permutation resulting from steps 2-3 described above
            for perm in permute(s[:i] + s[i+1:]):
                # print(f's: {s}\n')
                # print(f'perm: {perm}\n')
                print(f's[:i]: {s[:i]}\n')
                print(f's[i+1]: {s[i+1:]}\n')
                input('continua')

                # Add it to the output
                out += [let + perm]
                print(f'let + perm: {let + perm}\n')
                input('continua')

    return out
