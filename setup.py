#!/usr/bin/env python3
"""
Setup script for AI News Carousel Automation
"""
import subprocess
import sys


def run_command(cmd, description):
    """Run a command and show progress"""
    print(f"  [>] {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"     [OK] Done")
            return True
        else:
            print(f"     [ERR] Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"     [ERR] Error: {e}")
        return False


def main():
    print("=" * 60)
    print("AI News Carousel Automation - Setup")
    print("=" * 60)
    print()

    steps = [
        ("pip install -r requirements.txt", "Installing Python packages"),
        ("playwright install chromium", "Installing Playwright browser"),
    ]

    success = True
    for cmd, desc in steps:
        if not run_command(cmd, desc):
            success = False

    print()
    print("=" * 60)

    if success:
        print("[OK] Setup complete!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("  1. Run: python preview_templates.py")
        print("     (See sample carousels without scraping)")
        print()
        print("  2. Run: python run.py")
        print("     (Full automation with live news)")
        print()
        print("  Or double-click run.bat for Windows")
    else:
        print("[!] Setup incomplete")
        print("=" * 60)
        print()
        print("Please install manually:")
        print("  pip install -r requirements.txt")
        print("  playwright install chromium")

    print()


if __name__ == "__main__":
    main()
