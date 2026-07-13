const fs = require('fs');
const cheerio = require('cheerio');

const LOCAL_DIR = './';
const files = fs.readdirSync(LOCAL_DIR).filter(f => f.endsWith('.html'));
const allFiles = new Set(files);

let removedCount = 0;

for (let file of files) {
    const html = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(html);
    let modified = false;
    
    $('a.card').each((i, el) => {
        let href = $(el).attr('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            let path = href.split('?')[0].split('#')[0];
            if (path && path.endsWith('.html')) {
                if (!allFiles.has(path)) {
                    // Remove the card
                    $(el).remove();
                    modified = true;
                    removedCount++;
                }
            }
        }
    });
    
    if (modified) {
        fs.writeFileSync(file, $.html());
        console.log(`Removed broken links from ${file}`);
    }
}

console.log(`Total broken links (cards) removed: ${removedCount}`);
