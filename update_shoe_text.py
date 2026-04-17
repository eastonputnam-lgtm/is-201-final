from pathlib import Path

pages = sorted([p for p in Path('.').glob('*.html') if p.name not in ('mainpage.html','resume.html','scratch.html','webapp.html')])
updated = []
for page in pages:
    text = page.read_text()
    original = text
    text = text.replace("'Signature Shoe: ' + data.shoe;", "'Current Signature Shoe: ' + data.shoe;")
    if text != original:
        page.write_text(text)
        updated.append(page.name)
print('Updated pages:', updated)