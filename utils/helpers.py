import logging
import os
from pathlib import Path

def setup_logging(app_name):
    """Configura o sistema de logging para o aplicativo especificado"""
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / f"{app_name}.log"
    
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(app_name)

def get_asset_path(filename):
    """Retorna o caminho completo para um arquivo de asset"""
    assets_dir = Path(__file__).parent.parent / "assets"
    return assets_dir / filename

def load_environment_variables():
    """Carrega variáveis de ambiente do arquivo .env"""
    try:
        from dotenv import load_dotenv
        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(env_path)
        return True
    except Exception as e:
        print(f"Erro ao carregar variáveis de ambiente: {e}")
        return False