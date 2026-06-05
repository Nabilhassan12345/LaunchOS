from typing import Dict
from launchos.utils.helpers import fetch_github_readme

def clean_text(text: str) -> str:
    """Removes excess markdown formatting for cleaner analysis."""
    # Simple cleaner
    return text.replace('#', '').replace('*', '').strip()[:1000] # Cap length for speed

def analyze_with_llm(content: str) -> Dict[str, str]:
    """
    Simulates sending the cleaned content to an LLM (e.g., OpenAI/Gemini)
    to extract the core product schema.
    """
    # In a production version, this would be an actual API call.
    text = content.lower()
    
    # 1. Target Audience
    audience = "Developers"
    if any(k in text for k in ["b2b", "sales", "revenue"]):
        audience = "Founders & Sales"
    elif any(k in text for k in ["design", "ui", "figma"]):
        audience = "Designers"
        
    # 2. Category
    category = "Developer Tool"
    if "saas" in text:
        category = "B2B SaaS"
    elif "ai" in text or "llm" in text:
        category = "AI Application"
        
    # 3. Product Summary
    summary = content[:150] + "..." if len(content) > 150 else content
    
    # 4. Core Value Prop
    value_prop = "Saves time and automates manual tasks."
    if "fast" in text or "speed" in text:
        value_prop = "10x faster execution and performance."
        
    return {
        "summary": summary.replace('\n', ' ').strip(),
        "audience": audience,
        "value_prop": value_prop,
        "category": category
    }

def extract_product_context(input_data: str) -> Dict[str, str]:
    """Analyzes a GitHub URL or raw description to extract product details."""
    
    if input_data.startswith("http"):
        # 1. Fetch README from GitHub
        raw_content = fetch_github_readme(input_data)
        if not raw_content:
            raw_content = f"Could not fetch README from {input_data}. Assuming generic repo."
    else:
        # 2. Use plain text description
        raw_content = input_data
        
    # 3. Clean and extract
    cleaned_content = clean_text(raw_content)
    
    # 4. Analyze using LLM
    analysis = analyze_with_llm(cleaned_content)
    
    return analysis
