import json

content = open(r'C:\Users\chait\.gemini\antigravity-ide\brain\efe26ef5-c0ea-46c8-82e1-047b3603a5c5\.system_generated\steps\4939\content.md', encoding='utf-8').read()
json_str = content.split('export default ')[1].strip(';\n')
data = json.loads(json_str)

paths = []
for s in data['locations']:
    paths.append(f'<path id="{s["id"]}" d="{s["path"]}" opacity="0.8" fill="rgba(226,49,55,0.05)" />')

with open('india_paths.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(paths))
