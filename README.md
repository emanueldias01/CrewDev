# CrewDev

O **CrewDev** é um sistema baseado em **multiagentes de IA**, projetado para **analisar, documentar e testar automaticamente projetos de software**.  

O sistema é composto por três agentes especializados que trabalham em paralelo, lendo o diretório do projeto e produzindo relatórios detalhados:

- **Engenheiro de Documentação** — Gera documentação técnica em Markdown.  
- **Desenvolvedor de Testes** — Escreve testes unitários baseados no código-fonte.  
- **Analista de Qualidade** — Avalia o código e propõe melhorias.  

---

## Funcionalidades

- Geração automática de **documentação técnica completa** do projeto.  
- Criação de **testes unitários** contextualizados, com código e justificativas.  
- Análise estática de **falhas, vulnerabilidades e más práticas** no código.  
- Execução **assíncrona e paralela**, permitindo que todos os agentes trabalhem simultaneamente.(O codigo da branch main é síncrono, mas existe uma branch de nome "async" com a execucao de tarefas assíncrona)  
- Saídas em **Markdown**, salvas automaticamente (`documentation.md`, `tests.md`, `review.md`).  

## Como rodar:
 - Certifique-se de ter o Python 3.10 ou superior instalado em sua máquina.
 - Clone o repositorio
 - instale as dependencias do projeto:
 ```bash
    pip install -r requirements.txt
 ```
 - Crie um arquivo na raiz do diretorio do repositorio chamado 'key.txt' e coloque sua chave de api OPENAI

 - Inicie o programa a partir do diretorio do repositorio
 ```bash
    python main.py

```
- Quando solicitado, informe o caminho do diretório do projeto que você deseja analisar:
```bash
    Diretório: ./SeuProjeto
```

- Aguarde a analise. Durante a análise, você poderá visualizar os logs em tempo real, mostrando o raciocínio e as etapas realizadas por cada agente.

- Dica: para facilitar a análise, mantenha o diretório do seu projeto organizado e próximo ao repositório principal (por exemplo, dentro da mesma pasta).

