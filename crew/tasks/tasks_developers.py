from crewai import Task
from crew.developers.agent_developers import *

write_doc = Task(
    description=(
        "Analise todos os arquivos e diretórios dentro do caminho '{diretorio}'. "
        "Com base no código-fonte, gere uma documentação técnica completa do projeto. "
        "Descreva a função de cada módulo, classe e função, além da arquitetura geral do sistema. "
        "Inclua detalhes sobre dependências, fluxo de dados e propósito de cada componente. "
        "A documentação deve estar em formato Markdown, com seções bem definidas, por exemplo:\n\n"
        "## Visão Geral\n"
        "## Estrutura de Pastas\n"
        "## Módulos e Responsabilidades\n"
        "## Fluxo de Execução\n"
        "## Como Executar o Projeto\n"
        "## Exemplos de Uso\n"
        "## Observações Técnicas\n\n"
        "Não invente informações — baseie-se apenas no conteúdo encontrado no diretório analisado."
    ),
    agent=editor_doc,
    expected_output=(
        "Um arquivo Markdown (`documentation.md`) com a documentação técnica completa e organizada do projeto, "
        "incluindo descrições de módulos, classes, funções, dependências e exemplos práticos."
    ),
    markdown=True,
    output_file="documentation.md"
)


write_tests = Task(
    description=(
        "Examine o código-fonte do projeto dentro do diretório '{diretorio}'. "
        "Identifique funções, classes e componentes que requerem validação. "
        "Crie testes unitários adequados para cada caso, garantindo cobertura de casos de sucesso, falha e exceção. "
        "Os testes devem seguir o padrão e framework da linguagem principal detectada (ex: pytest, JUnit, Jest, etc). "
        "Apresente os testes em formato Markdown, com estrutura como:\n\n"
        "### Teste: <nome_do_teste>\n"
        "**Descrição:** Explicação breve do que o teste valida.\n"
        "**Código:** Bloco de código com o teste.\n"
        "**Justificativa:** O que esse teste garante no contexto do sistema.\n\n"
        "Os testes devem ser realistas, baseados no código encontrado e não genéricos."
    ),
    agent=tester,
    expected_output=(
        "Um arquivo Markdown (`tests.md`) contendo uma lista organizada de testes unitários, "
        "cada um com nome, descrição, código e justificativa. Os testes devem refletir o comportamento real do código."
    ),
    markdown=True,
    output_file="tests.md"
)

review = Task(
    description=(
        "Navegue pelos diretórios e arquivos do projeto em '{diretorio}'. "
        "Analise o código em busca de possíveis falhas, vulnerabilidades, más práticas, redundâncias e violações de padrão. "
        "Considere aspectos como: legibilidade, complexidade, manutenibilidade, segurança e desempenho. "
        "Produza um relatório técnico em Markdown com seções como:\n\n"
        "## Resumo da Análise\n"
        "## Pontos Fortes do Código\n"
        "## Problemas Identificados\n"
        "## Sugestões de Melhoria\n"
        "## Nível de Risco (Baixo, Médio, Alto)\n\n"
        "Baseie-se apenas nas informações encontradas nos arquivos do diretório e explique o motivo de cada sugestão."
    ),
    agent=editor_review,
    expected_output=(
        "Um arquivo Markdown (`review.md`) apresentando uma análise crítica do código, "
        "indicando falhas, más práticas e recomendações detalhadas de melhoria."
    ),
    markdown=True,
    output_file="review.md"
)
