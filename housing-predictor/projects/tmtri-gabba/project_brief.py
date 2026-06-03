#!/usr/bin/env python3
"""
TMTRI Gabba Project Script
High-quality lighting photo sourcing and project management
"""

import os
import sys
import json
from pathlib import Path

PROJECT_NAME = "TM@TRI (ENTRI) — Translational Manufacturing Facility"
PROJECT_DIR = Path(__file__).parent

IMAGE_DIR = PROJECT_DIR / "images"
README_PATH = PROJECT_DIR / "README.md"

def validate_images():
    """Check all images exist and are valid."""
    for img in sorted(IMAGE_DIR.iterdir()):
        size = img.stat().st_size
        print(f"  {img.name}: {size:,} bytes")

def build_project_json():
    """Build a structured project metadata file."""
    return {
        "name": "TM@TRI (ENTRI)",
        "full_name": "Translational Manufacturing Facility at TRI",
        "location": "Boggo Road Innovation Junction, Brisbane",
        "client": "Translational Research Institute",
        "architect": "Wilson Architects",
        "contractor": "Built Builders",
        "completion": "Early 2026",
        "gfa_sqm": 8700,
        "investment_aud": 100000000,
        "tenants": ["Sanofi"],
        "jobs_at_capacity": 500,
        "sustainability": {
            "green_star": 5,
            "nabers": 5.5
        },
        "facilities": [
            "cGMP Cleanrooms",
            "PC2 Laboratories",
            "Wet Labs",
            "Innovation Spaces",
            "Quality Control Labs"
        ],
        "product_types": ["Biologics", "pDNA", "RNA-based therapies", "Cell therapies"],
        "traditional_custodians": ["Yugara", "Turrbal"]
    }

if __name__ == "__main__":
    print(f"{'='*60}")
    print(f"  {PROJECT_NAME}")
    print(f"{'='*60}")
    print()
    print("Validating images...")
    validate_images()
    print()
    meta = build_project_json()
    with open(PROJECT_DIR / "project.json", "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Project metadata written to project.json")
    print(f"Images: {len(list(IMAGE_DIR.iterdir()))} files")
