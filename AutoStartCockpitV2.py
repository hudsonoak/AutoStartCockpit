################################################################################
# +----------------------------------------------------------------------------+
# |                      Infraestrutura e Serviços de TI
# |                             ti@fundahc.com.br
# |----------------------------------------------------------------------------+
# | FUNDAHC
# |----------------------------------------------------------------------------+
# | Tecnico  : Hudson Carvalho
# | Arquivo  : AutoStartCockpit.py
# | Objetivo : Automatizar início dos containers no cockpit do sitema TOTVS RM
# | Criado   : 01/04/2024
# | Alterado : 01/04/2024
# +----------------------------------------------------------------------------+
################################################################################
# Documentação de uso #
# Para utilizar este script, necessário ter as seguintes dependências instaladas:
# - Python em sua última versão instalado na máquina que irá executar;
# - pyautogui (Comando para instalação: pip install pyautogui);
# - pyscreeze (Comando para instalação: pip install pyscreeze);
# 
# Caso necessário atualizar alguma dependência, basta utilizar o comando:
# > pip install --upgrade nomeDaDependencia


import pyautogui
import time
import subprocess


# Caminho para o programa a ser iniciado
program_path = r'C:\totvs\CorporeRM\RM.Net\RM.exe'
# Iniciar o programa
subprocess.Popen(program_path)
# Espera 10 segundos para a janela ser carregada completamente
time.sleep(10)

# Variáveis #
# Defina uma função para clicar em um determinado local na tela
def click_position(x, y):
    pyautogui.click(x, y)
# Espera 5 segundos entre cada ação para dar tempo para as janelas/carregamento
def wait():
    time.sleep(5)

# Esperar a janela ser carregada
time.sleep(10)

# Fazer login
pyautogui.doubleClick(833, 381)         # Substitua pelas coordenadas do campo de usuário
pyautogui.typewrite('user')           # Substitua pelo nome de usuário
pyautogui.press('tab')
pyautogui.typewrite('password')        # Substitua pela senha
pyautogui.press('tab')
pyautogui.press('C')                    # Substitua por H se for ambiente de Homologação | C para CorporeRM (Produção)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')                # Pressione Enter para logar

# Esperar o login ser concluído
time.sleep(20)

# Navegar até a aba desejada
click_position(1110, 42)                # Aba Ambiente
click_position(173, 85)                 # Menu Cockpit

# Esperar a aba ser carregada
time.sleep(15)

# Iniciar os containers
click_position(22, 693)                 # Abre Container 8050
click_position(184, 755)                # Start container 8050
wait()
click_position(22, 693)                 # Close

click_position(22, 397)                 # Abre Container 8052
click_position(184, 465)                # Start container 8052
wait()
click_position(22, 397)                 # Close

click_position(418, 397)                # Abre Container 8056
click_position(579, 465)                # Start container 8056
wait()
click_position(418, 397)                # Close

click_position(815, 397)                # Container 8054
click_position(974, 465)                # Start container 8054
wait()

# Esperar a inicialização dos containers
time.sleep(10)

# Fecha o RM
pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')