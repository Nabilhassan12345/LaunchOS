import time

def simulate_thinking(seconds: float = 1.0):
    """Simple utility to simulate API latency or thinking time."""
    time.sleep(seconds)

def format_output(title: str, items: list) -> str:
    """Formats a list of items into a clean CLI string."""
    header = f"\n=== {title.upper()} ===\n"
    body = "\n".join([f"- {item}" for item in items])
    return header + body + "\n"
