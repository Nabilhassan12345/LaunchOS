import typer
from rich.console import Console
from rich.panel import Panel
from launchos.utils.helpers import simulate_thinking
from launchos.core.analyzer import extract_product_context
from launchos.agents.generator import create_hooks, create_posts, create_strategy

app = typer.Typer(help="LaunchOS: The AI agent that launches your products.")
console = Console()

@app.command()
def launch(input_data: str = typer.Argument(..., help="GitHub repo URL OR plain text description")):
    """Analyze a product idea and generate a viral launch strategy."""
    
    console.print(Panel(f"[bold magenta]🚀 LaunchOS Initializing...[/bold magenta]", border_style="magenta"))
    
    with console.status("[bold green]Fetching and analyzing product...", spinner="dots"):
        simulate_thinking(1.2)
        context = extract_product_context(input_data)
        
    console.print("[bold green]✓ Analysis Complete[/bold green]\n")
    console.print(f"  [dim]Category:[/dim] [bold]{context['category']}[/bold]")
    console.print(f"  [dim]Target Audience:[/dim] [bold]{context['audience']}[/bold]")
    console.print(f"  [dim]Value Prop:[/dim] [bold]{context['value_prop']}[/bold]")
    console.print(f"  [dim]Summary:[/dim] {context['summary']}\n")
    
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
