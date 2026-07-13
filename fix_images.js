const fs = require('fs');
const https = require('https');
const path = require('path');
const cheerio = require('cheerio');

const BASE_URL = 'https://shahinternational.in/';
const LOCAL_DIR = './';

// Function to download a file
function downloadFile(url, dest) {
    return new Promise((resolve, reject) => {
        // Create directories if they don't exist
        const dir = path.dirname(dest);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }

        const file = fs.createWriteStream(dest);
        https.get(url, (res) => {
            if (res.statusCode !== 200) {
                file.close();
                fs.unlink(dest, () => {}); // Delete empty file
                reject(new Error(`Status: ${res.statusCode}`));
                return;
            }
            res.pipe(file);
            file.on('finish', () => {
                file.close(resolve);
            });
        }).on('error', (err) => {
            file.close();
            fs.unlink(dest, () => {});
            reject(err);
        });
    });
}

async function fixImages() {
    const files = fs.readdirSync(LOCAL_DIR).filter(f => f.endsWith('.html'));
    const missingImages = new Set();

    console.log("Scanning files for missing images...");
    for (let file of files) {
        const html = fs.readFileSync(file, 'utf8');
        const $ = cheerio.load(html);
        
        $('img').each((i, el) => {
            let src = $(el).attr('src');
            if (src && src.startsWith('sites/')) {
                // Decode URI because src might have %20
                let localPath = decodeURIComponent(src);
                if (!fs.existsSync(localPath)) {
                    missingImages.add(src);
                }
            }
        });
    }

    console.log(`Found ${missingImages.size} missing images. Downloading...`);
    
    let successCount = 0;
    let failCount = 0;
    
    // Download missing images sequentially to avoid overwhelming the server
    for (let src of missingImages) {
        let url = BASE_URL + src; // Note: src in HTML might be encoded or not. If it has spaces, it might need encoding.
        // If the src already has %20, using it directly in URL is fine.
        // Ensure url is properly encoded if it isn't.
        if (!src.includes('%')) {
            url = BASE_URL + encodeURI(src);
        }
        
        let dest = decodeURIComponent(src);
        
        try {
            await downloadFile(url, dest);
            console.log(`[OK] Downloaded: ${dest}`);
            successCount++;
        } catch (e) {
            console.log(`[FAIL] ${url} - ${e.message}`);
            failCount++;
        }
    }
    
    console.log(`Finished downloading images. Success: ${successCount}, Failed: ${failCount}`);
}

fixImages();
