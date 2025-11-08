from crewai import Task
from crew.developers.agent_developers import *

write_doc = Task(
    description=(
        "Realize uma análise **exaustiva e criteriosa** de todos os diretórios e arquivos "
        "localizados no caminho '{diretorio}'. Utilize exclusivamente ferramentas de leitura "
        "de arquivo/diretório e NUNCA assuma, invente ou extrapole informações não presentes "
        "no código. Caso exista qualquer incerteza, declare explicitamente.\n\n"

        "### OBJETIVO\n"
        "Gerar uma documentação técnica absolutamente completa, fiel ao código e "
        "profissional.\n\n"

        "### REGRAS RÍGIDAS\n"
        "- Leia **todos** os arquivos pertinentes do projeto.\n"
        "- Não invente informações e não descreva APIs, comportamentos ou fluxos inexistentes.\n"
        "- Nunca inclua valores 'None' como string ao usar tools; sempre omita ou envie null.\n"
        "- Cruze informações entre arquivos para garantir consistência da arquitetura.\n"
        "- Detecte automaticamente a linguagem e estruturas presentes.\n"
        "- Caso encontre módulos interdependentes, descreva detalhadamente como se relacionam.\n"
        "- Gere somente conteúdo baseado em evidências encontradas.\n\n"

        "### CONTEÚDO OBRIGATÓRIO DO DOCUMENTO (EM MARKDOWN)\n"
        "## Visão Geral\n"
        "Descrição objetiva do propósito do projeto, conforme inferido *somente* pelo código.\n\n"
        "## Estrutura de Pastas\n"
        "Lista detalhada da árvore de diretórios com o papel de cada pasta.\n\n"
        "## Módulos e Responsabilidades\n"
        "Descrição precisa de cada módulo/arquivo, suas funções, classes e interfaces.\n\n"
        "## Fluxo de Execução\n"
        "Mapa completo do fluxo principal e fluxos auxiliares.\n\n"
        "## Como Executar o Projeto\n"
        "Passo a passo real baseado nos arquivos encontrados (scripts, dependências, etc).\n\n"
        "## Exemplos de Uso\n"
        "Trechos extraídos e validados pelo código real.\n\n"
        "## Observações Técnicas Importantes\n"
        "Restrições, dependências críticas, side-effects, limitações e qualquer detalhe crucial.\n\n"

        "Garanta que o documento final reflita **somente a verdade do código** e seja útil, claro, "
        "coeso, tecnicamente sólido e devidamente organizado."
    ),
    agent=editor_doc,
    expected_output=(
        "Um arquivo Markdown (`documentation.md`) contendo documentação completa, precisa, "
        "e totalmente baseada no código-fonte, incluindo descrição de arquitetura, "
        "módulos, funções, fluxos e exemplos válidos."
    ),
    markdown=True,
    async_execution=True,
    output_file="documentation.md"
)


write_tests = Task(
    description=(
        "Examine detalhadamente todo o código do diretório '{diretorio}', identificando:\n"
        "- funções que produzem saídas\n"
        "- classes contendo lógica relevante\n"
        "- serviços, controladores ou módulos que exigem validação\n"
        "- fluxos condicionais, loops, pontos de exceção e comportamentos críticos\n\n"

        "### REGRAS DE PRECISÃO\n"
        "- Baseie TODOS os testes exclusivamente no código analisado.\n"
        "- Não crie testes genéricos ou irreais.\n"
        "- Não invente funcionalidades que não existem.\n"
        "- Identifique cenários de sucesso, erro e exceção obrigatórios.\n"
        "- Para ferramentas como FileReadTool, nunca passe 'None' como string.\n"
        "- Identifique automaticamente o framework de teste adequado à linguagem "
        "detectada (pytest, JUnit, Jest, Go testing, etc).\n"
        "- Caso o código não tenha pontos testáveis suficientes, indique isso no relatório.\n\n"

        "### ESTRUTURA OBRIGATÓRIA DO OUTPUT (EM MARKDOWN)\n"
        "### Teste: <nome_do_teste>\n"
        "**Descrição:** Explicação objetiva do comportamento validado.\n"
        "**Código:** Bloco de código realista e executável baseado no projeto.\n"
        "**Justificativa:** Explicação do impacto e relevância do teste.\n\n"

        "Garanta que todos os testes reflitam o comportamento real do sistema e cubram "
        "os caminhos críticos detectados na análise do código."
    ),
    agent=tester,
    expected_output=(
        "Um arquivo Markdown (`tests.md`) contendo testes unitários completos, "
        "organizados e baseados integralmente no código real, com descrição, "
        "código e justificativa técnica clara."
    ),
    markdown=True,
    async_execution=True,
    output_file="tests.md"
)

review = Task(
    description=(
        "Leia e avalie todo o código do diretório '{diretorio}' de forma altamente criteriosa.\n\n"

        "### O QUE ANALISAR PROFUNDAMENTE:\n"
        "- Estrutura e organização do projeto\n"
        "- Boas e más práticas\n"
        "- Riscos de segurança\n"
        "- Lógica duplicada ou redundante\n"
        "- Código morto\n"
        "- Complexidade desnecessária\n"
        "- Fluxos confusos\n"
        "- Problemas de desempenho\n"
        "- Estruturas mal definidas\n"
        "- Falta de validação ou tratamento de erros\n\n"

        "### REGRAS IMPORTANTES\n"
        "- Não invente trechos de código ou problemas inexistentes.\n"
        "- Relate somente o que for **explicitamente comprovado** por arquivos reais.\n"
        "- Não passe strings 'None' para tools.\n"
        "- Valide possíveis impactos de cada falha encontrada.\n"
        "- Se detectar padrões de projeto quebrados ou inconsistências, explique tecnicamente.\n"
        "- Todas as recomendações devem vir acompanhadas de justificativa clara.\n\n"

        "### FORMATO OBRIGATÓRIO DO RELATÓRIO (MARKDOWN)\n"
        "## Resumo da Análise\n"
        "Visão geral do estado do código.\n\n"
        "## Pontos Fortes\n"
        "Aspectos positivos e bem implementados.\n\n"
        "## Problemas Identificados\n"
        "Lista detalhada, cada item com explicação técnica.\n\n"
        "## Sugestões de Melhoria\n"
        "Instruções concretas e aplicáveis.\n\n"
        "## Nível de Risco (Baixo, Médio, Alto)\n"
        "Classificação baseada no impacto e probabilidade.\n\n"

        "O relatório deve ser totalmente preciso, técnico e alinhado à realidade do código."
    ),
    agent=editor_review,
    expected_output=(
        "Um arquivo Markdown (`review.md`) contendo análise profunda, profissional, "
        "e totalmente baseada no código-fonte, incluindo riscos, falhas, pontos fortes "
        "e recomendações práticas."
    ),
    markdown=True,
    async_execution=True,
    output_file="review.md"
)