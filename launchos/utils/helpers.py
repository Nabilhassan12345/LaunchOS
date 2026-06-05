import time
import requests

def simulate_thinking(seconds: float = 1.0):
    """Simple utility to simulate API latency or thinking time."""
    time.sleep(seconds)

def format_output(title: str, items: list) -> str:
    """Formats a list of items into a clean CLI string."""
    header = f"\n=== {title.upper()} ===\n"
    body = "\n".join([f"- {item}" for item in items])
    return header + body + "\n"

def fetch_github_readme(repo_url: str) -> str:
    """Fetches the README.md content from a GitHub repository URL."""
    # Convert https://github.com/user/repo to https://raw.githubusercontent.com/user/repo/main/README.md
    if not repo_url.startswith("https://github.com/"):
        return ""
        
    parts = repo_url.replace("https://github.com/", "").split("/")
    if len(parts) < 2:
        return ""
        
    user, repo = parts[0], parts[1]
    
    # Try main branch first, then master
    for branch in ["main", "master"]:
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/README.md"
        response = requests.get(raw_url)
        if response.status_code == 200:
            return response.text
            
    return ""
