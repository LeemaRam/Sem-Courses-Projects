"""
Regex Extractor Module
Extracts specific information using regular expressions
"""

import re
from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RegexExtractor:
    """
    A class to extract specific information using regex patterns.
    Handles email addresses, phone numbers, and other structured data.
    """
    
    # Regex patterns
    EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Phone patterns for various formats
    PHONE_PATTERNS = [
        r'\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # +1-234-567-8900
        r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # (234) 567-8900
        r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',  # 234-567-8900
        r'\+?\d{10,14}',  # 12345678900
    ]
    
    URL_PATTERN = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """
        Extract email addresses from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of unique email addresses found
        """
        if not text:
            return []
        
        emails = re.findall(RegexExtractor.EMAIL_PATTERN, text)
        # Remove duplicates while preserving order
        seen = set()
        unique_emails = []
        for email in emails:
            email_lower = email.lower()
            if email_lower not in seen:
                seen.add(email_lower)
                unique_emails.append(email)
        
        logger.info(f"Extracted {len(unique_emails)} unique email(s)")
        return unique_emails
    
    @staticmethod
    def extract_phone_numbers(text: str) -> List[str]:
        """
        Extract phone numbers from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of unique phone numbers found
        """
        if not text:
            return []
        
        phone_numbers = []
        
        for pattern in RegexExtractor.PHONE_PATTERNS:
            matches = re.findall(pattern, text)
            phone_numbers.extend(matches)
        
        # Clean and normalize phone numbers
        cleaned_numbers = []
        for number in phone_numbers:
            # Remove common separators and keep only digits and +
            cleaned = re.sub(r'[^\d+]', '', number)
            if len(cleaned) >= 10:  # Valid phone number should have at least 10 digits
                cleaned_numbers.append(number)  # Keep original format
        
        # Remove duplicates
        seen = set()
        unique_numbers = []
        for number in cleaned_numbers:
            normalized = re.sub(r'[^\d]', '', number)
            if normalized not in seen and len(normalized) >= 10:
                seen.add(normalized)
                unique_numbers.append(number)
        
        logger.info(f"Extracted {len(unique_numbers)} unique phone number(s)")
        return unique_numbers
    
    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """
        Extract URLs from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of unique URLs found
        """
        if not text:
            return []
        
        urls = re.findall(RegexExtractor.URL_PATTERN, text)
        # Remove duplicates
        unique_urls = list(set(urls))
        
        logger.info(f"Extracted {len(unique_urls)} unique URL(s)")
        return unique_urls
    
    @staticmethod
    def extract_linkedin_url(text: str) -> Optional[str]:
        """
        Extract LinkedIn profile URL from text.
        
        Args:
            text (str): Input text
            
        Returns:
            Optional[str]: LinkedIn URL or None if not found
        """
        linkedin_pattern = r'(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+'
        match = re.search(linkedin_pattern, text)
        return match.group(0) if match else None
    
    @staticmethod
    def extract_github_url(text: str) -> Optional[str]:
        """
        Extract GitHub profile URL from text.
        
        Args:
            text (str): Input text
            
        Returns:
            Optional[str]: GitHub URL or None if not found
        """
        github_pattern = r'(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+'
        match = re.search(github_pattern, text)
        return match.group(0) if match else None
    
    @staticmethod
    def extract_years_of_experience(text: str) -> Optional[int]:
        """
        Extract years of experience from text.
        
        Args:
            text (str): Input text
            
        Returns:
            Optional[int]: Years of experience or None if not found
        """
        patterns = [
            r'(\d+)\+?\s*years?\s+(?:of\s+)?experience',
            r'experience[:\s]+(\d+)\+?\s*years?',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        return None


def extract_contact_info(text: str) -> dict:
    """
    Convenience function to extract all contact information.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary containing emails, phone numbers, and URLs
    """
    return {
        'emails': RegexExtractor.extract_emails(text),
        'phone_numbers': RegexExtractor.extract_phone_numbers(text),
        'linkedin': RegexExtractor.extract_linkedin_url(text),
        'github': RegexExtractor.extract_github_url(text),
    }
