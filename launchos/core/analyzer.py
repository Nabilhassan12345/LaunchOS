from typing import Dict

def extract_product_context(description: str) -> Dict[str, str]:
    """Analyzes the raw product idea to determine audience and value proposition."""
    # Simplified rule-based extraction to avoid heavy AI orchestration dependencies
    text = description.lower()
    
    audience = "Developers"
    if any(keyword in text for keyword in ["b2b", "sales", "revenue"]):
        audience = "Founders & Sales Teams"
    elif any(keyword in text for keyword in ["design", "ui", "figma"]):
        audience = "Designers"
        
    return {
        "audience": audience,
        "value_prop": description,
        "tone": "Punchy and direct"
    }
