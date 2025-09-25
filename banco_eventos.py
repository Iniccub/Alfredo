# Arquivo de banco de dados para exportação para MongoDB
# Este arquivo contém a estrutura de dados que será exportada para a coleção "eventos"
# no banco de dados "alfredo_db" do MongoDB Atlas

from datetime import datetime, timedelta

# Função para criar eventos de exemplo
def criar_eventos_exemplo():
    # Data atual para referência
    hoje = datetime.now().date()
    
    # Criar alguns eventos de exemplo para diferentes departamentos
    eventos = [
        {
            "title": "Reunião de Planejamento - TI",
            "start": datetime.combine(hoje + timedelta(days=1), datetime.min.time().replace(hour=10, minute=0)).isoformat(),
            "end": datetime.combine(hoje + timedelta(days=1), datetime.min.time().replace(hour=11, minute=30)).isoformat(),
            "description": "Departamento: TI\nParticipantes: João Silva, Maria Oliveira\n\nPlanejamento de projetos para o próximo trimestre."
        },
        {
            "title": "Revisão de Orçamento - Financeiro",
            "start": datetime.combine(hoje + timedelta(days=2), datetime.min.time().replace(hour=14, minute=0)).isoformat(),
            "end": datetime.combine(hoje + timedelta(days=2), datetime.min.time().replace(hour=15, minute=0)).isoformat(),
            "description": "Departamento: Financeiro\nParticipantes: Carlos Santos, Ana Pereira\n\nRevisão do orçamento mensal e planejamento financeiro."
        },
        {
            "title": "Estratégia de Marketing",
            "start": datetime.combine(hoje + timedelta(days=3), datetime.min.time().replace(hour=9, minute=0)).isoformat(),
            "end": datetime.combine(hoje + timedelta(days=3), datetime.min.time().replace(hour=10, minute=30)).isoformat(),
            "description": "Departamento: Marketing\nParticipantes: Fernanda Lima, Ricardo Gomes\n\nDefinição de estratégias para campanhas do próximo mês."
        },
        {
            "title": "Recrutamento e Seleção",
            "start": datetime.combine(hoje + timedelta(days=4), datetime.min.time().replace(hour=11, minute=0)).isoformat(),
            "end": datetime.combine(hoje + timedelta(days=4), datetime.min.time().replace(hour=12, minute=0)).isoformat(),
            "description": "Departamento: RH\nParticipantes: Juliana Costa, Pedro Almeida\n\nProcesso de recrutamento para novas vagas."
        },
        {
            "title": "Análise de Vendas",
            "start": datetime.combine(hoje + timedelta(days=5), datetime.min.time().replace(hour=15, minute=30)).isoformat(),
            "end": datetime.combine(hoje + timedelta(days=5), datetime.min.time().replace(hour=16, minute=30)).isoformat(),
            "description": "Departamento: Comercial\nParticipantes: Roberto Dias, Camila Ferreira\n\nAnálise dos resultados de vendas do último trimestre."
        }
    ]
    
    return eventos

