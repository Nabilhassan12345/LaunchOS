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
    
    # Sort best -> worst
    sorted_hooks = sorted(raw_hooks, key=lambda x: x[1], reverse=True)
    return sorted_hooks

def create_posts(context: Dict[str, str], hooks: List[Tuple[str, int]]) -> List[str]:
    """Generates ready-to-publish social media copy."""
    # Use the top hook and third hook for the posts
    hook_1 = hooks[0][0] if len(hooks) > 0 else "Check this out!"
    hook_3 = hooks[2][0] if len(hooks) > 2 else "You won't believe this."
    
    return [
        f"{hook_1}\n\nI just open-sourced {context.get('value_prop', 'this tool')}. It's built to be blazing fast and completely free.\n\nCheck out the repo below 👇\n#buildinpublic",
        f"{hook_3}\n\nThis took me weeks to build, but it will save you hours today. It's fully open source.\n\nLink in the thread 🧵"
    ]

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
