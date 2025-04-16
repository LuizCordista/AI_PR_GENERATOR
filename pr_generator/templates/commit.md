# Gerador de Mensagem de Commit Convencional

Este script analisa um git diff e gera uma mensagem de commit convencional apropriada.

## Entrada

Cole o git diff abaixo:

{{diff}}

## Instruções

1. Analise o diff fornecido.
2. Determine o tipo de alteração (feat, fix, docs, style, refactor, perf, test, chore).
3. Identifique o escopo da alteração, se aplicável.
4. Crie uma descrição curta e significativa da alteração.
5. Se necessário, adicione um corpo mais detalhado à mensagem do commit.
6. Se houver quebras de mudanças, adicione um rodapé com os detalhes.

## Saída

Com base na análise do diff, aqui está a mensagem de commit convencional sugerida:

<tipo>(<escopo>): <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]


### Explicação

- **Tipo**: O tipo de alteração (feat, fix, docs, etc.)
- **Escopo**: A parte do código afetada (opcional)
- **Descrição**: Breve descrição da alteração
- **Corpo**: Detalhes adicionais, se necessário
- **Rodapé**: Informações sobre quebras de mudanças, se houver

## Observações Adicionais

- A linha de assunto (primeira linha) não deve ter mais de 50 caracteres
- O corpo deve ser quebrado em 72 caracteres
- Use o tempo verbal no presente ("adiciona feature" não "adicionou feature")
- O corpo deve explicar o "o quê" e o "por quê", não o "como"

Sempre retorne em ingles
