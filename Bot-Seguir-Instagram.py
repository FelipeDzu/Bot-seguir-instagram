import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException

import pyautogui
import os
import datetime
from datetime import datetime

# Perguntar ao usuário quantos perfis deseja seguir
while True:
    try:
        quantidade_para_seguir = int(
            input("Quantos perfis você deseja seguir nesta execução? (1-100): ")
        )
        if 1 <= quantidade_para_seguir <= 100:
            if quantidade_para_seguir > 50:
                print(
                    "⚠️ Atenção: Seguir mais de 50 perfis pode aumentar o risco de bloqueio da conta."
                )
            break
        else:
            print("❌ Por favor, insira um número entre 1 e 100.")
    except ValueError:
        print("❌ Entrada inválida! Por favor, insira um número válido.")


iniciar_tempo = time.time()


# Função para fechar pop-ups de notificação
def fechar_popup_notificacao(driver):
    try:
        botao_not_now = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(text(), 'Not Now') or contains(text(), 'Agora não') or contains(text(), 'Fechar') or contains(text(), 'Nunca')]",
                )
            )
        )
        botao_not_now.click()
        print("✔️ Pop-up de notificação fechado.")
    except:
        pass  # Nenhum pop-up encontrado, continuar


# Dados do usuário
USUARIO_INSTAGRAM = ""
SENHA_INSTAGRAM = ""
CONCORRENTE = ""

# Inicia o navegador em modo stealth
driver = uc.Chrome()

driver.maximize_window()

# 1️⃣ Acessar Instagram e fazer login
print("🔓 Abrindo Instagram...")
driver.get("https://www.instagram.com/accounts/login/")

# Esperar os campos de login aparecerem
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    print("📝 Preenchendo dados de login...")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys(USUARIO_INSTAGRAM)
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys(SENHA_INSTAGRAM)
    time.sleep(2)
    print("🚀 Clicando no botão de login...")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)  # Tempo extra para carregar a página inicial
except Exception as e:
    print(f"❌ Erro ao fazer login: {e}")

# Fechar pop-ups de notificação
try:
    botao_not_now = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(text(), 'Not Now') or contains(text(), 'Agora não') or contains(text(), 'Fechar')]",
            )
        )
    )
    print("🔕 Fechando pop-up de notificação...")
    botao_not_now.click()
except Exception as e:
    print(f"✅ Nenhum pop-up encontrado ou erro ao fechar: {e}")
time.sleep(3)

# 2️⃣ Acessar a página do concorrente
try:
    print(f"📂 Acessando o perfil do concorrente {CONCORRENTE}...")
    driver.get(f"https://www.instagram.com/{CONCORRENTE}/")
    time.sleep(2)
    # Esperar a página carregar completamente
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//header"))
    )
except Exception as e:
    print(f"❌ Erro ao acessar o perfil do concorrente: {e}")

# Clicar no botão de "seguidores"
try:
    print("📊 Clicando no botão de seguidores...")
    seguidores_button = driver.find_element(
        By.XPATH, "//a[contains(@href, '/followers/')]"
    )
    seguidores_button.click()
except Exception as e:
    print(f"❌ Erro ao clicar no botão de seguidores: {e}")


# 4️⃣ Esperar o carregamento da lista de seguidores
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
)

# Fechar pop-ups de notificação novamente
# fechar_popup_notificacao(driver)

# 5️⃣ Encontrar o elemento com a classe específica e mover o mouse até ele
classes = "xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6"
# Transformando o valor das classes em um seletor CSS
seletor_css = "." + ".".join(classes.split())

# Encontrar o elemento com as classes especificadas
elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, seletor_css))
)

# 6️⃣ Mover o mouse até esse elemento
actions = ActionChains(driver)
actions.move_to_element(elemento).perform()

# Fechar pop-ups de notificação
fechar_popup_notificacao(driver)

# 7️⃣ Rolar para baixo dentro do elemento
for _ in range(5):  # Rolar 10 vezes (ajuste conforme necessário)
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", elemento
    )
    time.sleep(random.uniform(6, 11))  # Espera para imitar ação humana


# # 3️⃣ Esperar o carregamento da lista de seguidores
# try:
#     print("🔎 Esperando o carregamento da lista de seguidores...")
#     # Garantir que a janela/modal de seguidores apareceu
#     WebDriverWait(driver, 1).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
#     )
# except Exception as e:
#     print(f"❌ Erro ao carregar a lista de seguidores: {e}")

# # Pausar entre as ações do pyautogui para maior segurança
# pyautogui.PAUSE = 1

# time.sleep(2)
# pyautogui.scroll(-800)

# time.sleep(2)
# pyautogui.scroll(-800)

# time.sleep(10)

# Tentar rolar para baixo para garantir que todos os seguidores sejam carregados
# try:
#     dialog = driver.find_element(By.XPATH, "//div[@role='dialog']")
#     for _ in range(3):  # Rolando 3 vezes para carregar mais seguidores
#         driver.execute_script(
#             "arguments[0].scrollTop = arguments[0].scrollHeight", dialog
#         )
#         time.sleep(2)  # Espera para garantir que os seguidores carreguem
# except Exception as e:
#     print(f"❌ Erro ao rolar a lista de seguidores: {e}")


