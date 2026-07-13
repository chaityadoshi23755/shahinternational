const fs = require('fs');
const cheerio = require('cheerio');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

let replacedCount = 0;

files.forEach(file => {
    let html = fs.readFileSync(file, 'utf8');
    let $ = cheerio.load(html);
    let modified = false;

    $('img').each((i, el) => {
        let src = $(el).attr('src');
        if (src && !src.startsWith('http') && !src.startsWith('data:') && src !== 'placeholder.png') {
            let localPath = decodeURIComponent(src);
            if (!fs.existsSync(localPath)) {
                // Replace with placeholder
                $(el).attr('src', 'placeholder.png');
                modified = true;
                replacedCount++;
            }
        }
    });

    if (modified) {
        fs.writeFileSync(file, $.html());
        console.log(`Filled empty spaces in ${file}`);
    }
});

console.log(`Replaced ${replacedCount} broken images with placeholder.png.`);
