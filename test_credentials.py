#!/usr/bin/env python3
"""
Script de teste para verificar a lógica de detecção de credenciais do Google Cloud
"""

import os
import json
from pathlib import Path

def test_credentials_detection():
    """Testa a lógica de detecção de credenciais"""
    
    print("=== Teste de Detecção de Credenciais do Google Cloud ===\n")
    
    # Simular diferentes cenários de credenciais
    test_cases = [
        {
            "name": "JSON válido (como no Streamlit Cloud)",
            "env_var": '{"type": "service_account", "project_id": "test-project", "private_key_id": "123"}',
            "expected": True
        },
        {
            "name": "JSON inválido",
            "env_var": '{"invalid": "json"',
            "expected": False
        },
        {
            "name": "JSON sem chaves necessárias",
            "env_var": '{"some": "other", "keys": "here"}',
            "expected": False
        },
        {
            "name": "Caminho de arquivo (ambiente local)",
            "env_var": str(Path(__file__).parent / "decent-atlas-460512-g7-3b1d4ccb9c4e.json"),
            "expected": None  # Depende se o arquivo existe
        },
        {
            "name": "Variável vazia",
            "env_var": "",
            "expected": False
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"Teste {i}: {test_case['name']}")
        print(f"Valor: {test_case['env_var'][:50]}{'...' if len(test_case['env_var']) > 50 else ''}")
        
        # Aplicar a lógica de detecção
        credenciais_env = test_case['env_var']
        credenciais_configuradas = False
        
        if credenciais_env:
            # Verificar se é um JSON direto (Streamlit Cloud)
            if credenciais_env.strip().startswith('{') and credenciais_env.strip().endswith('}'):
                try:
                    # Validar se é um JSON válido com as chaves necessárias
                    creds_data = json.loads(credenciais_env)
                    if 'type' in creds_data and 'project_id' in creds_data:
                        credenciais_configuradas = True
                        print("✓ Credenciais válidas detectadas como JSON")
                    else:
                        print("✗ JSON não contém as chaves necessárias")
                except json.JSONDecodeError:
                    print("✗ JSON inválido")
            # Verificar se é um caminho de arquivo válido (ambiente local)
            elif os.path.exists(credenciais_env):
                credenciais_configuradas = True
                print("✓ Arquivo de credenciais encontrado")
            else:
                print("✗ Caminho de arquivo não existe")
        else:
            print("✗ Variável de ambiente vazia")
        
        if test_case['expected'] is not None:
            result = "✓ PASSOU" if credenciais_configuradas == test_case['expected'] else "✗ FALHOU"
            print(f"Resultado: {credenciais_configuradas} (esperado: {test_case['expected']}) - {result}")
        else:
            print(f"Resultado: {credenciais_configuradas} (arquivo existe: {os.path.exists(credenciais_env)})")
        
        print("-" * 50)

if __name__ == "__main__":
    test_credentials_detection()
