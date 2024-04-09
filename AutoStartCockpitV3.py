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
# | Alterado : 02/04/2024
# +----------------------------------------------------------------------------+
################################################################################
# Documentação de uso #
# Para utilizar este script, necessário ter as seguintes dependências instaladas:
# - Python em sua última versão instalado na máquina que irá executar;
# - pyautogui       (Comando para instalação: pip install pyautogui);
# - pyscreeze       (Comando para instalação: pip install pyscreeze);
# - pytesseract     (Comando para instalação: pip install pytesseract);
# - pillow          (Comando para instalação: pip install pillow);
# - opencv-python   (Comando para instalação: pip install opencv-python-headless);
# 
# Caso necessário atualizar alguma dependência, basta utilizar o comando:
# > pip install --upgrade nomeDaDependencia


import pyautogui
import time
import subprocess
import cv2
import numpy as np
import pytesseract
import time
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Caminho para o programa a ser iniciado
program_path = r'C:\TOTVS\RM.NET\RM.exe'
# Iniciar o programa
subprocess.Popen(program_path)
# Espera 10 segundos para a janela ser carregada completamente
time.sleep(10)

######################### Variáveis #########################
# Defina uma função para clicar em um determinado local na tela
def click_position(x, y):
    pyautogui.click(x, y)
# Espera 5 segundos entre cada ação para dar tempo para as janelas/carregamento
def wait():
    time.sleep(5)

# Esperar a janela ser carregada
time.sleep(10)

######################### Variáveis OCR #########################
# Função para processar a imagem e extrair texto usando OCR
def extract_text_from_image(image_path):
    # Carregar a imagem usando o OpenCV
    image = cv2.imread(image_path)

    # Converter a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar thresholding para binarizar a imagem
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Extrair texto da imagem usando OCR
    extracted_text = pytesseract.image_to_string(threshold_image)

    return extracted_text

######################### Tela de Login #########################
# Função para localizar campos e botões na tela de login e interagir com eles
def login_to_system():
    # Caminho para a pasta contendo as imagens
    images_folder = 'dependences/img/'

    # Carregar a imagem da tela de login
    login_image_path = images_folder + 'login.png'

    # Extrair texto da imagem da tela de login
    extracted_text = extract_text_from_image(login_image_path)

    # Detectar e interagir com os campos de entrada e botões
    if 'Insira seu Usuário ou E-mail' in extracted_text:
        # Localizar o campo de usuário
        user_field_position = pyautogui.locateCenterOnScreen(images_folder + 'login_campo_usuario.png')

        # Preencher o campo de usuário
        if user_field_position:
            pyautogui.click(user_field_position)
            pyautogui.typewrite('user')               # Defina o Usuário à ser utilizado

    if 'Insira sua senha' in extracted_text:
        # Localizar o campo de senha
        password_field_position = pyautogui.locateCenterOnScreen(images_folder + 'login_campo_senha.png')

        # Preencher o campo de senha
        if password_field_position:
            pyautogui.click(password_field_position)
            pyautogui.typewrite('password')            # Defina a senha do usuário

    if 'Alias' in extracted_text:
        # Localizar o campo de Alias
        alias_field_position = pyautogui.locateCenterOnScreen(images_folder + 'login_campo_alias.png')

        # Selecionar o CorporeRM no campo de Alias
        if alias_field_position:
            pyautogui.click(alias_field_position)
            pyautogui.typewrite('C')

    # Localizar e clicar no botão Entrar
    enter_button_position = pyautogui.locateCenterOnScreen(images_folder + 'login_botao_entrar.png')

    if enter_button_position:
        pyautogui.click(enter_button_position)

######################### Tela home #########################
# Função para clicar na aba "Ambiente"
def click_ambiente_tab():
    # Esperar um momento para garantir que a interface seja atualizada
    time.sleep(2)
    
    # Caminho para a pasta contendo as imagens
    images_folder = 'dependences/img/'

    # Localizar a posição do botão "Ambiente" com base na cor RGB
    ambiente_button_position = pyautogui.locateCenterOnScreen(images_folder + 'ambiente_button.png', confidence=0.9, region=(0, 0, 1920, 1080))

    # Se o botão "Ambiente" for encontrado, clicar nele
    if ambiente_button_position:
        pyautogui.click(ambiente_button_position)
    else:
        print("Botão 'Ambiente' não encontrado.")

# Função para clicar no botão "Cockpit"
def click_cockpit_button():
    # Esperar um momento para garantir que a interface seja atualizada após clicar em "Ambiente"
    time.sleep(2)

    # Caminho para a pasta contendo as imagens
    images_folder = 'dependences/img/'

    # Localizar a posição do botão "Cockpit" com base na cor RGB
    cockpit_button_position = pyautogui.locateCenterOnScreen(images_folder + 'cockpit_button.png', confidence=0.9, region=(0, 0, 1920, 1080))

    # Se o botão "Cockpit" for encontrado, clicar nele
    if cockpit_button_position:
        pyautogui.click(cockpit_button_position)
    else:
        print("Botão 'Cockpit' não encontrado.")

######################### Tela Cockpit #########################
# Função para verificar se todos os elementos necessários foram carregados na tela do Cockpit
def check_elements_loaded(retries=5):
    for _ in range(retries):
        # Verificar se todos os elementos necessários estão presentes na tela
        if pyautogui.locateOnScreen(images_folder + 'vermelho.png', confidence=0.9, region=(0, 0, 1920, 1080)):
            # Se os elementos estiverem carregados, esperar 8 segundos
            time.sleep(8)
            return True
        else:
            # Fechar a tela do Cockpit
            close_cockpit()

            # Esperar um pouco antes de tentar novamente
            time.sleep(10)
    return False

# Função para fechar a tela do Cockpit
def close_cockpit():
    # Fechar a tela do Cockpit
    pyautogui.hotkey('ctrl', 'w')

    # Localizar e clicar no botão de fechar a tela do Cockpit
    close_button_position = pyautogui.locateCenterOnScreen(images_folder + 'cockpit_close_button.png', confidence=0.9, region=(0, 0, 1920, 1080))
    if close_button_position:
        pyautogui.click(close_button_position)

######################### Execução #########################
# Espera 10 segundos para o programa ser iniciado e a tela de login estar visível
time.sleep(10)

# Realizar login no sistema
login_to_system()

# Esperar o login ser concluído
time.sleep(20)

# Clicar na aba "Ambiente"
click_ambiente_tab()

# Clicar no botão "Cockpit"
click_cockpit_button()

# Esperar 10 segundos para o cockpit
time.sleep(10)

# Aguardar bug dos containers
check_elements_loaded()




























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