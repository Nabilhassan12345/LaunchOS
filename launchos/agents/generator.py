from typing import List, Dict, Tuple

def create_hooks(context: Dict[str, str]) -> List[Tuple[str, int]]:
    """
    Generates 10 viral hooks based on the product context.
    Assigns a virality score (1-10) and sorts them best to worst.
    """
    audience = context.get("audience", "developers").lower()
    value = context.get("value_prop", "saves you hours").lower()
    category = context.get("category", "tool").lower()

    # Templates: short, curiosity-driven, outcome-focused, "I built X that does Y"
    raw_hooks = [
        (f"I built a {category} that {value} so you never have to do it manually again.", 9),
        (f"Stop wasting time; I built the ultimate {category} for {audience}.", 6),
        (f"If you are one of the {audience}, you need to see this {category} that {value}.", 8),
        (f"I got tired of the old way, so I built a {category} that completely changes how we work.", 9),
        (f"This new {category} I built {value}—and it's completely free.", 10),
        (f"I built a tiny {category} that {value}. Here is exactly how it works:", 8),
        (f"Don't build another {category} until you see how this one {value}.", 7),
        (f"I spent weeks building a {category} so {audience} can get results in seconds.", 9),
        (f"The hardest part of being in {audience} is over; I built a {category} that fixes it.", 7),
        (f"I built the exact {category} I wished I had when I started—it {value}.", 8)
    ]
    
def create_twitter_posts(context: Dict[str, str], hooks: List[Tuple[str, int]]) -> List[str]:
    """Generates 5 short, engaging Twitter/X posts."""
    value = context.get('value_prop', 'this tool')
    category = context.get('category', 'SaaS')
    
    # We use some of the best hooks as starting points
    return [
        f"{hooks[0][0]}\n\nI just open-sourced {value}. Built to be blazing fast and completely free.\n\nLink below 👇 #buildinpublic",
        f"{hooks[1][0]}\n\nThis took weeks to build, but it'll save you hours today. Fully open source. 🧵",
        f"Just shipped my new {category}! If you hate doing things manually, you're going to love this.\n\nRepo is public now.",
        f"What's the hardest part about building? For me, it was {value}. So I automated it. Check it out.",
        f"{hooks[3][0]}\n\nIt's live now. Would love feedback from the community! 👇"
    ]

def create_reddit_post(context: Dict[str, str]) -> str:
    """Generates a story-style Reddit post."""
    value = context.get('value_prop', 'saving time')
    audience = context.get('audience', 'developers')
    category = context.get('category', 'side project')
    
    return f"""Title: I got so frustrated with existing tools that I spent the last 3 weeks building my own {category}.

Hey r/{audience.replace(' ', '').lower()},

I've been dealing with {value} for a while now, and honestly, the existing solutions were either too expensive or too bloated. 

So I decided to scratch my own itch. I built a lightweight, open-source alternative. It doesn't do everything, but it does the core thing really well.

I just made the repo public today. I'd love to get some honest feedback from this community. What features would make this actually useful for your workflow?"""

def create_hn_post(context: Dict[str, str], hooks: List[Tuple[str, int]]) -> str:
    """Generates a Show HN style post."""
    value = context.get('value_prop', 'saving time')
    category = context.get('category', 'tool')
    
    return f"""Title: Show HN: A {category} for {value}

Hi HN,

I'm the creator of this project. {hooks[0][0]} 

I built this because I noticed a gap in the current ecosystem where existing tools are overly complex. The architecture is kept deliberately simple with zero unnecessary abstractions. 

Tech stack is standard, optimized for readability and speed.

Repo: [Link]

Happy to answer any technical questions about the implementation!"""

def create_devto_outline(context: Dict[str, str]) -> str:
    """Generates an article outline for Dev.to."""
    value = context.get('value_prop', 'saving time')
    
    return f"""Title: How I automated {value} using open-source tools

Outline:
1. Introduction
   - The pain point: Why existing solutions suck
   - The "aha" moment
2. Architecture & Tech Stack
   - Why I chose these specific tools
   - Keeping it simple
3. The Core Implementation
   - Code snippet showing the main engine
   - Overcoming [Challenge]
4. Results
   - Performance metrics
   - Next steps on the roadmap
5. Conclusion
   - Link to the GitHub repo
   - Call to action for contributors"""

def create_strategy() -> List[str]:
    """Generates a day-by-day launch checklist."""
    return [
        "Day -2: Post a 'teaser' screenshot on Twitter/X.",
        "Day -1: DM 15 highly engaged followers offering early access.",
        "Day 0: Launch on Product Hunt at 12:01 AM PST.",
        "Day 0: Publish the main launch thread on Twitter/X.",
        "Day 0: Cross-post to Hacker News ('Show HN: ...') at 8:00 AM EST.",
        "Day 1: Reply to all comments. Post a 'behind the scenes' technical breakdown."
    ]
