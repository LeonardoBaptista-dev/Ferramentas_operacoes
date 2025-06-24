# Ferramentas I.A SV

Dashboard com ferramentas de IA para otimização de operações de vendas.

## Funcionalidades

- **Gerador de Dossiê**: Crie dossiês comerciais detalhados a partir de sites de empresas
- **Corretor Ortográfico**: Corrija textos e melhore a qualidade da comunicação escrita
- **Gerador de Método de Vendas**: Crie estratégias de vendas personalizadas
- **Consultor IA**: Obtenha consultoria especializada em vendas

## Deploy Gratuito

### Opção 1: Streamlit Cloud (Recomendado)

1. **Faça upload do código para o GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/seu-usuario/seu-repositorio.git
   git push -u origin main
   ```

2. **Acesse [share.streamlit.io](https://share.streamlit.io)**

3. **Conecte sua conta GitHub e selecione o repositório**

4. **Configure as variáveis de ambiente**:
   - `GOOGLE_APPLICATION_CREDENTIALS`: Conteúdo do arquivo JSON de credenciais do Google Cloud (cole o conteúdo completo)
   - `GOOGLE_API_KEY`: Sua chave da API do Google
   - `EMAIL_REMETENTE`: Seu email
   - `EMAIL_SENHA`: Senha de app do Gmail

5. **Deploy automático será feito**

### Opção 2: Render

1. **Acesse [render.com](https://render.com)**
2. **Conecte seu repositório GitHub**
3. **Crie um novo Web Service**
4. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
5. **Adicione as variáveis de ambiente na seção Environment**

### Opção 3: Railway

1. **Acesse [railway.app](https://railway.app)**
2. **Conecte seu repositório GitHub**
3. **Deploy será automático usando o Procfile**
4. **Configure as variáveis de ambiente no dashboard**

## Configuração de Variáveis de Ambiente

Para qualquer plataforma, você precisará configurar:

### Google Cloud Credentials

**Para Streamlit Cloud/Render/Railway**:
- Em vez de usar um arquivo JSON, cole o conteúdo completo do arquivo `decent-atlas-460512-g7-3b1d4ccb9c4e.json` na variável `GOOGLE_APPLICATION_CREDENTIALS`

### Gmail App Password

1. Ative a verificação em duas etapas no Gmail
2. Gere uma senha de app em [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Use essa senha na variável `EMAIL_SENHA`

## Estrutura do Projeto

```
├── app.py                 # Aplicação principal
├── requirements.txt       # Dependências
├── Procfile              # Configuração para Railway/Heroku
├── runtime.txt           # Versão do Python
├── .streamlit/           
│   └── config.toml       # Configuração do Streamlit
├── apps/                 # Módulos das ferramentas
├── assets/               # Imagens e recursos
├── data/                 # Dados persistidos
└── materiais/            # Documentos de referência
```

## Desenvolvimento Local

1. **Clone o repositório**
2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure o arquivo .env** (use .env.example como base)
4. **Execute a aplicação**:
   ```bash
   streamlit run app.py
   ```

## Notas de Segurança

- ⚠️ **Nunca commite o arquivo .env ou credenciais reais no GitHub**
- Use variáveis de ambiente da plataforma para dados sensíveis
- Para produção, considere usar Google Cloud Secret Manager
- O arquivo `decent-atlas-460512-g7-3b1d4ccb9c4e.json` deve ser adicionado ao `.gitignore`

## Suporte

Para questões técnicas ou suporte, entre em contato através dos canais oficiais da Sucesso em Vendas.
