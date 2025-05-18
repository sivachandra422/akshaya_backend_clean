import os
import subprocess

def init_git_repo_if_needed(repo_path: str, remote_url: str):
    """
    Initializes a Git repository if it doesn't already exist.
    Sets up remote origin and configures user credentials.
    """
    git_dir = os.path.join(repo_path, ".git")
    if not os.path.exists(git_dir):
        subprocess.run(["git", "init"], cwd=repo_path, check=True)
        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=repo_path, check=True)
        subprocess.run(["git", "checkout", "-b", "main"], cwd=repo_path, check=True)

    # Set Git credentials globally
    git_user = os.getenv("GIT_USERNAME", "sivachandra422")
    git_email = os.getenv("GIT_EMAIL", "siva.sivachandra23@gmail.com")

    subprocess.run(["git", "config", "--global", "user.name", git_user], check=True)
    subprocess.run(["git", "config", "--global", "user.email", git_email], check=True)


def push_changes(repo_path: str, commit_message: str):
    """
    Commits changes and pushes to the origin using a PAT token securely.
    """
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
    status = subprocess.run(["git", "status", "--porcelain"], cwd=repo_path, capture_output=True, text=True)

    if not status.stdout.strip():
        raise Exception("No changes to commit.")

    subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)

    token = os.getenv("GIT_PAT")
    remote_url = os.getenv("GIT_REMOTE_URL")

    if not token or not remote_url:
        raise EnvironmentError("Missing GIT_PAT or GIT_REMOTE_URL")

    # Inject PAT into the remote URL
    auth_url = remote_url.replace("https://", f"https://{token}@")

    subprocess.run(["git", "remote", "set-url", "origin", auth_url], cwd=repo_path, check=True)

    # Push changes with force and upstream
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_path, check=True)