#!/usr/bin/env python3
"""
AI News Carousel Automation - Main Runner
Run this daily to generate your Instagram carousels
"""
import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from scraper.news_fetcher import AINewsFetcher
from generator.carousel_generator import CarouselGenerator
import json
from datetime import datetime


def main():
    print("=" * 60)
    print("AI NEWS CAROUSEL AUTOMATION")
    print("@auraman.ai")
    print("=" * 60)
    print()

    # Step 1: Fetch news
    print("Step 1: Fetching latest AI news...")
    fetcher = AINewsFetcher()
    news = fetcher.get_trending_news(limit=5)
    print(f"   [OK] Fetched {len(news)} news items")
    print()

    # Save news
    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = Path(__file__).parent / "output" / today
    output_dir.mkdir(parents=True, exist_ok=True)

    news_file = output_dir / "news.json"
    with open(news_file, 'w', encoding='utf-8') as f:
        json.dump(news, f, indent=2, ensure_ascii=False)
    print(f"   [OK] Saved news to {news_file}")
    print()

    # Step 2: Generate carousels
    print("Step 2: Generating carousels...")
    generator = CarouselGenerator(watermark="auraman.ai")

    all_carousels = []
    for i, item in enumerate(news):
        print(f"   Creating carousel {i+1}/5...")
        files = generator.generate_carousel(item, i)
        all_carousels.append({
            'news': item,
            'files': files
        })
    print(f"   [OK] Generated {len(all_carousels)} carousels")
    print()

    # Step 3: Generate captions
    print("Step 3: Creating captions...")
    captions = generator.generate_captions(all_carousels)

    captions_file = output_dir / "captions.txt"
    with open(captions_file, 'w', encoding='utf-8') as f:
        for i, cap in enumerate(captions, 1):
            f.write(f"\n{'='*60}\n")
            f.write(f"CAROUSEL {i}: {cap['title']}\n")
            f.write(f"{'='*60}\n\n")
            f.write(cap['caption'])
            f.write("\n\n")
            f.write(f"Images: {', '.join(cap['files'])}\n")

    print(f"   [OK] Saved captions to {captions_file}")
    print()

    # Summary
    print("=" * 60)
    print("ALL DONE!")
    print("=" * 60)
    print()
    print(f"Output location: {output_dir}")
    print()
    print("Your carousels are ready!")
    print()
    print("Next steps:")
    print("  1. Open the output folder above")
    print("  2. Review the generated carousel images")
    print("  3. Copy the caption from captions.txt")
    print("  4. Upload to Instagram manually")
    print()
    print("News summary:")
    for i, item in enumerate(news, 1):
        print(f"  {i}. [{item['category'].upper()}] {item['title'][:60]}...")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n[X] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
