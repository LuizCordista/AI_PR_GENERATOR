import git
import sys
from pr_generator import template_manager 


def get_git_diff(repo_path='.', base_branch='main'):
    try:
        repo = git.Repo(repo_path, search_parent_directories=True)
        current_branch = repo.active_branch.name
        diff = repo.git.diff(f'{base_branch}...{current_branch}')
        return diff
    except git.exc.InvalidGitRepositoryError:
        print("Error: Not a git repository")
        sys.exit(1)
    except git.exc.GitCommandError as e:
        print(f"Git error: {e}")
        sys.exit(1)


def get_commit_diff(repo_path='.'):
    try:
        repo = git.Repo(repo_path, search_parent_directories=True)

        unstaged = repo.git.diff(None)

        staged = repo.git.diff('--staged')
        
        all_changes = unstaged + staged
        
        if not all_changes:
            print("No unstaged changes")
            return None
        
        return all_changes

    except git.exc.InvalidGitRepositoryError:
        print("Erro: Não é um repositório Git válido.")
        sys.exit(1)

    except git.exc.GitCommandError as e:
        print(f"Erro Git: {e}")
        sys.exit(1)

def generate_pr_message(diff_text, template_name='default.md'):
    template = template_manager.load_template(template_name)
    return template.replace('{{diff}}', diff_text)

def generate_commit_message(commit_diff, template_name='commit.md'):
    template = template_manager.load_template(template_name)
    return template.replace('{{diff}}', commit_diff)