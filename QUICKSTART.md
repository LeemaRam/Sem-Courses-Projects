# Quick Start Guide
## Smart Resume Parser & Skill Extraction System

### Installation (Quick Version)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

2. **Run the application:**
   ```bash
   streamlit run app.py
   ```

3. **Access the app:**
   - Open browser to: http://localhost:8501

### Usage

1. Click "Browse files" and select a resume (PDF or DOCX)
2. Click "🚀 Process Resume"
3. View extracted data in the tabs
4. Download JSON using "Download as JSON" button

### Testing the Application

Use the sample resume in `data/sample_resumes/sample_resume_john_doe.txt`:
- Copy content to a Word document and save as .docx
- Or convert to PDF using any PDF creator

### Troubleshooting

**spaCy model not found:**
```bash
python -m spacy download en_core_web_sm
```

**Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

**Module not found error:**
```bash
# Make sure you're in the project directory
cd /path/to/Smart-Resume-Parser
pip install -r requirements.txt
```

### Project Structure Overview

```
├── app.py                  # Main Streamlit app (start here)
├── utils/                  # All processing modules
│   ├── text_extractor.py   # Extract text from PDF/DOCX
│   ├── ner_extractor.py    # Named Entity Recognition
│   ├── skill_extractor.py  # Skill extraction
│   └── ...
├── data/
│   ├── skills_list.txt     # Skills database
│   └── sample_resumes/     # Test files
└── requirements.txt        # Dependencies
```

### Next Steps

- Read [README.md](README.md) for detailed documentation
- Check [report_outline.md](report_outline.md) for academic report structure
- Customize `data/skills_list.txt` with your own skills
- Extend functionality by modifying utility modules

### Support

For issues:
1. Check README.md troubleshooting section
2. Verify all dependencies are installed
3. Ensure you're using Python 3.10+

Happy parsing! 📄✨
