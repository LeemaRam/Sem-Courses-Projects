#!/usr/bin/env python3
"""
Pre-Deployment Verification Script
Tests if the app is ready for Hugging Face Spaces deployment
"""

import sys
import os
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if Path(filepath).exists():
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description} MISSING: {filepath}")
        return False

def check_readme_yaml():
    """Check if README has HF Spaces YAML header"""
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("✗ README.md not found")
        return False
    
    with open(readme_path, 'r') as f:
        content = f.read()
        if content.startswith('---') and 'sdk: streamlit' in content:
            print("✓ README.md has HF Spaces YAML header")
            return True
        else:
            print("✗ README.md missing HF Spaces YAML header")
            return False

def check_requirements():
    """Check requirements.txt"""
    req_path = Path("requirements.txt")
    if not req_path.exists():
        print("✗ requirements.txt not found")
        return False
    
    with open(req_path, 'r') as f:
        content = f.read()
        required = ['streamlit', 'spacy', 'pdfplumber', 'python-docx', 'pandas']
        missing = [pkg for pkg in required if pkg not in content.lower()]
        
        if missing:
            print(f"✗ requirements.txt missing packages: {', '.join(missing)}")
            return False
        else:
            print("✓ requirements.txt has all required packages")
            return True

def check_imports():
    """Check if app.py imports work"""
    try:
        sys.path.insert(0, str(Path.cwd()))
        
        # Try importing main modules
        import streamlit
        print("✓ streamlit import successful")
        
        # Try importing utility modules
        from utils import text_extractor, preprocess, ner_extractor
        print("✓ utils modules import successful")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {str(e)}")
        return False

def main():
    """Run all checks"""
    print("=" * 60)
    print("HUGGING FACE SPACES DEPLOYMENT READINESS CHECK")
    print("=" * 60)
    print()
    
    checks = []
    
    # Check essential files
    print("Checking essential files...")
    checks.append(check_file_exists("app.py", "Main app file"))
    checks.append(check_file_exists("requirements.txt", "Requirements file"))
    checks.append(check_file_exists("README.md", "README file"))
    checks.append(check_file_exists(".streamlit/config.toml", "Streamlit config"))
    print()
    
    # Check utility modules
    print("Checking utility modules...")
    checks.append(check_file_exists("utils/__init__.py", "Utils package"))
    checks.append(check_file_exists("utils/text_extractor.py", "Text extractor"))
    checks.append(check_file_exists("utils/ner_extractor.py", "NER extractor"))
    checks.append(check_file_exists("utils/skill_extractor.py", "Skill extractor"))
    checks.append(check_file_exists("utils/regex_extractor.py", "Regex extractor"))
    checks.append(check_file_exists("utils/preprocess.py", "Preprocessor"))
    checks.append(check_file_exists("utils/output_formatter.py", "Output formatter"))
    print()
    
    # Check data files
    print("Checking data files...")
    checks.append(check_file_exists("data/skills_list.txt", "Skills database"))
    print()
    
    # Check README YAML
    print("Checking README.md...")
    checks.append(check_readme_yaml())
    print()
    
    # Check requirements
    print("Checking requirements.txt...")
    checks.append(check_requirements())
    print()
    
    # Check imports (optional, requires packages installed)
    print("Checking imports (optional)...")
    try:
        check_imports()
    except:
        print("⚠ Import check skipped (packages not installed)")
    print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(checks)
    total = len(checks)
    
    print(f"Checks passed: {passed}/{total}")
    
    if passed == total:
        print("\n✅ ALL CHECKS PASSED - READY FOR DEPLOYMENT!")
        print("\nNext steps:")
        print("1. Create a new Space on Hugging Face")
        print("2. Upload all files to the Space")
        print("3. Wait for build to complete")
        print("4. Test the deployed app")
        return 0
    else:
        print("\n❌ SOME CHECKS FAILED - PLEASE FIX ISSUES BEFORE DEPLOYMENT")
        print("\nSee DEPLOYMENT_GUIDE.md for more information")
        return 1

if __name__ == "__main__":
    sys.exit(main())
