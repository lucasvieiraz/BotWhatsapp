import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook ['Página1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    mensagem = f"Olá {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.lucasvieiraz.com.br "
    
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

webbrowser.open(link_mensagem_whatsapp)
sleep(10)

try:
    seta = pyautogui.locateCenterOnScreen('seta.png')
    sleep(10)
    pyautogui.click(seta[0], seta [1])
    sleep(10)

    pyautogui.hotkey('ctrl', 'w')
    sleep(10)
except:
    print(f'Não foi possivel enviat mensagem para {nome} ')
    with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome}, {telefone} ')
