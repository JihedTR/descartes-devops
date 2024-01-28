import os
import subprocess
from datetime import datetime

def execute_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout.strip()

def backup_files(destination_folder, commit_sha):
    execute_git_command(['git', 'checkout', commit_sha])
    
    # Backup files to the destination_folder based on commit_sha
    # Example: Copy files to destination_folder/data/<commit_sha>/...

def main():
    # Replace 'DD-MM-YYYY-test' with your desired branch
    branch_name = 'DD-MM-YYYY-test'
    repository_url = 'https://github.com/descartes-underwriting/devops-technical-test-data.git'
    
    # Clone the repository
    execute_git_command(['git', 'clone', repository_url])
    
    # Change to the repository directory
    os.chdir('devops-technical-test-data')
    
    # Get the initial commit SHA
    initial_commit_sha = execute_git_command(['git', 'rev-list', '--max-parents=0', 'HEAD'])
    
    # Iterate through commits and backup files
    commits = execute_git_command(['git', 'rev-list', '--first-parent', branch_name]).split('\n')
    for commit in commits:
        backup_files(f'data/{commit}', commit)
    
if __name__ == "__main__":
    main()
