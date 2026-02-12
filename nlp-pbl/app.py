"""
Smart Resume Parser & Skill Extraction System
Main Streamlit Application

This application allows users to upload resumes (PDF or DOCX) and automatically
extracts structured information using NLP techniques.
"""

import streamlit as st
import tempfile
import os
from pathlib import Path
import sys

# Add utils to path
sys.path.append(str(Path(__file__).parent))

from utils.text_extractor import TextExtractor
from utils.preprocess import TextPreprocessor
from utils.regex_extractor import RegexExtractor
from utils.ner_extractor import NERExtractor
from utils.skill_extractor import SkillExtractor
from utils.output_formatter import OutputFormatter


# Page configuration
st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #1E88E5;
        margin-bottom: 1rem;
    }
    .skill-tag {
        background-color: #E8F5E9;
        padding: 0.3rem 0.6rem;
        border-radius: 3px;
        margin: 0.2rem;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)


# Cache model loading for better performance
@st.cache_resource
def load_ner_model():
    """Load and cache NER model"""
    return NERExtractor()

@st.cache_resource
def load_skill_extractor():
    """Load and cache skill extractor"""
    skills_file = Path(__file__).parent / 'data' / 'skills_list.txt'
    return SkillExtractor(str(skills_file) if skills_file.exists() else None)


