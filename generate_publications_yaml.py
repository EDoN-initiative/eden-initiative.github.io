import os
import yaml
import bibtexparser

# Paths
BIB_FOLDER = "_bibliography"
OUTPUT_FILE = "_data/publications.yml"

# Collect all BibTeX files
bib_files = [os.path.join(BIB_FOLDER, f) for f in os.listdir(BIB_FOLDER) if f.endswith(".bib")]

publications = []

for bib_file in bib_files:
    with open(bib_file, encoding="utf-8") as bf:
        bib_database = bibtexparser.load(bf)
        for entry in bib_database.entries:
            # Convert BibTeX entry to minimal YAML fields
            pub = {
                "title": entry.get("title", "").replace("{", "").replace("}", ""),
                "authors": entry.get("author", ""),
                "year": int(entry.get("year", "0")),
                "journal": entry.get("journal", entry.get("booktitle", "")),
                "url": entry.get("url", ""),
            }
            publications.append(pub)

# Sort by year descending
publications.sort(key=lambda x: x["year"], reverse=True)

# Ensure _data folder exists
os.makedirs("_data", exist_ok=True)

# Write YAML
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    yaml.dump(publications, f, sort_keys=False, allow_unicode=True)

print(f"Generated {OUTPUT_FILE} with {len(publications)} publications.")