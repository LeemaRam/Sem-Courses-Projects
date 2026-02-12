"""
Output Formatter Module
Formats extracted resume data for display and export
"""

import json
from typing import Dict, List, Any
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OutputFormatter:
    """
    A class to format extracted resume data for various output formats.
    """
    
    @staticmethod
    def format_as_dict(extracted_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format extracted data as a clean dictionary.
        
        Args:
            extracted_data (Dict[str, Any]): Raw extracted data
            
        Returns:
            Dict[str, Any]: Formatted dictionary
        """
        formatted = {
            'name': extracted_data.get('name', 'Not found'),
            'contact': {
                'email': ', '.join(extracted_data.get('emails', [])) or 'Not found',
                'phone': ', '.join(extracted_data.get('phone_numbers', [])) or 'Not found',
                'linkedin': extracted_data.get('linkedin', 'Not found'),
                'github': extracted_data.get('github', 'Not found'),
            },
            'education': extracted_data.get('education', []),
            'experience': extracted_data.get('experience', []),
            'skills': extracted_data.get('skills', []),
            'extracted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return formatted
    
    @staticmethod
    def format_as_dataframe(extracted_data: Dict[str, Any]) -> pd.DataFrame:
        """
        Format extracted data as a pandas DataFrame for display.
        
        Args:
            extracted_data (Dict[str, Any]): Extracted data
            
        Returns:
            pd.DataFrame: Formatted DataFrame
        """
        # Create a list of key-value pairs for display
        data = []
        
        # Basic information
        data.append({'Field': 'Name', 'Value': extracted_data.get('name', 'Not found')})
        
        # Contact information
        emails = extracted_data.get('emails', [])
        data.append({'Field': 'Email', 'Value': ', '.join(emails) if emails else 'Not found'})
        
        phone_numbers = extracted_data.get('phone_numbers', [])
        data.append({'Field': 'Phone', 'Value': ', '.join(phone_numbers) if phone_numbers else 'Not found'})
        
        linkedin = extracted_data.get('linkedin')
        if linkedin:
            data.append({'Field': 'LinkedIn', 'Value': linkedin})
        
        github = extracted_data.get('github')
        if github:
            data.append({'Field': 'GitHub', 'Value': github})
        
        # Education
        education = extracted_data.get('education', [])
        if education:
            for i, edu in enumerate(education, 1):
                if isinstance(edu, dict):
                    edu_str = f"{edu.get('degree', 'N/A')} - {edu.get('institution', 'N/A')} ({edu.get('year', 'N/A')})"
                else:
                    edu_str = str(edu)
                data.append({'Field': f'Education {i}', 'Value': edu_str})
        else:
            data.append({'Field': 'Education', 'Value': 'Not found'})
        
        # Experience
        experience = extracted_data.get('experience', [])
        if experience:
            for i, exp in enumerate(experience, 1):
                if isinstance(exp, dict):
                    exp_str = f"{exp.get('company', 'N/A')} - {exp.get('duration', 'N/A')}"
                else:
                    exp_str = str(exp)
                data.append({'Field': f'Experience {i}', 'Value': exp_str})
        else:
            data.append({'Field': 'Experience', 'Value': 'Not found'})
        
        # Skills
        skills = extracted_data.get('skills', [])
        if skills:
            # Group skills for better display (max 10 per row)
            skill_groups = [skills[i:i+10] for i in range(0, len(skills), 10)]
            for i, group in enumerate(skill_groups, 1):
                data.append({'Field': f'Skills ({i})' if len(skill_groups) > 1 else 'Skills', 
                           'Value': ', '.join(group)})
        else:
            data.append({'Field': 'Skills', 'Value': 'Not found'})
        
        df = pd.DataFrame(data)
        logger.info("Formatted data as DataFrame")
        return df
    
    @staticmethod
    def format_as_json(extracted_data: Dict[str, Any], pretty: bool = True) -> str:
        """
        Format extracted data as JSON string.
        
        Args:
            extracted_data (Dict[str, Any]): Extracted data
            pretty (bool): Whether to format with indentation
            
        Returns:
            str: JSON string
        """
        formatted = OutputFormatter.format_as_dict(extracted_data)
        
        if pretty:
            json_str = json.dumps(formatted, indent=2, ensure_ascii=False)
        else:
            json_str = json.dumps(formatted, ensure_ascii=False)
        
        logger.info("Formatted data as JSON")
        return json_str
    
    @staticmethod
    def format_as_html(extracted_data: Dict[str, Any]) -> str:
        """
        Format extracted data as HTML for display.
        
        Args:
            extracted_data (Dict[str, Any]): Extracted data
            
        Returns:
            str: HTML string
        """
        html = "<div style='font-family: Arial, sans-serif;'>"
        
        # Name
        name = extracted_data.get('name', 'Not found')
        html += f"<h2>{name}</h2>"
        
        # Contact
        html += "<h3>Contact Information</h3><ul>"
        emails = extracted_data.get('emails', [])
        if emails:
            html += f"<li><strong>Email:</strong> {', '.join(emails)}</li>"
        
        phones = extracted_data.get('phone_numbers', [])
        if phones:
            html += f"<li><strong>Phone:</strong> {', '.join(phones)}</li>"
        
        linkedin = extracted_data.get('linkedin')
        if linkedin:
            html += f"<li><strong>LinkedIn:</strong> <a href='{linkedin}'>{linkedin}</a></li>"
        
        github = extracted_data.get('github')
        if github:
            html += f"<li><strong>GitHub:</strong> <a href='{github}'>{github}</a></li>"
        
        html += "</ul>"
        
        # Education
        education = extracted_data.get('education', [])
        if education:
            html += "<h3>Education</h3><ul>"
            for edu in education:
                if isinstance(edu, dict):
                    html += f"<li>{edu.get('degree', 'N/A')} - {edu.get('institution', 'N/A')} ({edu.get('year', 'N/A')})</li>"
                else:
                    html += f"<li>{edu}</li>"
            html += "</ul>"
        
        # Experience
        experience = extracted_data.get('experience', [])
        if experience:
            html += "<h3>Experience</h3><ul>"
            for exp in experience:
                if isinstance(exp, dict):
                    html += f"<li>{exp.get('company', 'N/A')} - {exp.get('duration', 'N/A')}</li>"
                else:
                    html += f"<li>{exp}</li>"
            html += "</ul>"
        
        # Skills
        skills = extracted_data.get('skills', [])
        if skills:
            html += "<h3>Skills</h3>"
            html += "<div style='display: flex; flex-wrap: wrap; gap: 8px;'>"
            for skill in skills:
                html += f"<span style='background-color: #e0e0e0; padding: 4px 8px; border-radius: 4px;'>{skill}</span>"
            html += "</div>"
        
        html += "</div>"
        
        logger.info("Formatted data as HTML")
        return html
    
    @staticmethod
    def highlight_entities(text: str, entities: List[Dict]) -> str:
        """
        Highlight entities in text using HTML.
        
        Args:
            text (str): Original text
            entities (List[Dict]): List of entities with start/end positions
            
        Returns:
            str: HTML string with highlighted entities
        """
        if not entities:
            return text
        
        # Sort entities by start position
        sorted_entities = sorted(entities, key=lambda x: x['start'])
        
        highlighted = ""
        last_end = 0
        
        # Color map for entity types
        color_map = {
            'PERSON': '#FFB6C1',
            'ORG': '#87CEEB',
            'DATE': '#90EE90',
            'GPE': '#FFD700',
            'MONEY': '#FFA07A',
            'EMAIL': '#DDA0DD',
            'PHONE': '#F0E68C',
        }
        
        for entity in sorted_entities:
            # Add text before entity
            highlighted += text[last_end:entity['start']]
            
            # Add highlighted entity
            color = color_map.get(entity['label'], '#D3D3D3')
            highlighted += f"<mark style='background-color: {color}; padding: 2px 4px; border-radius: 3px;'>"
            highlighted += f"{entity['text']} <sub style='font-size: 0.7em;'>({entity['label']})</sub>"
            highlighted += "</mark>"
            
            last_end = entity['end']
        
        # Add remaining text
        highlighted += text[last_end:]
        
        return highlighted


def format_resume_data(extracted_data: Dict[str, Any], format_type: str = 'dict') -> Any:
    """
    Convenience function to format resume data.
    
    Args:
        extracted_data (Dict[str, Any]): Extracted data
        format_type (str): Output format ('dict', 'json', 'dataframe', 'html')
        
    Returns:
        Any: Formatted data in specified format
    """
    formatter = OutputFormatter()
    
    if format_type == 'dict':
        return formatter.format_as_dict(extracted_data)
    elif format_type == 'json':
        return formatter.format_as_json(extracted_data)
    elif format_type == 'dataframe':
        return formatter.format_as_dataframe(extracted_data)
    elif format_type == 'html':
        return formatter.format_as_html(extracted_data)
    else:
        raise ValueError(f"Unsupported format type: {format_type}")
