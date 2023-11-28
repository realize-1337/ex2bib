import re
from pybtex.database import parse_file
from langdetect import detect

def modify_title(entry):
    title = entry.fields.get('title')
    if title:
        try:
            lang = detect(title)
            if lang != 'en':
                # Modify title format for non-English titles
                entry.fields['title'] = r'\foreignlanguage{ngerman}{%s}' % title
        except:
            pass  # Ignore exceptions in language detection

def process_bib(input_file, output_file):
    bib_data = parse_file(input_file)
    for entry in bib_data.entries.values():
        modify_title(entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        output = bib_data.to_string('bibtex')
        pattern = r'"\s*(.*?)\s*"'
        # Replace spaces with { } within the string
        modified_text = re.sub(pattern, r'{\1}', output)
        f.write(modified_text)

# Replace 'input.bib' and 'output.bib' with your actual file names
input_bib_file = r'C:\Users\david\Documents\Dev\Masterarbeit\bibs\Lib_raw.bib'
output_bib_file = r'C:\Users\david\Documents\Dev\Masterarbeit\bibs\Lib2.bib'

process_bib(input_bib_file, output_bib_file)
