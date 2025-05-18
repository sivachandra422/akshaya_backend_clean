import os
import subprocess

def init_git_repo_if_needed(repo_path: str, remote_url: str):
    # Initialize only if not already a git repo
    if not os.path.exists(os.path.join(repo_path, ".git")):
        subprocess.run(["git", "init"], cwd=repo_path, check=True)
        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=repo_path, check=True)
        subprocess.run(["git", "checkout", "-b", "main"], cwd=repo_path, check=True)

    # Set Git credentials globally
    git_user = os.getenv("GIT_USERNAME", "sivachandra422")
    git_email = os.getenv("GIT_EMAIL", "siva.sivachandra23@gmail.com")
    subprocess.run(["git", "config", "user.name", git_user], cwd=repo_path, check=True)
    subprocess.run(["git", "config", "user.email", git_email], cwd=repo_path, check=True)

def push_changes(repo_path: str, commit_message: str):
    # Check for changes
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
    result = subprocess.run(["git", "status", "--porcelain"], cwd=repo_path, capture_output=True, text=True)
    if not result.stdout.strip():
        raise Exception("No changes to commit.")

    subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)

    # Use PAT token
    token = os.getenv("GIT_PAT")
    remote_url = os.getenv("GIT_REMOTE_URL")
    if token:
        auth_url = remote_url.replace("https://", f"https://{token}@")
        subprocess.run(["git", "remote", "set-url", "origin", auth_url], cwd=repo_path, check=True)

    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_path, check=True)