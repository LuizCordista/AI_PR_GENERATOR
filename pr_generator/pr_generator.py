#!/usr/bin/env python3
from dotenv import load_dotenv
from pr_generator import chat_completition, git_manager, template_manager
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate PR message based on git diff')
    parser.add_argument('--base', '-b', default='main',
                      help='Base branch to compare against (default: main)')
    parser.add_argument('--template', '-t', default='default.md',
                      help='Template .md file to use (default: default.md)')
    parser.add_argument('--list-templates', action='store_true',
                      help='List available templates and exit')
    parser.add_argument('--commit', action='store_true',
                      help='Auto generates the commit message')
    args = parser.parse_args()

    if args.list_templates:
        templates = template_manager.list_templates()
        print('Available templates:')
        for t in templates:
            print(f'- {t}')
        return

    load_dotenv(override=True)

    if args.commit:
        diff = git_manager.get_commit_diff()
    else:
        diff = git_manager.get_git_diff(base_branch=args.base)
    if not diff:
        print("No changes found")
        return

    # Use generic chatCompletion interface
    if args.commit:
        prompt = git_manager.generate_commit_message(diff, template_name='commit.md')
    else:
        prompt = git_manager.generate_pr_message(diff, template_name=args.template)
    result = chat_completition.chatCompletion(prompt)
    print("\nGenerated PR Message:")
    print("=" * 50)
    print(result.content)
    print("=" * 50)

if __name__ == "__main__":
    main()