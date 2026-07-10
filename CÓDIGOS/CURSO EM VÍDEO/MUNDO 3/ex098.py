from time import sleep
from ex097 import title
def contador(start, end, step):
    intxt = start
    endtxt = end
    if start <= end:
        step = abs(step) if step > 0 or step < 0 else (step + 1)
        end += 1
    else:
        if step > 0 or step == 0:
            step = (step * -1) if step > 0 else (step - 1)
        end -= 1
    sleep(1)
    title(f'CONTAGEM DE {intxt} ATÉ {endtxt} DE {abs(step)} EM {abs(step)}')
    sleep(1)
    for c in range(start, end, step):
        sleep(0.15)
        print(c, end = ' ', flush = True)
    print()

contador(1, 10, 1)
contador(10, 1, 2)
print('\nSua vez de personalizar!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
contador(start, end, step)