# Lista de eventos de orçamento 2025
eventos_orcamento_2025 = [
    {'title': '[ORÇAMENTO 2025] CSA DV', 'start': '2025-05-12T14:00:00', 'end': '2025-05-12T15:00:00', 'description': 'Departamento: CSA - DV\nParticipantes: Karla Camargos Souza, Taianny Souza Pinto\n\nReunião de acompanhamento do reeal x orçado da unidade.'},
    {'title': '[ORÇAMENTO 2025] Contabilidade', 'start': '2025-05-13T09:00:00', 'end': '2025-05-13T09:30:00', 'description': 'Departamento: Contabilidade\nParticipantes: Juliana Silva Casagrande\n\nReunião de acompanhamento do reeal x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] CSA BH', 'start': '2025-05-13T09:00:00', 'end': '2025-05-13T10:00:00', 'description': 'Departamento: CSA - BH\nParticipantes: Mauro Pereces Macedo, Douglas Leite\n\nReunião de acompanhamento do reeal x orçado da unidade.'},
    {'title': '[ORÇAMENTO 2025] Gestão de Documentos', 'start': '2025-05-12T16:00:00', 'end': '2025-05-12T16:30:00', 'description': 'Departamento: Gestão de Documentos\nParticipantes: Miryam Laila Ferreira\n\nReunião de acompanhamento do reeal x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] CSA NL', 'start': '2025-05-14T09:00:00', 'end': '2025-05-14T10:00:00', 'description': 'Departamento: CSA - NL\nParticipantes: Fabricio de Paula Martins\n\nReunião de acompanhamento do reeal x orçado da unidade.'},
    {'title': '[ORÇAMENTO 2025] CSA GZ', 'start': '2025-05-14T14:30:00', 'end': '2025-05-14T15:30:00', 'description': 'Departamento: CSA - GZ\nParticipantes: Jaqueline Andrade Fonseca\n\nReunião de acompanhamento do reeal x orçado da unidade.'},
    {'title': '[ORÇAMENTO 2025] CSA CTG', 'start': '2025-05-15T09:00:00', 'end': '2025-05-15T10:00:00', 'description': 'Departamento: CSA - CTG\nParticipantes: Eduardo dos Santos Lopes, Pablo Ronam João\n\nReunião de acompanhamento do reeal x orçado da unidade.'},
    {'title': '[ORÇAMENTO 2025] Jurídico', 'start': '2025-05-15T10:30:00', 'end': '2025-05-15T11:00:00', 'description': 'Departamento: Assessoria Jurídica\nParticipantes: Leila Oliveira, Rafael Coelho Ferreira\n\nReunião de acompanhamento do reeal x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Financeiro', 'start': '2025-05-16T11:00:00', 'end': '2025-05-16T11:30:00', 'description': 'Departamento: Financeiro\nParticipantes: Julliana Cristina Bertoni, Amanda Macedo Fernandes\n\nReunião de acompanhamento do reeal x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Assistência Social', 'start': '2025-05-19T10:00:00', 'end': '2025-05-19T10:30:00', 'description': 'Departamento: Assistência Social\nParticipantes: Dayse Araújo Dutra\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Departamento Pessoal', 'start': '2025-05-20T09:00:00', 'end': '2025-05-20T10:00:00', 'description': 'Departamento: Departamento de Pessoal\nParticipantes: Karinne Dias, Diego Dias da Cruz\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Recursos Humanos', 'start': '2025-05-20T14:00:00', 'end': '2025-05-20T15:00:00', 'description': 'Departamento: Recursos Humanos\nParticipantes: Matheus Tine\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Comunicação', 'start': '2025-05-20T16:00:00', 'end': '2025-05-20T17:00:00', 'description': 'Departamento: Comunicação e Marketing\nParticipantes: Ana Rita Duarte de Faria, Aline Marian Duarte\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Sustentabilidade', 'start': '2025-05-21T09:00:00', 'end': '2025-05-21T09:30:00', 'description': 'Departamento: Sustentabilidade\nParticipantes: Marcela Poeiras\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Estratégia e Novos Negócios', 'start': '2025-05-21T16:30:00', 'end': '2025-05-21T17:00:00', 'description': 'Departamento: Estratégia e Novos Negócios\nParticipantes: Rodrigo Mourão\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] TI', 'start': '2025-05-22T10:00:00', 'end': '2025-05-22T11:00:00', 'description': 'Departamento: Tecnologia da Informação\nParticipantes: Hudson Oliveira Leite, Ricardo Frederico Gouveia, Luciana Alves Faria\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Internacionalização', 'start': '2025-05-23T10:00:00', 'end': '2025-05-23T10:30:00', 'description': 'Departamento: Internacionalização\nParticipantes: Clarissa Felix Azevedo\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Coord. Manutenção', 'start': '2025-05-27T09:00:00', 'end': '2025-05-27T09:30:00', 'description': 'Departamento: Coordenação de Manutenção\nParticipantes: Ricardo Augusto Loureiro\n\nReunião mensal de acompanhamento do orçamento.'},
    {'title': '[ORÇAMENTO 2025] Secretaria', 'start': '2025-05-23T15:00:00', 'end': '2025-05-23T15:30:00', 'description': 'Departamento: Secretaria\nParticipantes: Nubia Paula Las Casas\n\nReunião mensal de acompanhamento do real x orçado da área.'},
    {'title': '[ORÇAMENTO 2025] Pastoralidade', 'start': '2025-05-20T15:00:00', 'end': '2025-05-20T15:30:00', 'description': 'Departamento: Pastoralidade\nParticipantes: Jonathan Felix de Souza\n\nReunião de acompanhamento do real x orçado da área'}
]

# Combinar todos os eventos
eventos_db = criar_eventos_exemplo() + eventos_orcamento_2025

# Função para exportar eventos para MongoDB
def exportar_para_mongodb():
    try:
        from pymongo import MongoClient
        from mongodb import user, secure_password, string
        
        # Conectar ao MongoDB Atlas
        connection_string = string.replace('<db_password>', secure_password)
        client = MongoClient(connection_string)
        
        # Acessar o banco de dados 'alfredo_db'
        db = client['alfredo_db']
        
        # Obter a coleção 'eventos'
        collection = db['eventos']
        
        # Limpar todos os eventos existentes
        collection.delete_many({})
        
        # Inserir os eventos de exemplo
        if eventos_db:
            collection.insert_many(eventos_db)
            print(f"Exportados {len(eventos_db)} eventos para o MongoDB Atlas com sucesso!")
        
        client.close()
        return True
    except Exception as e:
        print(f"Erro ao exportar para MongoDB: {e}")
        return False

# Para exportar os eventos para o MongoDB
exportar_para_mongodb()