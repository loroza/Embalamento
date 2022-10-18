import tkinter as tk
from tkinter import ttk
import datetime as dt
from dbfread import DBF
import pandas as pd

button_columnspan = 10
serie_pedido = 'P4'

dbf_vendedor = DBF('S:\\Sistemas\\D-1\\vendedor.dbf', encoding='unicode_escape')
df_vendedor = pd.DataFrame(dbf_vendedor)

filtro = df_vendedor[(df_vendedor['CODVEND'] == '2843')|
                     (df_vendedor['CODVEND'] == '4273')|
                     (df_vendedor['CODVEND'] == '4274')|
                     (df_vendedor['CODVEND'] == '3688')|
                     (df_vendedor['CODVEND'] == '4164')|
                     (df_vendedor['CODVEND'] == '4176')|
                     (df_vendedor['CODVEND'] == '4173')][['CODVEND', 'VENDEDOR']]

for i in filtro.index:
    filtro.loc[i, 'CONCAT'] = (filtro.loc[i, 'CODVEND'] +'|'+ filtro.loc[i, 'VENDEDOR'])

cod_mkp = []

for mkp in filtro['CONCAT']:
    market = mkp.split('|')
    cod_mkp.append(market)

lista_mktp = []

for marketplace in cod_mkp:
    lista_mktp.append(marketplace[1])

lista_mktp.sort()

df_embalamento = pd.DataFrame(columns=['PEDIDO_PEC', 'CODEMB', 'CODVEND', 'ETIQUETA', 'INICIO', 'FIM'])

lista_inicio = []
lista_final = []
lista_atual = []

config_font_bold = 'Helvetica 18 bold'
config_font_bold2 = 'Helvetica 10 bold'

