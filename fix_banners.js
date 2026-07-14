const fs = require('fs');
const cheerio = require('cheerio');
const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

let modifiedCount = 0;

files.forEach(file => {
    let html = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(html, { decodeEntities: false });

    const mainImg = $('#main-product-image');
    if (mainImg.length > 0) {
        const src = mainImg.attr('src');
        const banner = $('.page-banner');
        
        if (banner.length > 0) {
            // Remove the hardcoded dark background style
            banner.removeAttr('style');
            
            // Check if it already has a banner bg
            if (banner.find('.page-banner-bg').length === 0) {
                // Prepend the image
                banner.prepend(`<img src="${src}" class="page-banner-bg" alt="Product Banner">`);
                
                fs.writeFileSync(file, $.html());
                modifiedCount++;
                console.log('Fixed ' + file);
            }
        }
    }
});

console.log('Total files modified: ' + modifiedCount);
