# 🚀 Hugging Face Spaces Deployment Guide
## Smart Resume Parser & Skill Extractor

This guide will help you deploy the Smart Resume Parser on Hugging Face Spaces.

---

## ✅ Pre-Deployment Checklist

All files are ready for deployment:

- ✅ **README.md** - Contains HF Spaces YAML header
- ✅ **requirements.txt** - HF Spaces compatible dependencies
- ✅ **app.py** - Streamlit application with caching
- ✅ **.streamlit/config.toml** - Streamlit configuration
- ✅ **packages.txt** - System dependencies (empty, none needed)
- ✅ **utils/** - All utility modules
- ✅ **data/skills_list.txt** - Skills database

---

## 📋 Deployment Steps

### Option 1: Deploy via Hugging Face Web Interface

1. **Create a New Space**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `smart-resume-parser` (or your choice)
   - License: MIT
   - SDK: **Streamlit**
   - Hardware: CPU (Basic) - Free tier is sufficient

2. **Upload Files**
   - Upload all project files to the Space
   - Ensure folder structure is maintained:
     ```
     ├── app.py
     ├── requirements.txt
     ├── README.md
     ├── packages.txt
     ├── .streamlit/
     │   └── config.toml
     ├── utils/
     │   ├── __init__.py
     │   ├── text_extractor.py
     │   ├── preprocess.py
     │   ├── ner_extractor.py
     │   ├── skill_extractor.py
     │   ├── regex_extractor.py
     │   └── output_formatter.py
     └── data/
         └── skills_list.txt
     ```

3. **Wait for Build**
   - HF Spaces will automatically install dependencies
   - Build time: 3-5 minutes
   - Watch the build logs for any errors

4. **Test the App**
   - Once built, the app will be available at:
     `https://huggingface.co/spaces/YOUR_USERNAME/smart-resume-parser`
   - Upload a test resume and verify functionality

### Option 2: Deploy via Git

1. **Clone Your HF Space**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/smart-resume-parser
   cd smart-resume-parser
   ```

2. **Copy Project Files**
   ```bash
   # Copy all files from this project to the cloned space
   cp -r /path/to/nlp-pbl/* .
   ```

3. **Commit and Push**
   ```bash
   git add .
   git commit -m "Initial deployment of Smart Resume Parser"
   git push
   ```

4. **Monitor Build**
   - Go to your Space URL
   - Check build logs
   - Wait for deployment to complete

---

## 🔧 Configuration Details

### requirements.txt
```txt
streamlit==1.28.0
spacy==3.7.2
https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.0/en_core_web_sm-3.7.0-py3-none-any.whl
pdfplumber==0.10.3
python-docx==1.1.0
pandas==2.1.3
numpy==1.26.2
Pillow==10.1.0
```

### README.md YAML Header
```yaml
---
title: Smart Resume Parser & Skill Extractor
emoji: 📄
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
pinned: false
---
```

### .streamlit/config.toml
```toml
[server]
headless = true
port = 7860
enableCORS = false

[theme]
primaryColor = "#1E88E5"
```

---

## 🎯 Expected Behavior

### On Startup
1. **Model Loading** (15-30 seconds first time)
   - spaCy downloads en_core_web_sm model
   - Models are cached using `@st.cache_resource`
   - Subsequent loads are instant

2. **App Ready**
   - Upload interface appears
   - Sidebar shows instructions
   - No errors in console

### On Resume Upload
1. **File Upload** - PDF/DOCX accepted
2. **Processing** - 2-5 seconds
3. **Results Display** - Multi-tab view
4. **JSON Download** - Available immediately

---

## 🐛 Troubleshooting

### Issue: Build Fails

**Check requirements.txt**
- Ensure no local paths
- Verify package versions are compatible
- Check for typos

**Check app.py**
- No hardcoded local paths
- All imports are available
- No missing files in utils/

### Issue: Model Download Fails

The app automatically downloads spaCy model on first run. If it fails:

1. Check build logs for errors
2. Verify requirements.txt includes spacy and model URL
3. Ensure sufficient memory (CPU Basic should work)

### Issue: File Upload Doesn't Work

- Verify `pdfplumber` and `python-docx` are installed
- Check that `utils/text_extractor.py` is present
- Test with a simple text-based PDF first

### Issue: UI Not Loading

- Check .streamlit/config.toml is present
- Verify app.py has `st.set_page_config()` at top
- Check for syntax errors in app.py

---

## 📊 Resource Usage

### Memory
- **Baseline**: ~200 MB (with models loaded)
- **Peak**: ~400 MB (during processing)
- **Recommended**: CPU Basic (free tier works fine)

### Processing Time
- **First load**: 30-45 seconds (model download)
- **Subsequent loads**: <2 seconds
- **Per resume**: 2-5 seconds

### Storage
- **Total Size**: ~150 MB
- **Models**: ~50 MB (en_core_web_sm)
- **Code**: ~2 MB
- **No persistent storage needed**

---

## ✅ Post-Deployment Checklist

After deployment, verify:

- [ ] App loads without errors
- [ ] Upload interface is visible
- [ ] Can upload PDF file
- [ ] Can upload DOCX file
- [ ] Processing completes successfully
- [ ] Results display in all tabs
- [ ] JSON download works
- [ ] No console errors
- [ ] Page loads in <5 seconds (after model cache)

---

## 🔄 Updating the Deployment

To update your deployed app:

1. **Make changes locally**
2. **Push to HF Space**
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push
   ```
3. **Wait for rebuild** (automatic)
4. **Test changes**

---

## 💡 Optimization Tips

### For Faster Loading
- Models are cached with `@st.cache_resource`
- No need to optimize further
- First load takes longer (model download)

### For Better Performance
- Current setup is optimal for HF Spaces
- Free tier CPU is sufficient
- No GPU needed

### For More Features
- Keep within memory limits (2 GB on free tier)
- Consider upgrading to paid tier for:
  - Larger models (en_core_web_lg)
  - Persistent storage
  - More concurrent users

---

## 🌐 Accessing Your Deployed App

### Public URL
```
https://huggingface.co/spaces/YOUR_USERNAME/smart-resume-parser
```

### Embed in Website
```html
<iframe
  src="https://YOUR_USERNAME-smart-resume-parser.hf.space"
  frameborder="0"
  width="850"
  height="450"
></iframe>
```

### Share Link
Share your Space URL directly with anyone!

---

## 📞 Support

### HF Spaces Documentation
- https://huggingface.co/docs/hub/spaces

### Streamlit Documentation
- https://docs.streamlit.io/

### Project Issues
- Check build logs in HF Space
- Review README.md for requirements
- Verify all files are uploaded

---

## 🎉 Success!

Your Smart Resume Parser is now live on Hugging Face Spaces!

**What's Next?**
- Share your Space URL
- Add to your portfolio
- Embed in your website
- Collect user feedback
- Consider enhancements:
  - Multi-language support
  - Custom skill databases
  - Resume scoring
  - Batch processing

---

## 📝 Notes

- **No API keys required**: All processing is local
- **No external calls**: Works offline after model download
- **Privacy**: Files processed in-session, not stored
- **Free tier**: Sufficient for most use cases
- **Auto-sleep**: Space sleeps after 48h inactivity (free tier)
- **Auto-wake**: Wakes up on first visit (may take 30s)

---

**Deployment Date**: Ready for deployment  
**Platform**: Hugging Face Spaces  
**Status**: ✅ Production Ready  

Happy Deploying! 🚀