# Coletar os seguidores (do 50º ao 100º, por exemplo)
seguidores = driver.find_elements(
    By.XPATH, "//div[@role='dialog']//a[contains(@href, '/')]"
)
seguidores_lista = [
    s.get_attribute("href") for s in seguidores[0:1000]
]  # Ajuste a faixa conforme necessário

print(f"📌 Encontrados {len(seguidores_lista)} seguidores.")

# Carregar a lista de perfis já seguidos
try:
    with open("seguindo_perfis.txt", "r") as file:
        perfis_seguidos = set(file.read().splitlines())
except FileNotFoundError:
    perfis_seguidos = set()

# 8 Mostrar todos os links coletados e verificar se já foram seguidos
print("\n🔍 Lista de perfis coletados:")
for link in seguidores_lista:
    if link in perfis_seguidos:
        print(f"🚫 Você já segue esse perfil: {link}")
    else:
        print(f"✅ Você pode seguir esse perfil: {link}")

# 9 Filtrar seguidores que ainda não foram seguidos
seguidores_nao_seguidos = [s for s in seguidores_lista if s not in perfis_seguidos]
print(f"\n🎯 {len(seguidores_nao_seguidos)} seguidores disponíveis para seguir.")

# 10 Escolher seguidores aleatórios dos disponíveis
seguidores_escolhidos = random.sample(
    seguidores_nao_seguidos, min(6, len(seguidores_nao_seguidos))
)
print(f"🎯 Selecionados {len(seguidores_escolhidos)} seguidores para seguir.")

contador = 0
for seguidor in seguidores_escolhidos:
    if contador >= quantidade_para_seguir:
        print("✅ Limite de usuários para seguir atingido.")
        break

    print(f"\n🚪 Acessando perfil: {seguidor}")

    try:
        driver.get(seguidor)
        time.sleep(5)

        try:
            print("🔎 Verificando botão de seguir...")

            # Primeira tentativa: Buscar por `aria-label="Seguir"`
            try:
                seguir_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button[aria-label='Seguir']")
                    )
                )
                print("✔️ Botão de seguir encontrado por CSS_SELECTOR!")
            except TimeoutException:
                print(
                    "❌ Botão de seguir não encontrado por CSS_SELECTOR, tentando outra abordagem..."
                )

                # Segunda tentativa: Buscar por XPath contendo 'Seguir' ou 'Follow'
                try:
                    seguir_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                "//button[contains(., 'Seguir') or contains(., 'Follow')]",
                            )
                        )
                    )
                    print("✔️ Botão de seguir encontrado por XPath!")
                except TimeoutException:
                    print("❌ Timeout: Botão de seguir não encontrado.")

                    # Adicionar o perfil à lista de seguidos para evitar repetir
                    seguidores_escolhidos.append(seguidor)
                    with open(seguidores_lista, "a") as file:
                        file.write(seguidor + "\n")
                    continue  # Pula para o próximo perfil

                # Clicar no botão de seguir
                seguir_button.click()
                print(f"✅ Seguiu: {seguidor}")

                # Adicionar o perfil à lista de seguidos
                seguidores_escolhidos.append(seguidor)

                # Atualizar o contador
                contador += 1

                # Atualizar o arquivo de seguidos
                with open(seguidores_lista, "a") as file:
                    file.write(seguidor + "\n")

                # Esperar um tempo aleatório entre ações para evitar bloqueios
                tempo_entre = random.randint(10, 48)
                print(
                    f"⌛ Esperando {tempo_entre} segundos antes de seguir o próximo perfil..."
                )
                time.sleep(tempo_entre)

        except WebDriverException as e:
            print(f"❌ Erro ao seguir: {seguidor}, erro: {e}")

    except Exception as e:
        print(f"❌ Erro ao acessar o perfil: {seguidor}, erro: {e}")


# Função para salvar os seguidores no arquivo
def salvar_seguidores(seguidores):
    arquivo_seguidores = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "seguidores.txt"
    )
    with open(arquivo_seguidores, "a") as file:
        for seguidor in seguidores:
            file.write(seguidor + "\n")


# Função para gerar o relatório
def gerar_relatorio(
    tempo_execucao,
    total_seguidores_coletados,
    total_seguidores_escolhidos,
    seguidores_com_sucesso,
    erros,
):
    arquivo_relatorio = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "relatorio.txt"
    )
    with open(arquivo_relatorio, "w") as file:
        file.write("Relatório de Automação - 2025-02-19\n\n")
        file.write(f"Tempo de execução: {tempo_execucao:.2f} segundos\n")
        file.write(f"Total de seguidores coletados: {total_seguidores_coletados}\n")
        file.write(f"Total de seguidores escolhidos: {total_seguidores_escolhidos}\n")
        file.write(f"Perfis seguidos com sucesso: {seguidores_com_sucesso}\n")
        file.write(f"Erros: {erros}\n")


# Tempo de execução
tempo_execucao = time.time() - iniciar_tempo

# Salvar os seguidores acessados
salvar_seguidores(seguidores_escolhidos)

# Gerar o relatório
gerar_relatorio(
    tempo_execucao, len(seguidores_lista), quantidade_para_seguir, contador, 0
)
print("✅ Relatório gerado com sucesso.")