class ResumeParserApp:
    """Main Resume Parser Application Class"""
    
    def __init__(self):
        """Initialize the application with necessary components"""
        self.text_extractor = TextExtractor()
        self.preprocessor = TextPreprocessor()
        self.regex_extractor = RegexExtractor()
        
        # Load models using cached functions
        try:
            self.ner_extractor = load_ner_model()
            self.skill_extractor = load_skill_extractor()
        except Exception as e:
            st.error(f"Error loading models: {str(e)}")
            st.info("The app may not function properly. Please refresh the page.")
            raise
        
        self.formatter = OutputFormatter()
    
    def extract_resume_data(self, text: str) -> dict:
        """
        Extract all information from resume text.
        
        Args:
            text (str): Resume text
            
        Returns:
            dict: Extracted information
        """
        # Preprocess text
        cleaned_text = self.preprocessor.preprocess(text, remove_urls_flag=False)
        
        # Extract contact information using regex
        emails = self.regex_extractor.extract_emails(text)
        phone_numbers = self.regex_extractor.extract_phone_numbers(text)
        linkedin = self.regex_extractor.extract_linkedin_url(text)
        github = self.regex_extractor.extract_github_url(text)
        
        # Extract entities using NER
        name = self.ner_extractor.get_resume_name(text)
        organizations = self.ner_extractor.extract_organizations(text)
        education = self.ner_extractor.extract_education(text)
        experience = self.ner_extractor.extract_experience(text)
        all_entities = self.ner_extractor.extract_entities(text)
        
        # Extract skills
        skills = self.skill_extractor.extract_skills(text)
        
        # Compile all extracted data
        extracted_data = {
            'name': name,
            'emails': emails,
            'phone_numbers': phone_numbers,
            'linkedin': linkedin,
            'github': github,
            'organizations': organizations,
            'education': education,
            'experience': experience,
            'skills': skills,
            'entities': all_entities,
            'raw_text': text,
            'cleaned_text': cleaned_text
        }
        
        return extracted_data
    
    def render_header(self):
        """Render the application header"""
        st.markdown('<p class="main-header">📄 Smart Resume Parser & Skill Extraction System</p>', 
                   unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Upload a resume to automatically extract structured information using NLP</p>', 
                   unsafe_allow_html=True)
    
    def render_sidebar(self):
        """Render the sidebar with information and options"""
        with st.sidebar:
            st.title("📄 About")
            st.markdown("""
            This application uses advanced NLP techniques to extract:
            
            - 👤 **Name** (using NER)
            - 📧 **Email** (using Regex)
            - 📱 **Phone Number** (using Regex)
            - 🎓 **Education** (using NER)
            - 💼 **Experience** (using NER)
            - 🛠️ **Skills** (using Keyword Extraction)
            
            ### Technologies Used:
            - spaCy for NER
            - Regular Expressions
            - pdfplumber & python-docx
            - Streamlit for UI
            
            ### Supported Formats:
            - PDF files (.pdf)
            - Word documents (.docx)
            """)
            
            st.markdown("---")
            st.markdown("### Instructions")
            st.markdown("""
            1. Upload a resume file
            2. Click 'Process Resume'
            3. View extracted information
            4. Download results as JSON
            """)
    
    def render_file_uploader(self):
        """Render the file upload section"""
        st.markdown("### 📤 Upload Resume")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            uploaded_file = st.file_uploader(
                "Choose a PDF or DOCX file",
                type=['pdf', 'docx'],
                help="Upload a resume in PDF or DOCX format"
            )
        
        return uploaded_file
    
    def render_results(self, extracted_data: dict):
        """
        Render the extracted results.
        
        Args:
            extracted_data (dict): Extracted resume data
        """
        st.markdown("---")
        st.markdown("## 📊 Extracted Information")
        
        # Create tabs for different views
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Summary", "💡 Detailed View", "📝 Raw Text", "🔍 Entities"])
        
        with tab1:
            # Display as DataFrame
            st.markdown("### Structured Data")
            df = self.formatter.format_as_dataframe(extracted_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Skills visualization
            if extracted_data.get('skills'):
                st.markdown("### 🛠️ Skills Overview")
                skills = extracted_data['skills']
                
                # Create columns for skills display
                cols_per_row = 5
                rows = [skills[i:i+cols_per_row] for i in range(0, len(skills), cols_per_row)]
                
                for row in rows:
                    cols = st.columns(cols_per_row)
                    for i, skill in enumerate(row):
                        with cols[i]:
                            st.markdown(f'<div class="skill-tag">{skill}</div>', 
                                      unsafe_allow_html=True)
                
                st.info(f"**Total Skills Found:** {len(skills)}")
        
        with tab2:
            # Detailed view
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 👤 Personal Information")
                st.write(f"**Name:** {extracted_data.get('name', 'Not found')}")
                
                if extracted_data.get('emails'):
                    st.write(f"**Email:** {', '.join(extracted_data['emails'])}")
                
                if extracted_data.get('phone_numbers'):
                    st.write(f"**Phone:** {', '.join(extracted_data['phone_numbers'])}")
                
                if extracted_data.get('linkedin'):
                    st.write(f"**LinkedIn:** {extracted_data['linkedin']}")
                
                if extracted_data.get('github'):
                    st.write(f"**GitHub:** {extracted_data['github']}")
                
                st.markdown("### 🏢 Organizations")
                orgs = extracted_data.get('organizations', [])
                if orgs:
                    for org in orgs[:10]:  # Show top 10
                        st.write(f"- {org}")
                else:
                    st.write("No organizations found")
            
            with col2:
                st.markdown("### 🎓 Education")
                education = extracted_data.get('education', [])
                if education:
                    for i, edu in enumerate(education, 1):
                        if isinstance(edu, dict):
                            st.write(f"**{i}.** {edu.get('degree', 'N/A')}")
                            st.write(f"   - Institution: {edu.get('institution', 'N/A')}")
                            st.write(f"   - Year: {edu.get('year', 'N/A')}")
                        else:
                            st.write(f"**{i}.** {edu}")
                else:
                    st.write("No education information found")
                
                st.markdown("### 💼 Experience")
                experience = extracted_data.get('experience', [])
                if experience:
                    for i, exp in enumerate(experience, 1):
                        if isinstance(exp, dict):
                            st.write(f"**{i}.** {exp.get('company', 'N/A')}")
                            st.write(f"   - Duration: {exp.get('duration', 'N/A')}")
                        else:
                            st.write(f"**{i}.** {exp}")
                else:
                    st.write("No experience information found")
        
        with tab3:
            # Raw text view
            st.markdown("### 📄 Extracted Text")
            st.text_area("Raw Text", extracted_data.get('raw_text', ''), height=400)
        
        with tab4:
            # Entities view
            st.markdown("### 🔍 Named Entities Detected")
            entities = extracted_data.get('entities', [])
            
            if entities:
                # Group entities by type
                entity_types = {}
                for entity in entities:
                    label = entity['label']
                    if label not in entity_types:
                        entity_types[label] = []
                    entity_types[label].append(entity['text'])
                
                # Display entities by type
                for label, texts in entity_types.items():
                    with st.expander(f"{label} ({len(texts)})"):
                        unique_texts = list(dict.fromkeys(texts))  # Remove duplicates
                        for text in unique_texts[:20]:  # Show top 20
                            st.write(f"- {text}")
            else:
                st.write("No entities detected")
    
    def render_download_button(self, extracted_data: dict):
        """
        Render the download button for JSON export.
        
        Args:
            extracted_data (dict): Extracted resume data
        """
        st.markdown("---")
        st.markdown("### 💾 Download Results")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col2:
            json_data = self.formatter.format_as_json(extracted_data)
            st.download_button(
                label="📥 Download as JSON",
                data=json_data,
                file_name="resume_data.json",
                mime="application/json",
                use_container_width=True
            )
    
    def run(self):
        """Main application logic"""
        self.render_header()
        self.render_sidebar()
        
        # File upload section
        uploaded_file = self.render_file_uploader()
        
        if uploaded_file is not None:
            # Display file information
            st.markdown('<div class="info-box">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**Filename:** {uploaded_file.name}")
            with col2:
                st.write(f"**File size:** {uploaded_file.size / 1024:.2f} KB")
            with col3:
                file_type = uploaded_file.name.split('.')[-1].upper()
                st.write(f"**File type:** {file_type}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Process button
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                process_button = st.button("🚀 Process Resume", use_container_width=True)
            
            if process_button:
                with st.spinner('Processing resume... Please wait.'):
                    try:
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_file_path = tmp_file.name
                        
                        # Extract text from file
                        file_type = uploaded_file.name.split('.')[-1].lower()
                        text = self.text_extractor.extract_text(tmp_file_path, file_type)
                        
                        # Clean up temp file
                        os.unlink(tmp_file_path)
                        
                        if text:
                            # Extract resume data
                            extracted_data = self.extract_resume_data(text)
                            
                            # Store in session state
                            st.session_state.extracted_data = extracted_data
                            
                            st.success("✅ Resume processed successfully!")
                            
                            # Display results
                            self.render_results(extracted_data)
                            
                            # Download button
                            self.render_download_button(extracted_data)
                        else:
                            st.error("❌ Failed to extract text from the file. The file might be empty or corrupted.")
                    
                    except Exception as e:
                        st.error(f"❌ An error occurred while processing the resume: {str(e)}")
                        st.exception(e)
            
            # Display cached results if available
            elif 'extracted_data' in st.session_state:
                st.info("Showing previously processed results. Upload a new file or click 'Process Resume' again.")
                self.render_results(st.session_state.extracted_data)
                self.render_download_button(st.session_state.extracted_data)
        
        else:
            # Welcome message when no file is uploaded
            st.markdown("---")
            st.markdown("""
            <div class="info-box">
            <h3>👋 Welcome to Smart Resume Parser!</h3>
            <p>Get started by uploading a resume file above. Our advanced NLP system will automatically extract:</p>
            <ul>
                <li>Personal information (Name, Email, Phone)</li>
                <li>Professional profiles (LinkedIn, GitHub)</li>
                <li>Educational background</li>
                <li>Work experience</li>
                <li>Technical and professional skills</li>
            </ul>
            <p><strong>Tip:</strong> For best results, use well-formatted resume files in PDF or DOCX format.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Sample output preview
            with st.expander("🔍 See Example Output"):
                st.markdown("""
                **Example Resume Parser Output:**
                
                **Sample Extracted Data:**
                - Name: John Doe
                - Email: john.doe@email.com
                - Phone: +1-234-567-8900
                - Skills: Python, Machine Learning, NLP, TensorFlow, Docker
                - Education: M.S. Computer Science - Stanford University
                - Experience: Senior Data Scientist at Tech Corp
                """)


def main():
    """Main entry point for the application"""
    app = ResumeParserApp()
    app.run()


if __name__ == "__main__":
    main()
