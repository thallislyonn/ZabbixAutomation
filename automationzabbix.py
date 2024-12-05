import customtkinter as ctk
from pyzabbix import ZabbixAPI
from selenium import webdriver
import threading
import time
import os
from PIL import Image

# Função para iniciar a automação com o WebDriver
def start_automation():
    # Opção de iniciar com o Chrome ou Firefox
    driver = webdriver.Firefox()
    driver.get("link para abrir o chamado")
    # Adicione o restante da sua automação aqui
    driver.quit()

# Função para monitorar a trigger do Zabbix
def monitor_trigger(label):
    # Conexão com o servidor do Zabbix
    zapi = ZabbixAPI("Link do Servidor Zabbix")
    zapi.login("seu usuário", "sua senha")

    # Verificação do host específico que você deseja
    while True:
        triggers = zapi.trigger.get(
            filter={"value": 1},
            output=["triggerid", "description", "priority"],
            selectHosts=["hostid", "host", "name"]
        )
        for trigger in triggers:
            if 'hosts' in trigger and trigger['hosts']:
                for host in trigger['hosts']:
                    if host['host'] == "Nome do Host" and trigger['priority'] == '5':
                        label.set_text("Link Caiu! Iniciando automação...")
                        start_automation()
                        return
        time.sleep(5)  # Esperar 5 segundos antes de verificar novamente

# Função para criar a interface gráfica
def create_interface():
    root = ctk.CTk()
    root.geometry("500x180")
    root.title("Robot Link Embratel")
    root.resizable(False, False)

    # Crie um label para exibir o texto
    label = ctk.CTkLabel(root, text="Monitorando o Link da Embratel", font=("Security Company", 30), text_color="#336FA1")
    label.pack(pady=20)

    # Crie uma animação de loop
    progress = ctk.CTkProgressBar(root, progress_color="white")
    progress.pack(pady=20)
    progress.start()

    # Define o caminho da imagem do logotipo da Embratel
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório atual do script
    image_path = os.path.join(current_dir, "imagens", "Embratel_logo.png")

    # Carregue a imagem usando PIL
    pil_image = Image.open(image_path)

    # Carrega e exibe a imagem na interface (se disponível)
    image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(100, 100))
    image_label = ctk.CTkLabel(root, image=image, text="")
    image_label.pack(pady=(0))

    # Inicie a thread de monitoramento
    thread = threading.Thread(target=monitor_trigger, args=(label,))
    thread.daemon = True  # Permite que a thread seja fechada quando a janela for fechada
    thread.start()

    root.mainloop()

# Inicie a interface gráfica
if __name__ == "__main__":
    create_interface()