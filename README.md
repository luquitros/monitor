[200~cat > ~/monitor/README.md << 'EOF'
# Monitor do Sistema

Monitor de recursos do sistema em tempo real usando Python, Prometheus e Grafana.

## O que monitora

- CPU (%)
- RAM (% e MB usado/total)
- Disco (% e GB livre)

## Stack

- **Python + psutil** — coleta as métricas
- **prometheus_client** — expõe as métricas em `/metrics`
- **Prometheus** — coleta e armazena as métricas
- **Grafana** — exibe os gráficos em tempo real

## Estrutura
```
monitor/
├── main.py                  # loop principal
├── config.py                # configurações
├── collectors/
│   └── psutil_collector.py  # coleta CPU, RAM e disco
├── prometheus.yml           # configuração do Prometheus
├── docker-compose.yml       # sobe Prometheus + Grafana
└── requirements.txt         # dependências Python
```

## Como rodar

### 1. Instala as dependências
```bash
pip install -r requirements.txt
```

### 2. Sobe o Prometheus e Grafana
```bash
docker-compose up -d
```

### 3. Roda o monitor
```bash
python main.py
```

### 4. Acessa o Grafana
Abre `http://localhost:3000` no navegador.
- Usuário: `admin`
- Senha: `admin`

## Métricas disponíveis

| Métrica | Descrição |
|---|---|
| `sistema_cpu_percent` | Uso de CPU em % |
| `sistema_ram_percent` | Uso de RAM em % |
| `sistema_disco_percent` | Uso de disco em % |
| `sistema_disco_livre_gb` | Espaço livre em GB |

## Requisitos

- Python 3.10+
- Docker e docker-compose
- Linux (testado no Arch Linux)
EOF~cat > ~/monitor/.gitignore << 'EOF'
venv/
__pycache__/
*.pyc
.env
vim
