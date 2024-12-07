Este projeto automatiza o envio de mensagens personalizadas para clientes por meio do WhatsApp Web, utilizando um arquivo Excel como base de dados. Ele combina Python com as bibliotecas OpenPyXL, PyAutoGUI, e WebBrowser para realizar o envio de mensagens automaticamente, economizando tempo e esforço.

# Objetivo

Automatizar o envio de notificações para clientes com informações como:

Nome do cliente

Telefone

Data de vencimento de boletos

Link para pagamento

# Funcionamento do Projeto

O script carrega uma planilha Excel (clientes.xlsx) que contém os dados dos clientes.

Para cada cliente, uma mensagem personalizada é criada com base nos dados fornecidos (nome, telefone e vencimento).

A mensagem é enviada via WhatsApp Web utilizando a biblioteca webbrowser para abrir links específicos e o PyAutoGUI para interagir com a interface gráfica.

Em caso de erro no envio da mensagem, o nome e telefone do cliente são registrados em um arquivo CSV chamado erros.csv.

# Tecnologias Utilizadas

Python

OpenPyXL: Para manipular e carregar a planilha Excel.

WebBrowser: Para abrir links do WhatsApp Web.
PyAutoGUI: Para automação de cliques e interação com a interface do WhatsApp Web.
