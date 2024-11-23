#!/bin/bash

# Atualizar o sistema
echo "Atualizando o sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar Python 3 e pip
echo "Instalando Python 3 e pip..."
sudo apt install -y python3 python3-pip

# Instalar dependências adicionais
echo "Instalando dependências do Python..."
pip3 install --upgrade pip
pip3 install telepot

# Informar o sucesso
echo "Instalação concluída com sucesso!"
echo "Agora você pode rodar seu script Python."
