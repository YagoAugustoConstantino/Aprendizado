import pyautogui as pa
import pyperclip
import pandas as pd
import time

pd.set_option('display.expand_frame_repr', False)

time.sleep(2)

print(pa.position())

pa.PAUSE = 1
pa.press('win')
pa.write('chrome')
pa.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pa.hotkey('ctrl', 'v')
pa.press('enter')
time.sleep(3)
pa.click(x=407, y=305, clicks=2)
time.sleep(2)
pa.click(x=407, y=305, clicks=2)
time.sleep(1)
pa.click(x=273, y=51)
pa.hotkey('ctrl', 'c')
time.sleep(1)
pa.click(x=423, y=743)

time.sleep(2)

ler_arquivo = pd.read_excel(r'..\ARQUIVOS\Vendas - Dez.xlsx')
tabela = pd.DataFrame(ler_arquivo)
print(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
print(faturamento)
print(quantidade)
