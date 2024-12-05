# Robot Link Embratel 

 ![Demonstração](https://media.giphy.com/media/Ldntg0zWQbWvvWk0m6/giphy.gif)

Este projeto monitora um link específico utilizando Zabbix (PyZabbix) e automatiza ações usando Selenium WebDriver e criação de uma interface gráfica com CustomTkinter para o acompanhamento de status da automação.

Essa automação é geralmente usada para abertura de chamado caso um link específico fique fora do ar, no meu caso, embratel.

 

## Índice

 

- [Requisitos](#requisitos)

- [Configuração](#configuração)

- [Uso](#uso)

- [Datalhes das funções](#funções-do-código)

- [Personalização](#personalização)

- [Autor](#autor)

- [Licença](#licença)

 

## Requisitos

 

Certifique-se de ter os seguintes pacotes instalados:

 

- `customtkinter`

- `pyzabbix`

- `selenium`

- `Pillow`

 

Você pode instalar os pacotes necessários usando pip:

 

```Code:

pip install customtkinter pyzabbix selenium Pillow

```

Além disso, você precisará de um navegador WebDriver instalado:

 

Firefox: Baixe o geckodriver e adicione-o ao seu PATH.

 

Chrome: Baixe o chromedriver e adicione-o ao seu PATH.

 

## Configuração

 

Configuração do Zabbix:

 

Certifique-se de ter as credenciais do seu servidor Zabbix (usuário e senha).

 

Modifique a URL do servidor Zabbix no código para apontar para o seu servidor:

 

```Code:

zapi = ZabbixAPI("http://URL SERVIDOR")

zapi.login("seu usuário", "sua senha")

```

 

Logotipo:

 

Coloque a imagem Embratel_logo.png ou uma imagem de sua prefência na pasta imagens dentro do diretório do projeto.

 

## Uso

 

Execute o script principal para iniciar a interface gráfica e começar a monitorar o link:

 

A interface exibirá uma mensagem e iniciará a automação caso a trigger do Zabbix detecte um problema com o link da Embratel.

 

```Code:

python automationzabbix.py

```

## Funções do código

 

- `start_automation():` Inicia a automação com o Selenium WebDriver.

 

- `monitor_trigger(label):` Monitora a trigger do Zabbix e inicia a automação se necessário.

 

- `create_interface():` Cria a interface gráfica usando CustomTkinter.

 

## Detalhes das Funções

 

`start_automation()`:

Esta função inicializa um WebDriver (Firefox) (Você pode escolher o navegador de sua preferência)

e navega para um link específico onde a automação ocorrerá. A automação que você deseja deve ser adicionada dentro dessa função.

 

`monitor_trigger(label)`:


A função cria uma conexão com o servidor Zabbix e monitora triggers específicas.

Se uma trigger de alta prioridade for detectada para um host específico, a automação é iniciada.

 

`create_interface()`:

Esta função cria a interface gráfica usando CustomTkinter.

Inclui um label para exibir o status e um progress bar para simular uma animação de monitoramento. Também carrega e exibe o logotipo da Embratel.

 

## Personalização

 

Você pode personalizar as seguintes partes do código para se adequar às suas necessidades:

 

`Navegador WebDriver`: Alterar webdriver.Firefox() para webdriver.Chrome() se preferir usar o Chrome.

 

`Configurações do Zabbix`: Atualizar as credenciais e URL do servidor Zabbix conforme necessário.

 

`Verificação de Hosts`: Modificar o nome do host e os critérios de prioridade na função monitor_trigger.

 

`Interface Gráfica`: Customizar a aparência e os elementos da interface gráfica conforme desejado.

 

## Autor

Thallis Araujo

 

- GitHub: thallislyonn

 

# Licença

 

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
