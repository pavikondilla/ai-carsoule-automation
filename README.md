# 🤖 AI News Carousel Automation

> Automated Instagram carousel generation for AI news with Gen Z aesthetics
> **@auraman.ai**

## What This Does

Every day, this tool:
1. **Scrapes** trending AI news from 4+ sources (TechCrunch, The Verge, Ars Technica, Reddit)
2. **Generates** 5 creative carousels with mixed Gen Z templates
3. **Creates** ready-to-post Instagram captions with hashtags
4. **Saves** everything to a dated folder for easy access

## Templates Included

| Template | Style | Best For |
|----------|-------|----------|
| 🔥 Hot Take | Bold gradients, aggressive | Breaking news |
| 🪟 Glassmorphism | Modern, clean | Professional updates |
| ✨ Y2K Core | Pastel, retro | Trendy/viral content |
| 💜 Neon | Cyberpunk, dark | Tech breakthroughs |
| 🧴 Minimal | Clean girl aesthetic | Business/policy news |

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Run the Automation

```bash
python run.py
```

Or on Windows, double-click `run.bat`

### 3. Find Your Carousels

Output goes to: `output/YYYY-MM-DD/`

```
output/2024-01-15/
├── carousel_0_slide_1.png    # Cover slide
├── carousel_0_slide_2.png    # News content
├── carousel_0_slide_3.png    # CTA slide
├── carousel_1_slide_1.png
├── ...
├── captions.txt              # Ready-to-copy captions
└── news.json                 # Raw news data
```

## Daily Workflow

```
8 AM: Run script → Check output folder
         ↓
Review carousels → Pick your favorite
         ↓
Copy caption from captions.txt
         ↓
Upload to Instagram manually
```

## Customization

### Change Number of Carousels
Edit `run.py`, line 45:
```python
news = fetcher.get_trending_news(limit=5)  # Change to 3 or 10
```

### Add More News Sources
Edit `scraper/news_fetcher.py` and add a new method:
```python
def fetch_your_source(self):
    # Your scraping logic
    pass
```

### Modify Templates
Edit `templates/carousel_template.html` - CSS is inline and well-commented.

### Change Watermark
Edit `run.py`, line 48:
```python
generator = CarouselGenerator(watermark="your.handle")
```

## File Structure

```
ai-news-automation/
├── scraper/
│   └── news_fetcher.py      # News scraping logic
├── templates/
│   └── carousel_template.html # HTML/CSS templates
├── generator/
│   └── carousel_generator.py  # Image generation
├── output/                   # Generated carousels
├── run.py                    # Main runner
├── run.bat                   # Windows quick launcher
└── requirements.txt          # Python dependencies
```

## Automation (Optional)

### Windows Task Scheduler
1. Open Task Scheduler
2. Create Basic Task → Daily
3. Action: Start a program
4. Program: `python.exe`
5. Arguments: `C:\path\to\run.py`

### macOS/Linux Cron
```bash
# Run daily at 8 AM
0 8 * * * cd /path/to/ai-news-automation && python run.py
```

## Troubleshooting

### Playwright not found
```bash
playwright install chromium
```

### News not fetching
- Check internet connection
- Some sites may block scraping (script handles gracefully)
- Reddit may rate-limit (add delay if needed)

### Images look wrong
- Ensure you have a 1080p+ display
- Playwright renders at 1080x1350 (Instagram 4:5)

## News Sources

- **TechCrunch AI** - Breaking AI startup news
- **The Verge AI** - Consumer tech angle
- **Ars Technica** - Technical deep-dives
- **Reddit r/artificial** - Community trending topics

## License

MIT - Use freely for your own content creation.

---

Built for **@auraman.ai** 🚀
