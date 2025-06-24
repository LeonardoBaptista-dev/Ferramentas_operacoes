import streamlit as st
import os
from pathlib import Path
import importlib
import sys

# Adiciona o diretório raiz ao path para importar módulos corretamente
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Função para navegar entre apps
def navigate_to(app_name):
    st.session_state.current_app = app_name
    st.query_params["app"] = app_name
    st.rerun()

# Inicializar o estado da sessão
if 'current_app' not in st.session_state:
    st.session_state.current_app = 'home'

# Verificar parâmetros de URL para navegação
if "app" in st.query_params:
    app_name = st.query_params["app"]
    if app_name != st.session_state.current_app:
        st.session_state.current_app = app_name

# Configuração da página - definimos o estado da barra lateral com base no app atual
sidebar_state = "collapsed" if st.session_state.current_app == 'home' else "expanded"

# Configuração da página
st.set_page_config(
    page_title="Agentes I.A SV - Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state=sidebar_state
)

# Diretório de assets
assets_dir = Path(__file__).parent / "assets"

# CSS personalizado
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3em;
        margin-bottom: 30px;
        color: #1E3A8A;
    }
    
    .tool-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .tool-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .tool-title {
        font-size: 1.5em;
        font-weight: bold;
        margin-bottom: 10px;
        color: #1E3A8A;
    }
    
    .tool-description {
        color: #4B5563;
        margin-bottom: 15px;
    }
    
    .tool-button {
        background-color: #1E3A8A;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
        font-weight: bold;
        display: block;
        margin: 0 auto;
        border: none;
        width: 80%;
    }
    
    .tool-button:hover {
        background-color: #2563EB;
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #6B7280;
        font-size: 0.8em;
    }
</style>
""", unsafe_allow_html=True)

# Renderizar o app apropriado
if st.session_state.current_app == 'home':
    # Cabeçalho com logo centralizada - abordagem simples
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        try:
            logo_path = assets_dir / "LOGO SUCESSO EM VENDAS HORIZONTAL AZUL.png"
            st.image(str(logo_path), width=500)  # Tamanho reduzido para 200px
        except FileNotFoundError:
            st.write("Logo não encontrada. Por favor, verifique o caminho da imagem.")

    st.markdown("<h1 class='main-title'>Ferramentas I.A SV</h1>", unsafe_allow_html=True)
    
    # Ferramentas disponíveis
    tools = [
        {
            "id": "dossie",
            "title": "Gerador de Dossiê",
            "description": "Crie dossiês comerciais detalhados a partir de sites de empresas.",
        },
        {
            "id": "corretor",
            "title": "Corretor Ortográfico",
            "description": "Corrija textos e melhore a qualidade da sua comunicação escrita.",
        },
        {
            "id": "metodo_vendas",
            "title": "Gerador de Método de Vendas",
            "description": "Crie estratégias de vendas personalizadas para diferentes cenários.",
        },
        {
            "id": "consultor_ia",
            "title": "Consultor IA",
            "description": "Obtenha consultoria especializada em vendas com nossa IA.",
            
        }
    ]
    
    # Exibir as ferramentas em grid
    col1, col2 = st.columns(2)
    
    for i, tool in enumerate(tools):
        with col1 if i % 2 == 0 else col2:
            # Criar card para cada ferramenta
            with st.container():
                st.markdown(f"""
                <div class="tool-container" style="text-align: center;">
                    <div class="tool-title">{tool['title']}</div>
                    <div class="tool-description">{tool['description']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Usar botão nativo do Streamlit para navegação
                if st.button(f"Acessar {tool['title']}", key=f"btn_{tool['id']}", 
                             use_container_width=True):
                    navigate_to(tool['id'])
    
    # Rodapé
    st.markdown("<div class='footer'>© 2025 Sucesso em Vendas. Todos os direitos reservados.</div>", unsafe_allow_html=True)

else:
    # Carrega o app selecionado
    try:
        # Passa a configuração da página para o app filho
        app_config = {
            "already_configured": True,  # Indica que a página já foi configurada
            "title": st.title,  # Passa a função de título para o app filho
            "header": lambda: None,  # Função vazia para o cabeçalho
            "sidebar": st.sidebar  # Passa a barra lateral
        }
        
        app_module = importlib.import_module(f"apps.{st.session_state.current_app}")
        
        # Verificar se a função app aceita parâmetros
        import inspect
        try:
            sig = inspect.signature(app_module.app)
            if len(sig.parameters) > 0:
                app_module.app(app_config)
            else:
                app_module.app()  # Chamar sem parâmetros se a função não os aceitar
        except (ValueError, TypeError):
            # Fallback se não conseguir obter a assinatura ou se houver erro de tipo
            try:
                app_module.app(app_config)
            except TypeError:
                app_module.app()
        
    except ImportError as e:
        st.error(f"Erro ao carregar o aplicativo: {e}")
        if st.button("Voltar para a página inicial", key="btn_home_error_import"):
            navigate_to('home')
    except Exception as e:
        st.error(f"Erro ao executar o aplicativo: {e}")
        if st.button("Voltar para a página inicial", key="btn_home_error_general"):
            navigate_to('home')