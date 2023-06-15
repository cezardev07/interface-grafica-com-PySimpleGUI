import PySimpleGUI as interface

from layout.layout import layout
from event.event import event

interface.theme('Reddit')

layoutInterface = layout(interface)

janela = interface.Window('Login', layoutInterface)

event(janela, interface)

janela.close()