# ⚡ LaunchOS

> I built an AI that launches your product for you.

You spend 3 weeks building the perfect app, and 3 minutes launching it. That's why you have 0 users.
**LaunchOS** is an open-source, CLI-first AI agent that takes your repo URL and generates a complete, viral launch operation in 10 seconds.

---

## 🚀 Demo

```bash
python main.py analyze "https://github.com/user/my-awesome-repo"
```
*(Insert animated GIF here showing the CLI generating hooks and playbooks)*

---

## ✨ Features

- **🧠 Auto-Analysis**: Pass it a GitHub URL or text. It extracts your target audience, value prop, and category automatically.
- **🔥 Hook Generator**: Generates 10 outcome-focused, curiosity-driven hooks scored by viral potential (1-10).
- **✍️ Multi-Platform Content**: Automatically writes optimized posts for Twitter/X, Reddit (story-style), Hacker News (Show HN), and Dev.to.
- **🎯 Distribution Strategy**: Tells you exactly which subreddits and communities to post in based on your product category.
- **🗓️ 7-Day Playbook**: Gives you a structured, step-by-step launch plan so you know exactly what to do and when.

---

## ⚡ Quickstart

No bloated orchestration frameworks. Zero abstraction. Just pure execution.

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/LaunchOS.git
   cd LaunchOS
   ```
2. **Install minimal dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the agent:**
   ```bash
   python main.py analyze "A fast, minimal markdown editor for developers"
   ```

---

## 📈 Example Output

```text
⚡ LaunchOS V1.0
The open-source AI agent that launches your products.

📡 Fetching and analyzing product...
✨ Analysis Complete!

  📦 Category:        Developer Tool
  🎯 Target Audience: Developers
  💎 Value Prop:      10x faster execution and performance.
  📝 Summary:         A fast, minimal markdown editor for developers

⚡ Generating viral hooks...
🔥 Top 10 Viral Hooks:
  1. This new developer tool I built 10x faster execution and performance.—and it's completely free. (Score: 10/10)
  2. I got tired of the old way, so I built a developer tool that completely changes how we work. (Score: 9/10)
  3. I built a developer tool that 10x faster execution and performance. so you never have to do it manually again. (Score: 9/10)

🔍 Analyzing distribution channels...
🎯 Distribution Targets:
  ▶ Subreddits:  r/programming, r/webdev, r/Python, r/reactjs
  ▶ Communities: Hacker News (Show HN), Dev.to, Hashnode, GitHub Trending

💡 Launch Tips:
  • Make sure your README has a GIF showing the tool in action within 5 seconds.
  • Don't just drop a link. Tell the story of WHY you built it.

🗓️ 7-Day Launch Playbook:
  Day 1
    👉 Post 'teaser' screenshot or architecture diagram on Twitter/X
    👉 DM 15 highly engaged followers or beta users offering early access

  Day 2
    👉 Launch on Product Hunt at 12:01 AM PST
    👉 Publish the main launch thread on Twitter/X
    👉 Cross-post to Hacker News ('Show HN: ...') at 8:00 AM EST

✅ Content Generated & Saved
  - outputs/hooks.txt
  - outputs/tweets.txt
  - outputs/reddit.txt
  - outputs/hn.txt
  - outputs/devto.txt
  - outputs/strategy.txt

🚀 DONE! Your launch assets are ready. Go ship it.
```

---

## 🤝 Contributing

We want to make this the ultimate open-source launch engine for developers. PRs are highly encouraged!
