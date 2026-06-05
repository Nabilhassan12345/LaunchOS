import typer
from rich.console import Console
from rich.panel import Panel
from launchos.utils.helpers import simulate_thinking
from launchos.core.analyzer import extract_product_context
from launchos.agents.generator import create_hooks, create_twitter_posts, create_reddit_post, create_hn_post, create_devto_outline, create_strategy, get_distribution_strategy
from launchos.utils.helpers import simulate_thinking, save_outputs

app = typer.Typer(help="LaunchOS: The AI agent that launches your products.")
console = Console()

@app.command()
def analyze(input_data: str = typer.Argument(..., help="GitHub repo URL OR plain text description")):
    """Analyze a product idea and generate a viral launch strategy."""
    
    # Clear the screen for a fresh, exciting launch experience
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    console.print(Panel(f"[bold cyan]⚡ LaunchOS V1.0[/bold cyan]\n[italic]The open-source AI agent that launches your products.[/italic]", border_style="cyan", padding=(1, 2)))
    console.print()
    
    with console.status("[bold green]📡 Fetching and analyzing product...", spinner="bouncingBar"):
        simulate_thinking(1.2)
        context = extract_product_context(input_data)
        
    console.print("[bold green]✨ Analysis Complete![/bold green]\n")
    console.print(f"  [cyan]📦 Category:[/cyan]        [bold white]{context['category']}[/bold white]")
    console.print(f"  [cyan]🎯 Target Audience:[/cyan] [bold white]{context['audience']}[/bold white]")
    console.print(f"  [cyan]💎 Value Prop:[/cyan]      [bold white]{context['value_prop']}[/bold white]")
    console.print(f"  [cyan]📝 Summary:[/cyan]         {context['summary']}\n")
    
    with console.status("[bold yellow]⚡ Generating viral hooks...", spinner="bouncingBar"):
        simulate_thinking(0.8)
        hooks = create_hooks(context)
        
    console.print("[bold yellow]🔥 Top 10 Viral Hooks:[/bold yellow]")
    for i, (hook_text, score) in enumerate(hooks, 1):
        color = "green" if score >= 9 else "yellow" if score >= 7 else "white"
        console.print(f"  [bold]{i}.[/bold] {hook_text} [dim](Score: [{color}]{score}/10[/{color}])[dim]")
    console.print()
        
    with console.status("[bold blue]✍️ Drafting multi-platform content...", spinner="bouncingBar"):
        simulate_thinking(1.0)
        tweets = create_twitter_posts(context, hooks)
        reddit = create_reddit_post(context)
        hn = create_hn_post(context, hooks)
        devto = create_devto_outline(context)
        
        # Format for saving
        hooks_text = "\n".join([f"{i}. {h[0]} (Score: {h[1]})" for i, h in enumerate(hooks, 1)])
        tweets_text = "\n\n---\n\n".join(tweets)
        
    with console.status("[bold magenta]🧠 Building launch strategy...", spinner="bouncingBar"):
        simulate_thinking(0.5)
        strategy = create_strategy()
        
        # Format strategy for saving
        strategy_text_lines = []
        for day_plan in strategy:
            strategy_text_lines.append(f"{day_plan['day']}:")
            for task in day_plan['tasks']:
                strategy_text_lines.append(f"- {task}")
            strategy_text_lines.append("")
        strategy_text = "\n".join(strategy_text_lines)
        
        save_outputs(hooks_text, tweets_text, reddit, hn, devto, strategy_text)
        
    console.print("[bold blue]✅ Content Generated & Saved[/bold blue]")
    console.print("  [dim]- outputs/hooks.txt[/dim]")
    console.print("  [dim]- outputs/tweets.txt[/dim]")
    console.print("  [dim]- outputs/reddit.txt[/dim]")
    console.print("  [dim]- outputs/hn.txt[/dim]")
    console.print("  [dim]- outputs/devto.txt[/dim]")
    console.print("  [dim]- outputs/strategy.txt[/dim]\n")
        
    with console.status("[bold cyan]🔍 Analyzing distribution channels...", spinner="bouncingBar"):
        simulate_thinking(0.8)
        distribution = get_distribution_strategy(context["category"])
        
    console.print("[bold cyan]🎯 Distribution Targets:[/bold cyan]")
    console.print("  [cyan]▶ Subreddits:[/cyan]  [bold white]" + ", ".join(distribution["subreddits"]) + "[/bold white]")
    console.print("  [cyan]▶ Communities:[/cyan] [bold white]" + ", ".join(distribution["communities"]) + "[/bold white]")
    console.print("\n[bold cyan]💡 Launch Tips:[/bold cyan]")
    for tip in distribution["tips"]:
        console.print(f"  [bold cyan]•[/bold cyan] {tip}")
    console.print()
        
    console.print("[bold magenta]🗓️ 7-Day Launch Playbook:[/bold magenta]")
    for day_plan in strategy:
        console.print(f"  [bold underline]{day_plan['day']}[/bold underline]")
        for task in day_plan['tasks']:
            console.print(f"    [bold magenta]👉[/bold magenta] {task}")
        console.print()
        
    console.print(Panel("[bold green]🚀 DONE! Your launch assets are ready. Go ship it.[/bold green]", border_style="green", expand=False))
    console.print()

if __name__ == "__main__":
    app()
