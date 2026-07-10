def title(str):
    centralizer = len(str) + 2
    separator = '~'
    print()
    print(separator*(centralizer))
    print(f'{str:^{centralizer}}')
    print(separator*(centralizer))