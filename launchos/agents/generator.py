from typing import List, Dict

def create_hooks(context: Dict[str, str]) -> List[str]:
    """Generates viral hooks based on the extracted context."""
    audience = context["audience"]
    return [
        f"Stop wasting time. I just built a tool specifically for {audience}.",
        f"The hardest part of building for {audience} is over. Meet the solution.",
        f"I was tired of doing this manually. So I automated it. Here's how:"
    ]

def create_posts(context: Dict[str, str], hooks: List[str]) -> List[str]:
    """Generates ready-to-publish social media copy."""
    return [
        f"{hooks[0]}\n\nI just open-sourced {context['value_prop']}. It's built to be blazing fast and completely free.\n\nCheck out the repo below 👇\n#buildinpublic",
        f"{hooks[2]}\n\nThis took me weeks to build, but it will save you hours today. It's fully open source.\n\nLink in the thread 🧵"
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
