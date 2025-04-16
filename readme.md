# PR Generator

PR Generator é uma ferramenta CLI que automaticamente gera mensagens de Pull Request usando IA, baseando-se nas mudanças do seu código (git diff).

## Requisitos

- Python 3.12 ou superior
- Git
- `pipx` (para instalação global isolada)

## Instalação

Recomendamos usar `pipx` para instalar a ferramenta globalmente em um ambiente isolado.

1.  **Instale `pipx`** (se ainda não tiver):
    ```bash
    python -m pip install --user pipx
    python -m pipx ensurepath
    ```
    *Nota: Pode ser necessário reiniciar o terminal após `ensurepath`.*

2.  **Clone o repositório:**
    ```bash
    git clone [url-do-repositorio]
    cd Pr_generator
    ```

3.  **Instale usando `pipx`:**
    ```bash
    pipx install .
    ```
    Isso tornará o comando `pr-generator` disponível globalmente.

*(Opcional: Para desenvolvimento, siga os passos de ambiente virtual abaixo)*

### Instalação para Desenvolvimento

Se você pretende contribuir com o projeto:

1.  Clone o repositório (se ainda não o fez).
2.  Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    # ou
    venv\Scripts\activate     # Windows
    ```
3.  Instale o pacote em modo de desenvolvimento:
    ```bash
    pip install -e .[dev] # Instala dependências de desenvolvimento também (se houver)
    # ou apenas
    pip install -e .
    ```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
LLM_API_URL="url-da-api"
LLM_API_KEY="sua-api-key"
LLM_MODEL="nome-do-modelo" # Exemplo: gpt-3.5-turbo
# Opcional: LLM_HEADERS={"Custom-Header": "valor"}
```

## Uso

O PR Generator pode ser usado diretamente pela linha de comando após a instalação:

```bash
pr-generator [--base BRANCH] [--template TEMPLATE] [--list-templates]
```

Opções:
- `--base` ou `-b`: Branch base para comparação (default: 'main')
- `--template` ou `-t`: Template .md a ser usado (default: 'default.md')
- `--list-templates`: Lista os templates disponíveis e sai

Exemplo:
```bash
pr-generator --base develop --template meu_template.md
```

Para listar os templates disponíveis:
```bash
pr-generator --list-templates
```

### Como adicionar novos templates

1. Crie um arquivo `.md` com o formato desejado na pasta `pr_generator/templates/`.
2. Use o nome do arquivo com a opção `--template` ao rodar o comando.
   - Exemplo: `pr-generator --template meu_template.md`

O template padrão é o `default.md`. Você pode criar quantos templates quiser, basta adicioná-los na pasta `pr_generator/templates/`.

O comando irá:
1. Recuperar o diff entre sua branch atual e a branch base
2. Gerar uma mensagem de PR formatada usando IA e o template escolhido
3. Exibir a mensagem gerada no terminal

A mensagem gerada seguirá o formato do template selecionado.

## Desenvolvimento

Para contribuir com o projeto:

1. Fork o repositório
2. Crie sua feature branch (`git checkout -b feat/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feat/MinhaFeature`)
5. Abra um Pull Request