const fs = require('fs');
const cheerio = require('cheerio');

const LOCAL_DIR = './';
const files = fs.readdirSync(LOCAL_DIR).filter(f => f.endsWith('.html'));

let brokenLinks = [];
let allFiles = new Set(files);

for (let file of files) {
    const html = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(html);
    
    $('a').each((i, el) => {
        let href = $(el).attr('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto:') && !href.startsWith('tel:')) {
            // It's a local link
            // Remove any query params or hashes
            let path = href.split('?')[0].split('#')[0];
            if (path && path.endsWith('.html')) {
                if (!allFiles.has(path)) {
                    brokenLinks.push({ source: file, target: path });
                }
            }
        }
    });
}

if (brokenLinks.length > 0) {
    console.log("Broken links found:");
    brokenLinks.forEach(b => {
        console.log(`- In ${b.source}: points to missing ${b.target}`);
    });
} else {
    console.log("No broken internal HTML links found!");
}
