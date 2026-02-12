"""
Text Preprocessing Module
Cleans and normalizes extracted text for NLP processing
"""

import re
from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextPreprocessor:
    """
    A class to preprocess and clean text extracted from resumes.
    """
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize text.
        
        Args:
            text (str): Raw text to clean
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
        
        # Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep meaningful punctuation
        text = re.sub(r'[^\w\s@.+\-(),:/]', '', text)
        
        # Normalize line breaks
        text = text.replace('\r\n', '\n').replace('\r', '\n')
        
        # Remove multiple newlines
        text = re.sub(r'\n+', '\n', text)
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text
    
    @staticmethod
    def remove_urls(text: str) -> str:
        """
        Remove URLs from text.
        
        Args:
            text (str): Input text
            
        Returns:
            str: Text with URLs removed
        """
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.sub(url_pattern, '', text)
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """
        Normalize whitespace in text.
        
        Args:
            text (str): Input text
            
        Returns:
            str: Text with normalized whitespace
        """
        return ' '.join(text.split())
    
    @staticmethod
    def split_into_sections(text: str) -> dict:
        """
        Split resume text into logical sections.
        
        Args:
            text (str): Resume text
            
        Returns:
            dict: Dictionary with section names as keys and content as values
        """
        sections = {}
        
        # Common section headers in resumes
        section_patterns = {
            'education': r'(?i)(education|academic|qualification|degree)',
            'experience': r'(?i)(experience|employment|work history|professional experience)',
            'skills': r'(?i)(skills|technical skills|competencies|expertise)',
            'projects': r'(?i)(projects|portfolio)',
            'certifications': r'(?i)(certifications?|licenses?)',
            'summary': r'(?i)(summary|objective|profile)'
        }
        
        lines = text.split('\n')
        current_section = 'header'
        sections[current_section] = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check if line is a section header
            is_header = False
            for section_name, pattern in section_patterns.items():
                if re.match(pattern, line) and len(line) < 50:
                    current_section = section_name
                    sections[current_section] = []
                    is_header = True
                    break
            
            if not is_header:
                if current_section not in sections:
                    sections[current_section] = []
                sections[current_section].append(line)
        
        # Join lines in each section
        for key in sections:
            sections[key] = '\n'.join(sections[key])
        
        return sections
    
    @staticmethod
    def preprocess(text: str, remove_urls_flag: bool = True) -> str:
        """
        Apply full preprocessing pipeline to text.
        
        Args:
            text (str): Raw text to preprocess
            remove_urls_flag (bool): Whether to remove URLs
            
        Returns:
            str: Preprocessed text
        """
        if not text:
            logger.warning("Empty text provided for preprocessing")
            return ""
        
        # Clean text
        text = TextPreprocessor.clean_text(text)
        
        # Remove URLs if requested
        if remove_urls_flag:
            text = TextPreprocessor.remove_urls(text)
        
        # Normalize whitespace
        text = TextPreprocessor.normalize_whitespace(text)
        
        logger.info("Text preprocessing completed")
        return text


def preprocess_text(text: str, remove_urls: bool = True) -> str:
    """
    Convenience function to preprocess text.
    
    Args:
        text (str): Raw text to preprocess
        remove_urls (bool): Whether to remove URLs
        
    Returns:
        str: Preprocessed text
    """
    return TextPreprocessor.preprocess(text, remove_urls)
