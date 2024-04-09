################################################################################
# +----------------------------------------------------------------------------+
# |                      Infraestrutura e Serviços de TI
# |                             ti@fundahc.com.br
# |----------------------------------------------------------------------------+
# | FUNDAHC
# |----------------------------------------------------------------------------+
# | Técnico  : Hudson Carvalho
# | Arquivo  : AutoStartCockpit.py
# | Objetivo : Automatizar início dos containers no cockpit do sitema TOTVS RM
# | Criado   : 01/04/2024
# | Alterado : 09/04/2024
# +----------------------------------------------------------------------------+
################################################################################

def banner():
	print("""

███████╗██╗░░░██╗███╗░░██╗██████╗░░█████╗░██╗░░██╗░█████╗░
██╔════╝██║░░░██║████╗░██║██╔══██╗██╔══██╗██║░░██║██╔══██╗
█████╗░░██║░░░██║██╔██╗██║██║░░██║███████║███████║██║░░╚═╝
██╔══╝░░██║░░░██║██║╚████║██║░░██║██╔══██║██╔══██║██║░░██╗
██║░░░░░╚██████╔╝██║░╚███║██████╔╝██║░░██║██║░░██║╚█████╔╝
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░

\033[94mInfraestrutura e Serviços de TI\033[0m

Técnico  : \033[96mHudson Carvalho\033[0m
Arquivo  : AutoStartCockpit.py
Objetivo : Automatizar início dos containers no cockpit do sitema TOTVS RM
Criado   : 01/04/2024
Alterado : \033[91m09/04/2024\033[0m

""")
banner()



import pyautogui
import time
import subprocess
from alive_progress import alive_bar            # Biblioteca de Barra de Progresso



program_path = r'C:\TOTVS\RM.NET\RM.exe'        # Caminho para o programa a ser iniciado



# Defina uma função para clicar em um determinado local na tela
def click_position(x, y):
    pyautogui.click(x, y)



# Espera 5 segundos entre cada ação para dar tempo para as janelas/carregamento
def wait():
    time.sleep(5)



# Função para abrir o programa e acompanhar o progresso
def open_program_with_progress():
    print("\033[96mAbrindo o programa...\033[0m")
    with alive_bar(2, title="Progresso", spinner="waves", bar="filling", enrich_print=False) as bar:
        bar(1)
        # Iniciar o programa
        subprocess.Popen(program_path)
        time.sleep(20)                          # Espera 20 segundos para a janela ser carregada parcialmente
        bar(1)
    print("Programa aberto completamente.")



# Função para abrir o programa e acompanhar o progresso
def login_with_progress():
    print("\033[96mLogando no RM...\033[0m")
    with alive_bar(2, title="Progresso", spinner="waves", bar="filling", enrich_print=False) as bar:
    # Fazer login
        bar(1)
        pyautogui.doubleClick(833, 381)         # Substitua pelas coordenadas do campo de usuário
        pyautogui.typewrite('user')  # Substitua pelo nome de usuário
        pyautogui.press('tab')
        pyautogui.typewrite('password')     # Substitua pela senha
        pyautogui.press('tab')
        pyautogui.press('C')                    # Substitua por H se for ambiente de Homologação | C para CorporeRM (Produção)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')                # Pressione Enter para logar
        time.sleep(35)                          # Espera 35 segundos para a janela ser carregada parcialmente
        bar(1)



# Função para acessar a área do cockpit e acompanhar o progresso
def cockpit_area_with_progress():
    print("\033[96mAcessando o Ambiente Cockpit...\033[0m")
    with alive_bar(2, title="Progresso", spinner="waves", bar="filling", enrich_print=False) as bar:
    # Navegar até a aba desejada
        bar(1)
        click_position(1110, 42)                # Aba Ambiente
        wait()
        click_position(173, 85)                 # Menu Cockpit
        time.sleep(15)
        bar(1)



def loop_cockpit(total_iterations):
    with alive_bar(total_iterations * 1, title="Progresso", spinner="waves", bar="filling", enrich_print=False) as bar:
        for i in range(total_iterations):
            print(f"\033[91mTratando BUG {i+1}\033[0m")
            # Loop para minimizar bug RM
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.press('enter')
            wait()
            click_position(1110, 42)                # Aba Ambiente
            wait()
            click_position(173, 85)                 # Menu Cockpit
            time.sleep(15)
            print(f"Tentativa {i+1} concluída")
            bar(1)
# Definir o número de iterações desejadas
num_iterations = 3



# Função para iniciar os containers e acompanhar o progresso
def container_area_with_progress():
    print("\033[96mIniciando containers...\033[0m")
    with alive_bar(4, title="Progresso", spinner="waves", bar="filling", enrich_print=False) as bar:
    # Iniciar os containers 
        click_position(22, 693)                 # Abre Container 8050
        click_position(318, 755)                # Stop Container
        time.sleep(10)
        click_position(184, 755)                # Start container 8050
        time.sleep(10)
        click_position(22, 693)                 # Close
        bar(1)
        print("\033[92mContainer 1 iniciado\033[0m")

        click_position(22, 397)                 # Abre Container 8052
        click_position(319, 465)                # Stop Container
        time.sleep(10)
        click_position(184, 465)                # Start container 8052
        time.sleep(10)
        click_position(22, 397)                 # Close
        bar(1)
        print("\033[92mContainer 2 iniciado\033[0m")

        click_position(418, 397)                # Abre Container 8056
        click_position(714, 465)                # Stop Container
        time.sleep(10)
        click_position(579, 465)                # Start container 8056
        time.sleep(10)
        click_position(418, 397)                # Close
        bar(1)
        print("\033[92mContainer 3 iniciado\033[0m")

        click_position(815, 397)                # Container 8054
        click_position(1112, 465)               # Stop Container
        time.sleep(10)
        click_position(974, 465)                # Start container 8054
        time.sleep(10)
        bar(1)
        print("\033[92mContainer 4 iniciado\033[0m")



# Chamada da função para abrir o programa
print("\033[91mAtenção:\033[0m \033[93mnão mexa o mouse e nem utilize o computador durante a execução da automação!\033[0m")
time.sleep(10)
open_program_with_progress()
# Chamada da função para login no RM
login_with_progress()
# Chamada da função Ambiente Cockpit
cockpit_area_with_progress()
# Chamada da função para executar o loop de cockpit com 3 iterações
loop_cockpit(num_iterations)
# Chamada da função Container Area
container_area_with_progress()



time.sleep(10)                                  # Esperar a tela dos containers carregar corretamente



# Fecha o RM
pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')
print("\033[92mRM encerrado!\033[0m")
time.sleep(10)                                  # Esperar encerrar o RM
print("\033[91mAutomação encerrada!\033[0m")