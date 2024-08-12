import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=804, y=377)
pyautogui.write("guilherme.santos300106@gmail.com")
pyautogui.press("tab")
pyautogui.write("gui30061206")

pyautogui.click(x=972, y=533)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:

    pyautogui.click(x=725, y=258)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")

    pyautogui.write(custo)



    pyautogui.press("tab")
    obs= str(tabela.loc[linha, "obs"])
    #Só ira executar o comando caso obs seja diferente de nan, caso contrario só passara para o proximo
    if obs != "nan":
       pyautogui.write(obs)


    pyautogui.press("tab")
    pyautogui.press("enter")


    pyautogui.scroll(5000)