def confirma():

    print(lista_atual)

    lista_inicio.clear()
    lista_final.clear()

    entry_pedido.delete(0, 'end')
    entry_shipping.delete(0, 'end')

    pedido_pec = str(entry_pedido.get())
    shipp_meli = str(entry_shipping.get())

    if pedido_pec == '':
        p_security = tk.Label(text=f'FAVOR INSERIR UM NOVO NÚMERO DO PEDIDO', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

        p_security = tk.Label(text=f'FAVOR INSERIR UM NOVO NÚMERO DO PEDIDO', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif shipp_meli == '':
        p_security = tk.Label(text=f'FAVOR INSERIR UM NOVO NÚMERO DA ETIQUETA', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

        p_security = tk.Label(text=f'FAVOR INSERIR UM NOVO NÚMERO DO PEDIDO', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    lista_atual.clear()


def finaliz_emb():

    finish_time = dt.datetime.now()
    finish_time = finish_time.strftime('%d/%m/%Y %H:%M:%S')
    opera_emba = str(entry_opera.get())
    pedido_pec = str(entry_pedido.get())
    shipp_meli = str(entry_shipping.get())
    marketplace= (list(df_vendedor[df_vendedor['VENDEDOR'] == str(combo_marketpl.get())]['CODVEND'])[0])

    if opera_emba == '':
        p_security = tk.Label(text=f'FAVOR INSERIR O CÓDIGO DO OPERADOR', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif pedido_pec == '':
        p_security = tk.Label(text=f'FAVOR INSERIR O NÚMERO DO PEDIDO', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif shipp_meli == '':
        p_security = tk.Label(text=f'FAVOR INSERIR O NÚMERO DA ETIQUETA', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif marketplace == '':
        p_security = tk.Label(text=f'FAVOR INFORMAR O MARKETPLACE DA ETIQUETA', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    else:

        embala = tk.Label(text=f'FINALIZADO: {finish_time}', background='#c9ffe1', foreground='#00b050')
        embala.grid(row=19, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        embala.configure(font=config_font_bold)

        botao_check = tk.Button(text='Confirmar', background='#00b050', foreground='#fff', command=confirma)
        botao_check.grid(row=21, column=8, padx=10, pady=10, sticky='nswe', columnspan=2)

        lista_final.append((pedido_pec, opera_emba, marketplace, shipp_meli, finish_time))

        pos = 0

        for registro in lista_inicio:
            lista_atual.append((registro[0], registro[1], registro[2], registro[3], registro[4], lista_final[pos][4]))
            pos = pos + 1

def iniciar_emb():

    start_time = dt.datetime.now()
    start_time = start_time.strftime('%d/%m/%Y %H:%M:%S')
    opera_emba = str(entry_opera.get())
    pedido_pec = str(entry_pedido.get())
    shipp_meli = str(entry_shipping.get())
    marketplace= (list(df_vendedor[df_vendedor['VENDEDOR'] == str(combo_marketpl.get())]['CODVEND'])[0])

    if opera_emba == '':
        p_security = tk.Label(text=f'FAVOR INSERIR O CÓDIGO DO OPERADOR', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif pedido_pec == '':
        p_security = tk.Label(text=f'FAVOR INSERIR O NÚMERO DO PEDIDO', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif shipp_meli == '':
        p_security = tk.Label(text=f'FAVOR INSERIR O NÚMERO DA ETIQUETA', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    elif marketplace == '':
        p_security = tk.Label(text=f'FAVOR INFORMAR O MARKETPLACE DA ETIQUETA', background='#c9ffe1', foreground='#00b050')
        p_security.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_security.configure(font=config_font_bold2)

    else:
        p_block_opera = tk.Label(text=((list(df_vendedor[df_vendedor['CODVEND'] == opera_emba]['VENDEDOR'])[0]).split(' ')[0]) + ' ' + ((list(df_vendedor[df_vendedor['CODVEND'] == opera_emba]['VENDEDOR'])[0]).split(' ')[1]), background='#c9ffe1')
        p_block_opera.grid(row=1, column=10, padx=10, pady=10, sticky='nswe', columnspan=3)
        p_block_opera.configure(font=config_font_bold2)

        # p_block_pedido = tk.Label(text=serie_pedido + '-' + pedido_pec, background='#c9ffe1')
        # p_block_pedido.grid(row=3, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)
        #
        # p_block_shipp = tk.Label(text=shipp_meli, background='#c9ffe1')
        # p_block_shipp.grid(row=5, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)
        #
        # p_block_market = tk.Label(text=marketplace, background='#c9ffe1')
        # p_block_market.grid(row=7, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)

        p_start_time = tk.Label(text=f'INICIADO: {start_time}', background='#c9ffe1', foreground='#00b050')
        p_start_time.grid(row=13, column=0, padx=20, pady=20, sticky='nswe', columnspan=button_columnspan)
        p_start_time.configure(font=config_font_bold)

        botao_finish = tk.Button(text='Finalizar o embalamento', command=finaliz_emb)
        botao_finish.grid(row=17, column=0, padx=10, pady=10, sticky='nswe', columnspan=button_columnspan)

        lista_inicio.append((pedido_pec, opera_emba, marketplace, shipp_meli, start_time))

                ########################################################################################

if __name__ == '__main__':

    janela = tk.Tk()
    janela.title('Embalamento de pedidos')
    janela.geometry('650x500')
    janela.configure(background='#c9ffe1')

    label_opera = tk.Label(text='INSIRA O SEU CÓDIGO DE OPERADOR', background='#c9ffe1')
    label_opera.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
    label_opera.configure(font=config_font_bold2)

    entry_opera = tk.Entry()
    entry_opera.grid(row=1, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)

    ####################################################################################################################

    label_pedido = tk.Label(text='INSIRA O NÚMERO PEDIDO PECISTA', background='#c9ffe1')
    label_pedido.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
    label_pedido.configure(font=config_font_bold2)

    label_serie = tk.Label(text=serie_pedido, background='#c9ffe1', foreground='#00b050')
    label_serie.grid(row=3, column=5, padx=10, pady=10, sticky='nswe', columnspan=1)
    label_serie.configure(font=config_font_bold2)

    entry_pedido = tk.Entry()
    entry_pedido.grid(row=3, column=6, padx=10, pady=10, sticky='nswe', columnspan=3)

    ####################################################################################################################

    label_shipping = tk.Label(text='INSIRA O CÓDIGO DA ETIQUETA', background='#c9ffe1')
    label_shipping.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
    label_shipping.configure(font=config_font_bold2)

    entry_shipping = tk.Entry()
    entry_shipping.grid(row=5, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)

    ####################################################################################################################

    label_marketpl = tk.Label(text='INFORME O MARKETPLACE DA ETIQUETA', background='#c9ffe1')
    label_marketpl.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
    label_marketpl.configure(font=config_font_bold2)

    combo_marketpl = ttk.Combobox(values=lista_mktp)
    combo_marketpl.grid(row=7, column=5, padx=10, pady=10, sticky='nswe', columnspan=4)

    ####################################################################################################################

    botao_start = tk.Button(text='Iniciar o embalamento', command=iniciar_emb)
    botao_start.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=button_columnspan)

    janela.mainloop()