const fs = require('fs');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let original = content;
    
    // Remove the bad inline styles
    content = content.replace(/style="display: grid; grid-template-columns: 1fr 1fr; gap: var\(--space-xl\); align-items: start;"/g, '');
    content = content.replace(/style="display: flex; gap: 15px;"/g, '');
    content = content.replace(/style="display: flex; flex-direction: column; gap: 10px;"/g, '');
    
    // Some lines might have extra spaces if formatted differently, but the generator did it exactly like above.
    
    if (content !== original) {
        fs.writeFileSync(file, content);
        console.log('Fixed ' + file);
    }
});
