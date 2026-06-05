import typer
from rich.console import Console
from rich.panel import Panel
from launchos.utils.helpers import simulate_thinking
from launchos.core.analyzer import extract_product_context
from launchos.agents.generator import create_hooks, create_posts, create_strategy

app = typer.Typer(help="LaunchOS: The AI agent that launches your products.")
console = Console()

@app.command()
def launch(description: str = typer.Argument(..., help="Describe your product in one sentence")):
    """Analyze a product idea and generate a viral launch strategy."""
    
    console.print(Panel(f"[bold magenta]🚀 LaunchOS Initializing...[/bold magenta]", border_style="magenta"))
    
    with console.status("[bold green]Analyzing product and audience...", spinner="dots"):
        simulate_thinking(1.2)
        context = extract_product_context(description)
        
    console.print(f"[bold green]✓[/bold green] Target Audience: [bold]{context['audience']}[/bold]\n")
    
    with console.status("[bold yellow]Generating viral hooks...", spinner="dots"):
        simulate_thinking(0.8)
        hooks = create_hooks(context)
        
    console.print("[bold yellow]🔥 Viral Hooks:[/bold yellow]")
    for i, hook in enumerate(hooks, 1):
        console.print(f"  {i}. {hook}")
    console.print()
        
    with console.status("[bold blue]Drafting social copy...", spinner="dots"):
        simulate_thinking(1.0)
        posts = create_posts(context, hooks)
        
    console.print("[bold blue]🐦 Social Posts:[/bold blue]")
    for post in posts:
        console.print(Panel(post, border_style="blue"))
        
    with console.status("[bold magenta]Building launch strategy...", spinner="dots"):
        simulate_thinking(0.5)
        strategy = create_strategy()
        
    console.print("[bold magenta]🗓️ Launch Playbook:[/bold magenta]")
    for step in strategy:
        console.print(f"  [bold]•[/bold] {step}")
        
    console.print("\n[bold green]Done! You are ready to launch.[/bold green] 🚀\n")

if __name__ == "__main__":
    app()
