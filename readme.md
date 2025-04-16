# PR Generator

PR Generator is a CLI tool that automatically generates Pull Request messages using AI, based on your code changes (git diff).

## Requirements

- Python 3.12 or higher
- Git
- `pipx` (for global isolated installation)

## Installation

We recommend using `pipx` to install the tool globally in an isolated environment.

1. **Install `pipx`** (if you don't have it yet):
    ```bash
    python -m pip install --user pipx
    python -m pipx ensurepath
    ```
    *Note: You may need to restart your terminal after running `ensurepath`.*

2. **Clone the repository:**
    ```bash
    git clone [repository-url]
    cd Pr_generator
    ```

3. **Install using `pipx`:**
    ```bash
    pipx install .
    ```
    This will make the `pr-generator` command available globally.

*(Optional: For development, follow the virtual environment steps below)*

### Development Installation

If you want to contribute to the project:

1. Clone the repository (if you haven't already).
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    # or
    venv\Scripts\activate     # Windows
    ```
3. Install the package in development mode:
    ```bash
    pip install -e .[dev] # Installs dev dependencies if any
    # or just
    pip install -e .
    ```

## Configuration

Create a `.env` file at the root of the project with the following variables:

```env
LLM_API_URL="your-api-url"
LLM_API_KEY="your-api-key"
LLM_MODEL="model-name" # Example: gpt-3.5-turbo
# Optional: LLM_HEADERS={"Custom-Header": "value"}
```

## Usage

PR Generator can be used directly from the command line after installation:

```bash
pr-generator [--base BRANCH] [--template TEMPLATE] [--list-templates] [--commit]
```

Options:
- `--base` or `-b`: Base branch for comparison (default: 'main')
- `--template` or `-t`: .md template to use (default: 'default.md')
- `--list-templates`: List available templates and exit
- `--commit`: Automatically generates a conventional commit message instead of a Pull Request message

Examples:

Generate a Pull Request message:
```bash
pr-generator --base develop --template my_template.md
```

Generate a conventional commit message:
```bash
pr-generator --commit
```

List available templates:
```bash
pr-generator --list-templates
```

### How to add new templates

1. Create a `.md` file with your desired format in the `pr_generator/templates/` folder.
2. Use the file name with the `--template` option when running the command.
   - Example: `pr-generator --template my_template.md`

The default template is `default.md`. You can create as many templates as you want, just add them to the `pr_generator/templates/` folder.

The command will:
1. Retrieve the diff between your current branch and the base branch
2. Generate a formatted PR message using AI and the selected template
3. Display the generated message in the terminal

The generated message will follow the format of the selected template.

## Contributing

To contribute to the project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/MyFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feat/MyFeature`)
5. Open a Pull Request