# Telugu Proverb Collector And Explainer 

Telugu Proverb Collector And Explainer is a Streamlit app powered by a fine tuned TinyLlama model. It interprets Telugu proverbs with nuanced variations and allows users to submit new idioms for cultural preservation. This project is in its final stages of development.

---

## Features

- Generation of proverb interpretations
- Multi-style outputs: Explanation, Summary, Youth Tone, Poetic Form, Regional Insight, Comparable Proverbs
- Idiom submission with local JSON storage

---

## Project Structure

```
Proverb Collector LLM/
├──.venv                        
├──data
   └── proverbs.json
├──model/
   └── tinyllama-telugu-model/
├──utils/
   └── pycache/
   └──format_dataset.py
   └──generate_response.py
├──tinyllama_finetune.py
├──README.md
├──requirements.txt
├──streamlit_app.py
├──test_model.py
├──training_data.json
```

---

## Setup Instructions

1. Activate virtual environment in local development environment and install required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the project directory and launch the app:

   ```bash
   streamlit run streamlit_app.py
   ```

3. Submit a proverb and optional region to generate enriched responses.

4. Use the idiom submission section to add new entries to the archive.

---

## Notes

- All prompts follow the fine-tuned format: `<s>[INST]...[/INST]`
- Submissions are stored in UTF-8 encoded JSON
- Outputs can be reused for future fine-tuning or storytelling

---

## License

Please consult the maintainers for permission before distributing modified versions.

