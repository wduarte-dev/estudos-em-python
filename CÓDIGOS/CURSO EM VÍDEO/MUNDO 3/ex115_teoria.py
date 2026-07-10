# with open('ex115_teste.txt', 'r') as file:              # 'r' significa 'read'
#     for i, line in enumerate(file):               # i -> Número da linha, line -> Conteúdo da linha
#         print('Linha', i+1, '---->', line, end ='') # EXIBE O ARQUIVO LINHA A LINHA
#     text = file.read() # LÊ O ARQUIVO INTEIRO
#     print(text)        # EXIBE O CONTEÚDO

# with open('ex115_teste.txt', 'w') as file:    # 'w' significa 'write', é importante ressaltar
#                                         # que todo conteúdo do arquivo será apagado.
#     file.write('Essa linha foi escrita via código!\n')
#     file.write('E essa linha também!\n')
#     file.write('Mas tudo que estava escrito no arquivo foi embora!\n')

# with open('ex115_teste.txt', 'a') as file: # 'a' significa 'append'.  O conteúdo do arquivo não
#                                      # é removido, apenas adicionado.
#     text = file.write('Adicionei esse texto sem remover nada do arquivo!')
