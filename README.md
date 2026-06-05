# 🚀 LaunchOS

The open-source AI agent that launches your products for you. Built to be minimal, clean, and CLI-first.

## ⚡ Quickstart

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Launch it: `python main.py "A new CLI tool that automates git rebasing"`

## 🛠️ Architecture

Built on a philosophy of **Zero Abstraction**:
- `launchos/cli/` - The entrypoint using `Typer` and `rich`.
- `launchos/core/` - Simple functions. No deep class inheritance.
- `launchos/agents/` - Functions that generate hooks, posts, and strategies.
- `launchos/utils/` - Shared helpers.

## 🤝 Contributing
Open a Pull Request to help us make this the ultimate open-source launch engine.
