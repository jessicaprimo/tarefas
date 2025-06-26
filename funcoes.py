import os

def carregar_usuarios(arquivo='usuarios.txt'):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, 'r', encoding='utf-8') as f:
        usuarios = [linha.strip() for linha in f.readlines() if linha.strip()]
    return usuarios

def salvar_tarefa(usuario, descricao, prioridade, arquivo='tarefas.txt'):
    with open(arquivo, 'a', encoding='utf-8') as f:
        f.write(f"{usuario}|{descricao}|{prioridade}\n")

def carregar_tarefas_por_usuario(usuario, arquivo='tarefas.txt'):
    tarefas = {"Alta": [], "Média": [], "Baixa": []}
    if not os.path.exists(arquivo):
        return tarefas
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split('|')
            if len(partes) >= 3:
                usuario_linha, descricao, prioridade = partes[:3]
                if usuario_linha == usuario:
                    if prioridade in tarefas:
                        tarefas[prioridade].append(descricao)
    return tarefas
