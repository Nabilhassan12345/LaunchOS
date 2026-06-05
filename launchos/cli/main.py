import typer
from rich.console import Console
from rich.panel import Panel
from launchos.utils.helpers import simulate_thinking
from launchos.core.analyzer import extract_product_context
from launchos.agents.generator import create_hooks, create_twitter_posts, create_reddit_post, create_hn_post, create_devto_outline, create_strategy
from launchos.utils.helpers import simulate_thinking, save_outputs

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
        
    console.print("[bold yellow]🔥 Top 10 Viral Hooks:[/bold yellow]")
    for i, (hook_text, score) in enumerate(hooks, 1):
        color = "green" if score >= 9 else "yellow" if score >= 7 else "white"
        console.print(f"  {i}. {hook_text} [dim](Score: [{color}]{score}/10[/{color}])[dim]")
    console.print()
        
    with console.status("[bold blue]Drafting multi-platform content...", spinner="dots"):
        simulate_thinking(1.0)
        tweets = create_twitter_posts(context, hooks)
        reddit = create_reddit_post(context)
        hn = create_hn_post(context, hooks)
        devto = create_devto_outline(context)
        
        # Format for saving
        hooks_text = "\n".join([f"{i}. {h[0]} (Score: {h[1]})" for i, h in enumerate(hooks, 1)])
        tweets_text = "\n\n---\n\n".join(tweets)
        
        save_outputs(hooks_text, tweets_text, reddit, hn, devto)
        
    console.print("[bold blue]✓ Content Generated & Saved[/bold blue]")
    console.print("  [dim]- outputs/hooks.txt[/dim]")
    console.print("  [dim]- outputs/tweets.txt[/dim]")
    console.print("  [dim]- outputs/reddit.txt[/dim]")
    console.print("  [dim]- outputs/hn.txt[/dim]")
    console.print("  [dim]- outputs/devto.txt[/dim]\n")
        
    with console.status("[bold magenta]Building launch strategy...", spinner="dots"):
        simulate_thinking(0.5)
        strategy = create_strategy()
        
    console.print("[bold magenta]🗓️ Launch Playbook:[/bold magenta]")
    for step in strategy:
        console.print(f"  [bold]•[/bold] {step}")
        
    console.print("\n[bold green]Done! You are ready to launch.[/bold green] 🚀\n")

if __name__ == "__main__":
    app()
