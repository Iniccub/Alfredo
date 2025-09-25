"""
Script para fazer backup dos eventos do MongoDB para um arquivo local.
Este script lê todos os eventos da coleção 'eventos' no banco de dados 'alfredo_db'
e os salva em um arquivo JSON local com data e hora no nome do arquivo.
"""

import json
import os
from datetime import datetime
from pymongo import MongoClient
import sys

def conectar_mongodb():
    """Conecta ao MongoDB usando as credenciais do arquivo mongodb.py"""
    try:
        # Importa as credenciais do arquivo mongodb.py
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from mongodb import user, secure_password, string
        
        # Cria a string de conexão
        connection_string = string.replace('<db_password>', secure_password)
        
        # Conecta ao MongoDB
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        
        # Testa a conexão
        client.admin.command('ping')
        print("Conectado ao MongoDB Atlas com sucesso!")
        
        # Retorna o banco de dados
        return client['alfredo_db']
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

def fazer_backup():
    """Faz o backup dos eventos do MongoDB para um arquivo JSON local"""
    # Conecta ao MongoDB
    db = conectar_mongodb()
    
    if db is None:  # Corrigido: usar 'is None' em vez de 'not db'
        print("Não foi possível conectar ao MongoDB. Backup cancelado.")
        return False
    
    try:
        # Obtém a coleção de eventos
        collection = db['eventos']
        
        # Busca todos os eventos, excluindo o campo _id
        eventos = list(collection.find({}, {'_id': 0}))
        
        # Cria o diretório de backup se não existir
        backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        
        # Cria o nome do arquivo com data e hora
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"backup_eventos_{timestamp}.json")
        
        # Salva os eventos no arquivo JSON
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(eventos, f, ensure_ascii=False, indent=4)
        
        print(f"Backup concluído com sucesso! {len(eventos)} eventos salvos em {backup_file}")
        return True
    
    except Exception as e:
        print(f"Erro ao fazer backup: {e}")
        return False

def restaurar_backup(arquivo_backup):
    """Restaura os eventos de um arquivo de backup para o MongoDB"""
    # Verifica se o arquivo existe
    if not os.path.exists(arquivo_backup):
        print(f"Arquivo de backup não encontrado: {arquivo_backup}")
        return False
    
    # Conecta ao MongoDB
    db = conectar_mongodb()
    
    if db is None:  # Corrigido: usar 'is None' em vez de 'not db'
        print("Não foi possível conectar ao MongoDB. Restauração cancelada.")
        return False
    
    try:
        # Lê os eventos do arquivo de backup
        with open(arquivo_backup, 'r', encoding='utf-8') as f:
            eventos = json.load(f)
        
        # Obtém a coleção de eventos
        collection = db['eventos']
        
        # Confirma com o usuário
        confirmacao = input(f"Isso substituirá todos os {collection.count_documents({})} eventos existentes. Continuar? (s/n): ")
        
        if confirmacao.lower() != 's':
            print("Restauração cancelada pelo usuário.")
            return False
        
        # Remove todos os eventos existentes
        collection.delete_many({})
        
        # Insere os eventos do backup
        if eventos:
            collection.insert_many(eventos)
        
        print(f"Restauração concluída com sucesso! {len(eventos)} eventos restaurados.")
        return True
    
    except Exception as e:
        print(f"Erro ao restaurar backup: {e}")
        return False

def listar_backups():
    """Lista todos os arquivos de backup disponíveis"""
    backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backups')
    
    if not os.path.exists(backup_dir):
        print("Nenhum backup encontrado.")
        return []
    
    backups = [f for f in os.listdir(backup_dir) if f.startswith('backup_eventos_') and f.endswith('.json')]
    
    if not backups:
        print("Nenhum backup encontrado.")
        return []
    
    print("Backups disponíveis:")
    for i, backup in enumerate(backups, 1):
        # Extrai a data e hora do nome do arquivo
        timestamp = backup.replace('backup_eventos_', '').replace('.json', '')
        data_hora = datetime.strptime(timestamp, "%Y%m%d_%H%M%S").strftime("%d/%m/%Y %H:%M:%S")
        
        # Obtém o tamanho do arquivo
        tamanho = os.path.getsize(os.path.join(backup_dir, backup)) / 1024  # KB
        
        print(f"{i}. {data_hora} - {tamanho:.2f} KB")
    
    return [os.path.join(backup_dir, b) for b in backups]

if __name__ == "__main__":
    print("=== Sistema de Backup do Alfredo ===")
    print("1. Fazer backup")
    print("2. Restaurar backup")
    print("3. Listar backups")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        fazer_backup()
    elif opcao == "2":
        backups = listar_backups()
        if backups:
            try:
                indice = int(input("Digite o número do backup a ser restaurado: ")) - 1
                if 0 <= indice < len(backups):
                    restaurar_backup(backups[indice])
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    elif opcao == "3":
        listar_backups()
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opção inválida.")