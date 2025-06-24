#!/bin/bash

# Script de setup para produção
echo "Configurando ambiente de produção..."

# Criar diretórios necessários
mkdir -p data logs dossies

# Configurar permissões se necessário
chmod 755 data logs dossies

# Verificar variáveis de ambiente obrigatórias
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "⚠️  AVISO: GOOGLE_APPLICATION_CREDENTIALS não configurada"
fi

if [ -z "$GOOGLE_API_KEY" ]; then
    echo "⚠️  AVISO: GOOGLE_API_KEY não configurada"
fi

echo "✅ Setup concluído!"
