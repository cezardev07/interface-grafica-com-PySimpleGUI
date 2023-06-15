def layout(interface):
    
    layoutInterface = [
        [
            interface.Text('')
        ],
        [
            interface.Text('Email :'),
            interface.Input(key = 'name', size = (50,1))
        ],
        [
            interface.Text('Senha:'),
            interface.Input(key = 'senha', password_char = '*' , size = (50,1))
        ],
        [
            interface.Button('Login',size = (50,1))
        ],
        [
            interface.Text('Output:')
        ],
        [
            interface.Text('', key = 'usuario')
        ]
    ]

    return layoutInterface