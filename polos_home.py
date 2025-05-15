import streamlit as st

st.set_page_config(
    page_title="GENPAC",
    page_icon="images/logo01.png",
    layout="wide"
)

# Dicionário com estrutura de contratos e links
polos = {
    "POLO RS": {
        "Engenharia RS": {
            "BANRISUL USER 1": {
                "url": "https://www.appsheet.com/start/c0fe2be5-d3b4-47cc-9a7d-445bb2f882ce"
            },
            "BANRISUL USER 2": {
                "url": "https://www.appsheet.com/start/0301816b-0516-481f-bccb-19b31720175a"
            },
            "SEC. OBRAS PÚBLICA": {
                "url": "https://www.appsheet.com/start/dadd8a36-177c-437b-9648-5f6ab6428b19"},
            "SMED LESTE": {
                "url": "https://www.appsheet.com/start/eb779b55-6ced-4a8e-b3c6-2caa271fc106"
            },
            "SMED NORTE": {
                "url": "https://www.appsheet.com/start/5be3b962-b0aa-4b42-b533-7573e7eb3da6"},
            
            "BANRISUL CENTRO": {
                "url": "https://www.appsheet.com/start/3222c768-03d7-4100-ad23-437e3706a8d5"
            }
        }
    },
    "POLO RN NT": {
        "Contratos": {
            "Menu": {
                "url": "https://www.appsheet.com/start/c4dbab31-a8e5-4762-ae9d-d36539332035"
            },
        }
    },
    "POLO PR": {
        "CONTRATOS":{
            "FUNDEPAR":{
                "url": "https://www.appsheet.com/start/2660e717-f91b-477f-9da6-fe3a3f9b391d"
            }
        }
    },
    
    "POLO DF": {}, "POLO CG": {}, "POLO GO": {}, "POLO RN MO": {},
    "POLO RN MA": {}, "POLO RN PF": {}, "POLO MG BH": {},
    "POLO RS VERA": {}, "POLO RS PE": {}, "POLO RN AB": {}, "POLO RN NC": {},
     "POLO REC": {}
}

# Sidebar com logo e navegação
st.sidebar.image("images/logo01.png", width=150)  # Substitua pelo caminho correto do seu logo
st.sidebar.title("Navegação")
polo_selecionado = st.sidebar.selectbox("Selecione o Polo", list(polos.keys()))

subpaginas = polos[polo_selecionado]
if subpaginas:
    subpagina_selecionada = st.sidebar.radio("Selecione a Página", list(subpaginas.keys()))
    contratos = subpaginas[subpagina_selecionada]

    st.sidebar.markdown("### Contratos:")
    for nome, info in contratos.items():
        html = f"""
        <div style='display: flex; align-items: center; margin-bottom: 8px;'>
            <span style='font-size: 18px; margin-right: 8px;'>🏗️</span>
            <a href='{info["url"]}' target='_blank' 
               style='text-decoration: none; color: blue; font-size: 15px;'>{nome}</a>
        </div>
        """
        st.sidebar.markdown(html, unsafe_allow_html=True)
else:
    st.sidebar.info("Nenhuma subpágina para este polo.")

import streamlit as st

import streamlit as st

# Pagina Principal
st.title("GENPAC")
st.write("Área destinada para vídeos, textos e orientações.")

st.title("Orientações Banrisul Centro Contrato")
# Linha com 4 vídeos + texto de orientação
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.video("https://youtu.be/49Xo_sQLBig")
    st.write("🔹 Orientação 1: Como acessar o sistema.")

with col2:
    st.video("https://youtu.be/49Xo_sQLBig")
    st.write("🔹 Orientação 2: Cadastro de usuários.")

with col3:
    st.video("https://youtu.be/49Xo_sQLBig")
    st.write("🔹 Orientação 3: Preenchimento de relatórios.")

with col4:
    st.video("https://youtu.be/49Xo_sQLBig")
    st.write("🔹 Orientação 4: Envio de documentos.")

# Rodapé fixo
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0E1117;
            color: #FFFFFF;
            text-align: center;
            padding: 15px 10px;
            font-size: 13px;
            font-family: 'Segoe UI', sans-serif;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.5);
            z-index: 100;
        }

        .footer a {
            color: #00BFFF;
            text-decoration: none;
            margin: 0 10px;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        .footer-icons {
            margin-top: 5px;
        }

        .footer-icons a {
            margin: 0 8px;
            color: #FFFFFF;
        }

        .footer-icons a:hover {
            color: #00BFFF;
        }

        .reportview-container .main .block-container {
            padding-bottom: 80px;
        }
    </style>

    <div class="footer">
        © 2025 <strong>GENPAC</strong> — Todos os direitos reservados<br>
    </div>
""", unsafe_allow_html=True)
