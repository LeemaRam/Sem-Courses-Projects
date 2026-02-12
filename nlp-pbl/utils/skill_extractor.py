"""
Skill Extractor Module
Extracts skills and key phrases from resume text
"""

from typing import List, Set, Dict, Optional
import re
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SkillExtractor:
    """
    A class to extract skills from resume text.
    Uses keyword matching and phrase extraction.
    """
    
    def __init__(self, skills_file: Optional[str] = None):
        """
        Initialize the skill extractor.
        
        Args:
            skills_file (Optional[str]): Path to file containing list of skills
        """
        self.skills_set = set()
        
        if skills_file and os.path.exists(skills_file):
            self.load_skills_from_file(skills_file)
        else:
            self.load_default_skills()
        
        logger.info(f"Loaded {len(self.skills_set)} skills")
    
    def load_skills_from_file(self, file_path: str):
        """
        Load skills from a text file (one skill per line).
        
        Args:
            file_path (str): Path to skills file
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                skills = [line.strip().lower() for line in f if line.strip()]
                self.skills_set = set(skills)
            logger.info(f"Loaded skills from {file_path}")
        except Exception as e:
            logger.error(f"Error loading skills from file: {str(e)}")
            self.load_default_skills()
    
    def load_default_skills(self):
        """
        Load a default set of common technical and professional skills.
        """
        default_skills = [
            # Programming Languages
            'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'ruby', 'go',
            'rust', 'php', 'swift', 'kotlin', 'scala', 'r', 'matlab', 'perl',
            
            # Web Technologies
            'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'django',
            'flask', 'fastapi', 'spring', 'asp.net', 'jquery', 'bootstrap', 'tailwind',
            
            # Databases
            'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'cassandra', 'oracle',
            'sqlite', 'dynamodb', 'neo4j', 'elasticsearch',
            
            # Cloud & DevOps
            'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'gitlab',
            'github actions', 'terraform', 'ansible', 'ci/cd', 'devops',
            
            # Data Science & ML
            'machine learning', 'deep learning', 'nlp', 'computer vision', 'tensorflow',
            'pytorch', 'keras', 'scikit-learn', 'pandas', 'numpy', 'matplotlib',
            'data analysis', 'data visualization', 'statistics', 'big data', 'spark',
            
            # Tools & Technologies
            'git', 'linux', 'unix', 'bash', 'powershell', 'vim', 'vscode', 'jupyter',
            'api', 'rest', 'graphql', 'microservices', 'agile', 'scrum', 'jira',
            
            # Soft Skills
            'leadership', 'communication', 'teamwork', 'problem solving', 'analytical',
            'project management', 'critical thinking', 'time management',
            
            # Other Technical
            'testing', 'debugging', 'optimization', 'security', 'networking',
            'algorithms', 'data structures', 'oop', 'functional programming',
        ]
        
        self.skills_set = set(default_skills)
        logger.info("Loaded default skills set")
    
    def extract_skills(self, text: str) -> List[str]:
        """
        Extract skills from text using keyword matching.
        
        Args:
            text (str): Input text (resume)
            
        Returns:
            List[str]: List of identified skills
        """
        if not text:
            return []
        
        text_lower = text.lower()
        found_skills = []
        
        # Match skills from the skills set
        for skill in self.skills_set:
            # Use word boundaries for better matching
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.append(skill)
        
        # Remove duplicates and sort
        found_skills = sorted(list(set(found_skills)))
        
        logger.info(f"Extracted {len(found_skills)} skills")
        return found_skills
    
    def extract_skills_with_context(self, text: str) -> List[Dict[str, str]]:
        """
        Extract skills along with surrounding context.
        
        Args:
            text (str): Input text
            
        Returns:
            List[Dict[str, str]]: List of skills with context
        """
        if not text:
            return []
        
        text_lower = text.lower()
        skills_with_context = []
        
        for skill in self.skills_set:
            pattern = r'\b' + re.escape(skill) + r'\b'
            matches = re.finditer(pattern, text_lower)
            
            for match in matches:
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)
                context = text[start:end].strip()
                
                skills_with_context.append({
                    'skill': skill,
                    'context': context
                })
                break  # Only first occurrence
        
        return skills_with_context
    
    def categorize_skills(self, skills: List[str]) -> Dict[str, List[str]]:
        """
        Categorize extracted skills into groups.
        
        Args:
            skills (List[str]): List of skills
            
        Returns:
            Dict[str, List[str]]: Dictionary of categorized skills
        """
        categories = {
            'Programming Languages': [],
            'Web Technologies': [],
            'Databases': [],
            'Cloud & DevOps': [],
            'Data Science & ML': [],
            'Tools & Frameworks': [],
            'Soft Skills': [],
            'Other': []
        }
        
        # Define category keywords
        category_keywords = {
            'Programming Languages': ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'go', 'rust', 'php', 'swift', 'kotlin'],
            'Web Technologies': ['html', 'css', 'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'express'],
            'Databases': ['sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'oracle', 'sqlite'],
            'Cloud & DevOps': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'terraform', 'ci/cd'],
            'Data Science & ML': ['machine learning', 'deep learning', 'nlp', 'tensorflow', 'pytorch', 'pandas', 'numpy'],
            'Tools & Frameworks': ['git', 'linux', 'bash', 'api', 'rest', 'microservices'],
            'Soft Skills': ['leadership', 'communication', 'teamwork', 'problem solving', 'analytical'],
        }
        
        for skill in skills:
            categorized = False
            for category, keywords in category_keywords.items():
                if skill.lower() in keywords:
                    categories[category].append(skill)
                    categorized = True
                    break
            
            if not categorized:
                categories['Other'].append(skill)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}


def extract_skills_from_resume(text: str, skills_file: Optional[str] = None) -> List[str]:
    """
    Convenience function to extract skills from resume text.
    
    Args:
        text (str): Resume text
        skills_file (Optional[str]): Path to skills file
        
    Returns:
        List[str]: List of extracted skills
    """
    extractor = SkillExtractor(skills_file)
    return extractor.extract_skills(text)
