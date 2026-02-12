"""
Test Script for Smart Resume Parser
Run this to verify your installation is correct
"""

import sys
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    print("=" * 60)
    print("Testing Package Imports...")
    print("=" * 60)
    
    packages = {
        'streamlit': 'Streamlit',
        'spacy': 'spaCy',
        'pdfplumber': 'pdfplumber',
        'docx': 'python-docx',
        'pandas': 'pandas',
        'numpy': 'numpy',
    }
    
    failed = []
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}: OK")
        except ImportError as e:
            print(f"✗ {name}: FAILED - {str(e)}")
            failed.append(name)
    
    return len(failed) == 0


def test_spacy_model():
    """Test if spaCy model is installed"""
    print("\n" + "=" * 60)
    print("Testing spaCy Model...")
    print("=" * 60)
    
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        print("✓ spaCy model 'en_core_web_sm': OK")
        
        # Test basic NER
        doc = nlp("John Doe works at Google in New York.")
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        print(f"  Test entities found: {entities}")
        return True
        
    except Exception as e:
        print(f"✗ spaCy model: FAILED - {str(e)}")
        print("  Run: python -m spacy download en_core_web_sm")
        return False


def test_utils_modules():
    """Test if all utility modules can be imported"""
    print("\n" + "=" * 60)
    print("Testing Utility Modules...")
    print("=" * 60)
    
    modules = [
        'utils.text_extractor',
        'utils.preprocess',
        'utils.ner_extractor',
        'utils.skill_extractor',
        'utils.regex_extractor',
        'utils.output_formatter',
    ]
    
    failed = []
    for module in modules:
        try:
            __import__(module)
            print(f"✓ {module}: OK")
        except ImportError as e:
            print(f"✗ {module}: FAILED - {str(e)}")
            failed.append(module)
    
    return len(failed) == 0


def test_data_files():
    """Test if required data files exist"""
    print("\n" + "=" * 60)
    print("Testing Data Files...")
    print("=" * 60)
    
    files_to_check = [
        'data/skills_list.txt',
        'data/sample_resumes/sample_resume_john_doe.txt',
    ]
    
    all_exist = True
    for file_path in files_to_check:
        path = Path(file_path)
        if path.exists():
            print(f"✓ {file_path}: OK")
        else:
            print(f"✗ {file_path}: NOT FOUND")
            all_exist = False
    
    return all_exist


def test_basic_functionality():
    """Test basic extraction functionality"""
    print("\n" + "=" * 60)
    print("Testing Basic Functionality...")
    print("=" * 60)
    
    try:
        from utils.regex_extractor import RegexExtractor
        from utils.ner_extractor import NERExtractor
        from utils.skill_extractor import SkillExtractor
        
        # Test regex extraction
        print("\n1. Testing Email Extraction...")
        regex_extractor = RegexExtractor()
        test_text = "Contact me at john.doe@example.com or jane@test.org"
        emails = regex_extractor.extract_emails(test_text)
        print(f"   Found emails: {emails}")
        assert len(emails) >= 2, "Should find at least 2 emails"
        print("   ✓ Email extraction working")
        
        # Test phone extraction
        print("\n2. Testing Phone Extraction...")
        test_text = "Call me at +1-234-567-8900 or (555) 123-4567"
        phones = regex_extractor.extract_phone_numbers(test_text)
        print(f"   Found phones: {phones}")
        print("   ✓ Phone extraction working")
        
        # Test NER
        print("\n3. Testing Named Entity Recognition...")
        ner_extractor = NERExtractor()
        test_text = "John Doe works at Google in New York since 2020."
        entities = ner_extractor.extract_entities(test_text)
        print(f"   Found {len(entities)} entities")
        for ent in entities:
            print(f"   - {ent['text']}: {ent['label']}")
        print("   ✓ NER working")
        
        # Test skill extraction
        print("\n4. Testing Skill Extraction...")
        skills_file = Path('data/skills_list.txt')
        skill_extractor = SkillExtractor(str(skills_file) if skills_file.exists() else None)
        test_text = "Experienced with Python, Java, Machine Learning, and Docker"
        skills = skill_extractor.extract_skills(test_text)
        print(f"   Found skills: {skills}")
        assert len(skills) > 0, "Should find at least some skills"
        print("   ✓ Skill extraction working")
        
        return True
        
    except Exception as e:
        print(f"\n✗ Functionality test FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("SMART RESUME PARSER - INSTALLATION TEST")
    print("=" * 60)
    
    results = {
        'Imports': test_imports(),
        'spaCy Model': test_spacy_model(),
        'Utility Modules': test_utils_modules(),
        'Data Files': test_data_files(),
        'Basic Functionality': test_basic_functionality(),
    }
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ ALL TESTS PASSED!")
        print("Your installation is ready to use.")
        print("\nRun the application with:")
        print("  streamlit run app.py")
    else:
        print("✗ SOME TESTS FAILED")
        print("Please fix the issues above before running the application.")
        print("\nCommon fixes:")
        print("  - Install missing packages: pip install -r requirements.txt")
        print("  - Download spaCy model: python -m spacy download en_core_web_sm")
        print("  - Ensure you're in the correct directory")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
