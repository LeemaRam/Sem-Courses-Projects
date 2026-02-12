"""
Named Entity Recognition (NER) Extractor Module
Extracts named entities using spaCy
"""

import spacy
from typing import List, Dict, Optional, Tuple
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NERExtractor:
    """
    A class to extract named entities from text using spaCy.
    Identifies names, organizations, dates, and other entities.
    """
    
    def __init__(self, model_name: str = "en_core_web_sm"):
        """
        Initialize the NER extractor with a spaCy model.
        
        Args:
            model_name (str): Name of the spaCy model to use
        """
        try:
            self.nlp = spacy.load(model_name)
            logger.info(f"Loaded spaCy model: {model_name}")
        except OSError:
            logger.warning(f"Model {model_name} not found. Attempting to download...")
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", model_name])
            self.nlp = spacy.load(model_name)
            logger.info(f"Downloaded and loaded spaCy model: {model_name}")
    
    def extract_entities(self, text: str) -> List[Dict[str, str]]:
        """
        Extract all named entities from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[Dict[str, str]]: List of entities with text, label, and position
        """
        if not text:
            return []
        
        doc = self.nlp(text)
        entities = []
        
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            })
        
        logger.info(f"Extracted {len(entities)} entities")
        return entities
    
    def extract_person_names(self, text: str) -> List[str]:
        """
        Extract person names from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of person names
        """
        if not text:
            return []
        
        doc = self.nlp(text)
        names = []
        
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                names.append(ent.text)
        
        # Take the first few lines to find the candidate name (usually at the top)
        lines = text.split('\n')[:5]
        top_text = ' '.join(lines)
        doc_top = self.nlp(top_text)
        
        top_names = [ent.text for ent in doc_top.ents if ent.label_ == "PERSON"]
        
        # Prioritize names from the top of the document
        if top_names:
            # Remove duplicates while preserving order
            all_names = top_names + [n for n in names if n not in top_names]
            return list(dict.fromkeys(all_names))  # Remove duplicates
        
        return list(dict.fromkeys(names))  # Remove duplicates
    
    def extract_organizations(self, text: str) -> List[str]:
        """
        Extract organization names from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of organization names
        """
        if not text:
            return []
        
        doc = self.nlp(text)
        orgs = []
        
        for ent in doc.ents:
            if ent.label_ == "ORG":
                orgs.append(ent.text)
        
        return list(dict.fromkeys(orgs))  # Remove duplicates
    
    def extract_dates(self, text: str) -> List[str]:
        """
        Extract dates from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of dates
        """
        if not text:
            return []
        
        doc = self.nlp(text)
        dates = []
        
        for ent in doc.ents:
            if ent.label_ == "DATE":
                dates.append(ent.text)
        
        return dates
    
    def extract_education(self, text: str) -> List[Dict[str, str]]:
        """
        Extract education information from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[Dict[str, str]]: List of education entries
        """
        education_keywords = [
            'bachelor', 'master', 'phd', 'doctorate', 'diploma', 'degree',
            'b.tech', 'b.e', 'm.tech', 'm.e', 'mba', 'bba', 'bca', 'mca',
            'b.sc', 'm.sc', 'b.a', 'm.a', 'llb', 'md', 'mbbs'
        ]
        
        education_entries = []
        lines = text.lower().split('\n')
        
        for i, line in enumerate(lines):
            if any(keyword in line for keyword in education_keywords):
                # Extract the education entry (current line and possibly next line)
                entry = lines[i]
                if i + 1 < len(lines):
                    entry += ' ' + lines[i + 1]
                
                # Extract degree and institution using NER
                doc = self.nlp(entry)
                orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
                dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
                
                education_entries.append({
                    'degree': line.strip(),
                    'institution': orgs[0] if orgs else 'Not specified',
                    'year': dates[0] if dates else 'Not specified'
                })
        
        return education_entries
    
    def extract_experience(self, text: str) -> List[Dict[str, str]]:
        """
        Extract work experience information from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[Dict[str, str]]: List of experience entries
        """
        # Look for experience section
        exp_pattern = r'(?i)(experience|employment|work history)'
        
        # Split text into sections
        sections = re.split(exp_pattern, text)
        
        if len(sections) < 2:
            return []
        
        # Take the section after "experience" keyword
        exp_text = sections[-1]
        
        doc = self.nlp(exp_text)
        
        # Extract organizations and dates
        orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
        
        experiences = []
        for i, org in enumerate(orgs[:5]):  # Limit to 5 most recent
            experiences.append({
                'company': org,
                'duration': dates[i] if i < len(dates) else 'Not specified',
            })
        
        return experiences
    
    def get_resume_name(self, text: str) -> Optional[str]:
        """
        Extract the most likely candidate name from resume.
        Usually the name appears at the top of the resume.
        
        Args:
            text (str): Resume text
            
        Returns:
            Optional[str]: Candidate name or None
        """
        # Take first few lines
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            return None
        
        # Process first 3 lines to find name
        top_text = ' '.join(lines[:3])
        doc = self.nlp(top_text)
        
        # Find PERSON entities in the first line first
        first_line_doc = self.nlp(lines[0])
        person_in_first_line = [ent.text for ent in first_line_doc.ents if ent.label_ == "PERSON"]
        
        if person_in_first_line:
            return person_in_first_line[0]
        
        # Otherwise, find any PERSON entity in top 3 lines
        persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        
        if persons:
            return persons[0]
        
        # Fallback: if first line looks like a name (2-4 words, capitalized)
        first_line_words = lines[0].split()
        if 2 <= len(first_line_words) <= 4 and all(word[0].isupper() for word in first_line_words if word):
            return lines[0]
        
        return None


def extract_entities_from_resume(text: str, model_name: str = "en_core_web_sm") -> Dict:
    """
    Convenience function to extract all entities from a resume.
    
    Args:
        text (str): Resume text
        model_name (str): spaCy model name
        
    Returns:
        Dict: Dictionary containing all extracted entities
    """
    extractor = NERExtractor(model_name)
    
    return {
        'name': extractor.get_resume_name(text),
        'organizations': extractor.extract_organizations(text),
        'education': extractor.extract_education(text),
        'experience': extractor.extract_experience(text),
        'dates': extractor.extract_dates(text),
    }
