from .auth.auth import auth

def event(janela, interface):
    while True:
        events, values = janela.read()
        if events == interface.WINDOW_CLOSED:
            break
        
        auth(janela, values)
