import streamlit as st
import funcoes

st.set_page_config(page_title="Sistema de Tarefas", page_icon="📝", layout="wide")

st.markdown("<h1 style='color:#4B8BBE;'>📋 Sistema de Cadastro de Tarefas</h1>", unsafe_allow_html=True)

menu = st.sidebar.radio("📌 Menu", ["Cadastrar tarefa", "Visualizar tarefas"])

usuarios = funcoes.carregar_usuarios()

if menu == "Cadastrar tarefa":
    st.subheader("➕ Cadastrar nova tarefa")
    
    if not usuarios:
        st.warning("⚠️ Nenhum usuário cadastrado. Adicione usuários no arquivo usuarios.txt.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            usuario = st.selectbox("👤 Selecione o usuário", usuarios)
        with col2:
            prioridade = st.radio("📌 Prioridade", ["Alta", "Média", "Baixa"], horizontal=True)
        
        descricao = st.text_area("📝 Descrição da tarefa")

        if st.button("💾 Salvar tarefa"):
            if descricao.strip() == "":
                st.error("Por favor, preencha a descrição da tarefa.")
            else:
                funcoes.salvar_tarefa(usuario, descricao, prioridade)
                st.success("✅ Tarefa salva com sucesso!")
                st.balloons()

elif menu == "Visualizar tarefas":
    st.subheader("📑 Visualizar tarefas")

    if not usuarios:
        st.warning("⚠️ Nenhum usuário cadastrado.")
    else:
        usuario = st.selectbox("👤 Selecione o usuário", usuarios)
        tarefas = funcoes.carregar_tarefas_por_usuario(usuario)

        cores = {"Alta": "#ff4b4b", "Média": "#ffa500", "Baixa": "#4caf50"}

        for prioridade in ["Alta", "Média", "Baixa"]:
            with st.expander(f"📌 Tarefas com prioridade {prioridade}"):
                if tarefas[prioridade]:
                    for tarefa in tarefas[prioridade]:
                        st.markdown(
                            f"<div style='background-color:{cores[prioridade]}; padding:8px; margin-bottom:4px; border-radius:5px; color:white'>{tarefa}</div>",
                            unsafe_allow_html=True
                        )
                else:
                    st.info("Nenhuma tarefa.")
