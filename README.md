# Sistema de Análise da Loteria

Um sistema em Python para análise de números da loteria, geração de apostas aleatórias e identificação de números "mágicos" - aqueles que não aparecem em nenhuma das apostas analisadas.

## Funcionalidades

- Geração de apostas aleatórias com números de 1 a 60
- Carregamento de apostas a partir de arquivos CSV
- Identificação de números "mágicos" (números não utilizados em nenhuma aposta)
- Interface de menu interativa para fácil utilização
- Sistema de logs e salvamento de resultados com timestamp

## Requisitos

- Python 3.6 ou superior
- Não requer bibliotecas externas (utiliza apenas módulos da biblioteca padrão)

## Estrutura do Projeto

```
lottery-analysis/
│
├── numeros_magicos_loteria.py    # Arquivo principal do programa
├── apostas.csv         # Arquivo de exemplo para apostas
└── README.md          # Este arquivo que você está lendo :o)
```

## Como Usar

1. Execute o programa:
```bash
python numeros_magicos_loteria.py
```

2. Use o menu interativo para:
   - Gerar novas apostas aleatórias
   - Carregar apostas existentes
   - Encontrar números mágicos
   - Salvar resultados

### Formato do Arquivo CSV

O arquivo CSV deve conter uma aposta por linha, com 6 números por aposta, separados por vírgula.
Exemplo:
```
6,11,14,20,31,45
8,15,35,24,50,44
1,17,18,23,11,10
```

### Arquivos de Saída

- **apostas_geradas.csv**: Contém as apostas geradas aleatoriamente
- **numeros_magicos_[TIMESTAMP].txt**: Contém os números mágicos encontrados e estatísticas

## Funcionalidades Detalhadas

### 1. Geração de Apostas
- Gera apostas aleatórias com 6 números únicos
- Números entre 1 e 60
- Salva automaticamente em arquivo CSV

### 2. Carregamento de Apostas
- Lê arquivos CSV existentes
- Validação de formato e tratamento de erros
- Feedback sobre quantidade de apostas carregadas

### 3. Análise de Números Mágicos
- Identifica números que não aparecem em nenhuma aposta
- Gera relatório detalhado com timestamp
- Salva resultados em arquivo texto

## Tratamento de Erros

O sistema inclui tratamento para:
- Arquivos não encontrados
- Formatos inválidos de CSV
- Entradas inválidas do usuário
- Erros de permissão de arquivo

## Contribuindo

Para contribuir com o projeto:
1. Fork o repositório
2. Crie uma branch para sua feature
3. Faça commit das mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Está sob licença GNU.
