import os
import json
import tempfile
from pathlib import Path

def setup_google_credentials():
    """
    Configura as credenciais do Google Cloud para ambientes de produção.
    Suporta tanto arquivo JSON local quanto string JSON em variável de ambiente.
    """
    # Primeiro, tenta obter credenciais da variável de ambiente
    google_creds = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
    if google_creds:
        # Se é um caminho de arquivo existente, usa diretamente
        if os.path.isfile(google_creds):
            return google_creds
        
        # Se parece ser um JSON string (para deploy em nuvem)
        try:
            # Tenta parsear como JSON
            creds_dict = json.loads(google_creds)
            
            # Cria um arquivo temporário com as credenciais
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(creds_dict, f)
                temp_creds_path = f.name
            
            # Define a variável de ambiente para o arquivo temporário
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = temp_creds_path
            return temp_creds_path
            
        except json.JSONDecodeError:
            # Se não é JSON válido, assume que é um caminho de arquivo
            pass
    
    # Fallback para arquivo local (desenvolvimento)
    local_creds_path = str(Path(__file__).parent / "decent-atlas-460512-g7-3b1d4ccb9c4e.json")
    if os.path.isfile(local_creds_path):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = local_creds_path
        return local_creds_path
    
    return None

def get_google_api_key():
    """
    Obtém a chave da API do Google a partir das variáveis de ambiente.
    """
    return os.getenv('GOOGLE_API_KEY')
