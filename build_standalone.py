import os

scratch_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\retail-sales-dashboard"
artifact_file = r"C:\Users\Asus\.gemini\antigravity\brain\e1554a3b-987f-46f6-ad87-a03e21efc604\retail_sales_dashboard.html"

with open(os.path.join(scratch_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

with open(os.path.join(scratch_dir, "styles.css"), "r", encoding="utf-8") as f:
    css = f.read()

with open(os.path.join(scratch_dir, "data.js"), "r", encoding="utf-8") as f:
    data_js = f.read()

with open(os.path.join(scratch_dir, "app.js"), "r", encoding="utf-8") as f:
    app_js = f.read()

# Replace <link rel="stylesheet" href="styles.css"> with <style>...</style>
html = html.replace('<link rel="stylesheet" href="styles.css">', f'<style>\n{css}\n</style>')

# Replace <script src="data.js"></script> and <script src="app.js"></script> with inlined scripts
combined_scripts = f'<script>\n{data_js}\n</script>\n<script>\n{app_js}\n</script>'
html = html.replace('<script src="data.js"></script>\n  <!-- Main Application Logic -->\n  <script src="app.js"></script>', combined_scripts)
html = html.replace('<script src="data.js"></script>\n  <script src="app.js"></script>', combined_scripts)

with open(artifact_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated standalone artifact at {artifact_file} ({len(html)} bytes)")
