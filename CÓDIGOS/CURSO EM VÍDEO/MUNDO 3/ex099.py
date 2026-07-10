def maior(*args):
    args_list = []
    print('-'*(40 + len(args)*2))
    print('Analisando os valores passados...')
    print(f'Foram {len(args)} valores ao todo, sendo eles:', end = ' ')
    for num in args:
        args_list.append(str(num))
    print(', '.join(args_list), end = ' ')
    # for num in args:
    #     print(num, end = ' ')
    try:
        print(f'\nO maior valor informado foi {max(args)}')
    except ValueError:
        print(f'\nNão há nenhum valor para ser comparado.')
    print('-'*(40 + len(args)*2))
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()