# -*- coding: utf-8 -*-
'''
autor: José Jasnau Caeiro
date:4 de Outubro de 2012
obs: soma de um par de hexadecimais
'''

#declaração de duas variáveis de tipo 'str'
a = '0xa' #representação correspondente ao número inteiro 10
b = '0xb' #representação correspondente ao número inteiro 11

#conversão da representação em termo de 'str' em inteiro
# escolhendo a base hexadecimal 16
base = 16
a_int = int(a, base)
b_int = int(b,base)

#soma dos inteiros resultantes
c_int = a_int + b_int

#conversão na representação hexadecimal em termos de 'str'
c = hex (c_int)
#impressão no ecrã do resultado
print c

#representação do número binário correspondente a
b = '0b11110001'

#conversão para hexadecimal e impressão no ecrã
print hex(int(b,2))
