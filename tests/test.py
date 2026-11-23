import os
import sys

sys.stdout.reconfigure(encoding='utf-8')  # console cp1252 no Windows nao imprime as setas

pasta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(pasta_raiz)

import logandprint as log
log.debugMode(True)

log.write('Teste')
log.info('Teste')
log.error('Teste')
log.success('Teste')
log.warning('Teste')
log.debug('Teste')

log.export_to_csv()



teste = 'teste'
print('\033[91m ERROR \033[0m') #Vermelho brilhante
print('\033[93m WARNING \033[0m') #Amarelo
print('\033[92m SUCCESS \033[0m') #Verde
print('\033[96m DEBUG \033[0m') #Ciano
print('\033[5;41m CRITICAL \033[0m') #Vermelho piscante
print('\033[91m CRITICAL \033[0m')  # Vermelho brilhante
print('\033[41m\033[97m CRITICAL \033[0m')  # Background vermelho, texto branco
print('\033[1;31m CRITICAL \033[0m')  # Negrito vermelho
print('\033[4;31m CRITICAL \033[0m')  # Sublinhado vermelho
print('-----------')
print('\033[1;31m\u2193 CRITICAL \u2193\033[0m')
print('\033[1;31m', '\u2193' * 10, '\033[5;41m CRITICAL \033[0m\033[1;31m', '\u2193' * 10, '\033[0m')
print('\033[91m Essa é uma mensagem crítica para o sistema \033[0m')
print('\033[1;31m', '\u2191' * 32, '\033[0m')
print('\u2193' * 10)  # Seta para baixo
print('\u2191' * 10)  # Seta para cima
