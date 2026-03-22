#!/usr/bin/env python3
"""
Template Preview - Generate sample carousels to see all styles
"""
from generator.carousel_generator import CarouselGenerator
from datetime import datetime
import json


def main():
    print("Generating template previews...")
    print()

    generator = CarouselGenerator(watermark="auraman.ai")

    # Sample news items for each category
    samples = [
        {
            'title': 'OpenAI just dropped GPT-5 and it\'s actually mind-blowing',
            'source': 'TechCrunch',
            'category': 'model',
            'excerpt': 'The new model features 10x the parameters and can generate entire applications from a single prompt. Early testers are calling it the ChatGPT moment all over again.'
        },
        {
            'title': 'Midjourney V7 generates photorealistic video now',
            'source': 'The Verge',
            'category': 'image',
            'excerpt': 'The latest update brings motion to static images with incredible coherence. Artists are already using it for music videos.'
        },
        {
            'title': 'AI startup raises $500M at $4B valuation',
            'source': 'Ars Technica',
            'category': 'business',
            'excerpt': 'The company builds enterprise AI agents that can replace entire departments. Investors are betting big on the automation wave.'
        },
        {
            'title': 'EU passes new AI regulation framework',
            'source': 'Reddit r/artificial',
            'category': 'policy',
            'excerpt': 'The comprehensive bill sets strict guidelines for training data transparency and model evaluation standards.'
        },
        {
            'title': 'This new tool clones your voice in 10 seconds',
            'source': 'Product Hunt',
            'category': 'tool',
            'excerpt': 'Voice synthesis has never been this accessible. Just upload a 10-second sample and generate unlimited audio.'
        }
    ]

    print("Creating preview carousels for each template style...")
    print()

    for i, sample in enumerate(samples):
        print(f"  {i+1}. {sample['category'].upper()}: {sample['title'][:50]}...")
        files = generator.generate_carousel(sample, i)

    print()
    print("=" * 60)
    print("Preview carousels generated!")
    print("=" * 60)
    print()

    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = f"output/{today}"

    print(f"Check: {output_dir}/")
    print()
    print("Each carousel has:")
    print("  - Slide 1: Cover (branded intro)")
    print("  - Slide 2: News content (varies by template)")
    print("  - Slide 3: CTA (follow prompt)")
    print()
    print("Template styles used:")
    for sample in samples:
        print(f"  • {sample['category']}: {sample['title'][:40]}...")


if __name__ == "__main__":
    main()
