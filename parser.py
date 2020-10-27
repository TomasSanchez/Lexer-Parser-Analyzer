import lexer
from producciones import *


def Parser(inputString):
    self = {
        'tokens': lexer.tokenize(inputString),
        'index': 0,
        'error': False,
    }

    def parse():
        pni('Programa')
        token_actual = self['tokens'][self['index']]
        if token_actual.lexeme == 'EOF' and self['error'] == False:
            return True
        else:
            return False

    def es_terminal(simbolo):
        return simbolo not in no_terminales


    def procesar(parteDerecha):
        token_apuntado = self['tokens'][self['index']]
        indice = self['index']
        for simbolo in parteDerecha:
            token_apuntado = self['tokens'][self['index']]
            if simbolo not in no_terminales:
                if simbolo.kind == token_apuntado.kind:
                    self['index'] += 1 
                    indice = self['index']
                else:
                    self['error'] = True
                    break
            else:
                pni(simbolo)
                if self['error']:
                    break


    def pni(noTerminal):
        for parteDerecha in producciones[noTerminal]:
            self['error'] = False
            pivot = self['index']
            procesar(parteDerecha)
            if self['error']:
                self['index'] = pivot
            else:
                break

    return parse()

