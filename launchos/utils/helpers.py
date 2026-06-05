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
    """Fetches the README.md content from a GitHub repository URL safely."""
    if not repo_url.startswith("https://github.com/"):
        return ""
        
    parts = repo_url.replace("https://github.com/", "").split("/")
    if len(parts) < 2:
        return ""
        
    user, repo = parts[0], parts[1]
    
    try:
        for branch in ["main", "master"]:
            raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/README.md"
            response = requests.get(raw_url, timeout=10)
            if response.status_code == 200:
                return response.text
    except requests.RequestException:
        pass # Fallback to empty string on network failure
            
    return ""

def save_outputs(hooks: str, tweets: str, reddit: str, hn: str, devto: str, strategy: str, readme: str) -> bool:
    """Saves all generated content to the outputs directory safely."""
    import os
    try:
        os.makedirs("outputs", exist_ok=True)
        
        with open("outputs/hooks.txt", "w", encoding="utf-8") as f:
            f.write(hooks)
        with open("outputs/tweets.txt", "w", encoding="utf-8") as f:
            f.write(tweets)
        with open("outputs/reddit.txt", "w", encoding="utf-8") as f:
            f.write(reddit)
        with open("outputs/hn.txt", "w", encoding="utf-8") as f:
            f.write(hn)
        with open("outputs/devto.txt", "w", encoding="utf-8") as f:
            f.write(devto)
        with open("outputs/strategy.txt", "w", encoding="utf-8") as f:
            f.write(strategy)
        with open("outputs/readme_viral.md", "w", encoding="utf-8") as f:
            f.write(readme)
        return True
    except IOError as e:
        print(f"Error saving files: {e}")
        return False
