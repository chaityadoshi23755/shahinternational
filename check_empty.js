const fs = require('fs');
const cheerio = require('cheerio');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
let missing = [];

files.forEach(file => {
    const html = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(html);
    $('img').each((i, el) => {
        let src = $(el).attr('src');
        if (src && !src.startsWith('http') && !src.startsWith('data:')) {
            // Check if file exists locally
            let localPath = decodeURIComponent(src);
            if (!fs.existsSync(localPath)) {
                missing.push({ file, src: localPath });
            }
        }
    });
});

console.log(`Found ${missing.length} missing image references in HTML files.`);
if (missing.length > 0) {
    missing.slice(0, 10).forEach(m => console.log(m.file + ': ' + m.src));
}
