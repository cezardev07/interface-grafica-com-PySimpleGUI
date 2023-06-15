def auth(janela, values):
    if values['name'] == 'dev@gmail.com' and values['senha'] == '123':
        janela['usuario'].update(f'welcome!')

    if values['name'] == "dev@gmail.com" and values['senha'] != "123":
        janela['usuario'].update('senha incorreta')

    if values['name'] != "dev@gmail.com":
        janela['usuario'].update('usuario não encontrado')

    if values['name'] == "" or values['senha'] == "":
        janela['usuario'].update('complete o formulario')