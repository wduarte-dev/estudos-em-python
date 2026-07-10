# quando terminado a contagem, solta barulho, e no final da explosão mostra uma mensagem de boom
from pygame import mixer as reproduzir
reproduzir.init()
from time import sleep
for c in range (10, 0, -1):
    print(c)
    sleep(1)
reproduzir.music.load('fogos-de-artificio.mp3')
reproduzir.music.play()
sleep(5)
print('\033[31mBOOM!\033[0m')
sleep(1)
reproduzir.music.load('risada_quico.mp3')
reproduzir.music.play()
