import os
import subprocess

def init_git_repo_if_needed(repo_path: str, remote_url: str):
    """
    Initializes Git repo and sets global credentials. Adds remote origin safely.
    """
    if not os.path.exists(os.path.join(repo_path, ".git")):
        subprocess.run(["git", "init"], cwd=repo_path, check=True)
        subprocess.run(["git", "checkout", "-b", "main"], cwd=repo_path, check=True)

    # Set Git global user info
    git_user = os.getenv("GIT_USERNAME", "sivachandra422")
    git_email = os.getenv("GIT_EMAIL", "siva.sivachandra23@gmail.com")

    subprocess.run(["git", "config", "--global", "user.name", git_user], check=True)
    subprocess.run(["git", "config", "--global", "user.email", git_email], check=True)

    # Inject PAT into remote URL
    token = os.getenv("GIT_PAT")
    if not token:
        raise EnvironmentError("GIT_PAT not found in environment variables.")

    auth_url = remote_url.replace("https://", f"https://{token}@")

    # Check if origin exists
    result = subprocess.run(["git", "remote"], cwd=repo_path, capture_output=True, text=True)
    remotes = result.stdout.strip().splitlines()

    if "origin" in remotes:
        subprocess.run(["git", "remote", "set-url", "origin", auth_url], cwd=repo_path, check=True)
    else:
        subprocess.run(["git", "remote", "add", "origin", auth_url], cwd=repo_path, check=True)


def push_changes(repo_path: str, commit_message: str):
    """
    Commits and pushes changes to the repo using secure PAT-based remote.
    """
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)

    # Skip commit if no changes
    result = subprocess.run(["git", "status", "--porcelain"], cwd=repo_path, capture_output=True, text=True)
    if not result.stdout.strip():
        raise Exception("No changes to commit.")

    subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)

    # Push changes
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=repo_path, check=True)