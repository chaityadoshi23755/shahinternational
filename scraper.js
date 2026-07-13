const fs = require('fs');
const https = require('https');
const cheerio = require('cheerio');

const BASE_URL = 'https://shahinternational.in/';
const LOCAL_DIR = './';

// Keep track of processed files to avoid infinite loops
const processedFiles = new Set();
const filesToProcess = new Set();

// Helper to fetch HTML from URL
function fetchUrl(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            if (res.statusCode !== 200) {
                reject(new Error(`Failed to fetch ${url} (status: ${res.statusCode})`));
                return;
            }
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
        }).on('error', err => reject(err));
    });
}

// Generate revamped Grid Page HTML
function generateGridPage(title, items) {
    let cardsHtml = items.map(item => `
        <a href="${item.href}" class="card">
          <div class="card-img-wrap">
            <img src="${item.img}" alt="${item.title}" class="card-img">
          </div>
          <div class="card-body">
            <h3 class="card-title">${item.title}</h3>
          </div>
        </a>`).join('');

    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} | Shah International</title>
  <link rel="shortcut icon" href="sites/default/files/favicon_v3_2024_0.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="shared-header"></div>
  <section class="page-banner" style="background-color: var(--color-bg-dark);">
    <div class="page-banner-overlay" style="background: linear-gradient(135deg, rgba(26,26,26,0.9), rgba(26,26,26,0.7));"></div>
    <div class="page-banner-content">
      <h1>${title}</h1>
      <ol class="breadcrumb"><li><a href="index.html">Home</a></li><li>${title}</li></ol>
    </div>
  </section>
  <section class="page-content">
    <div class="container">
      <div class="card-grid grid-cols-4">
        ${cardsHtml}
      </div>
    </div>
  </section>
  <div id="shared-footer"></div>
  <script src="includes.js"></script>
</body>
</html>`;
}

// Generate revamped Detail Page HTML
function generateDetailPage(title, img, htmlContent, thumbnails = []) {
    let thumbsHtml = '';
    if (thumbnails.length > 0) {
        thumbsHtml = `<div class="product-thumbnails" style="display: flex; flex-direction: column; gap: 10px;">` + 
                     thumbnails.map(t => `<img src="${t}" class="gallery-thumb" style="width: 80px; height: 80px; object-fit: cover; cursor: pointer; border-radius: var(--radius-sm); box-shadow: var(--shadow-sm); border: 2px solid transparent;" onclick="document.getElementById('main-product-image').src='${t}'; document.querySelectorAll('.gallery-thumb').forEach(el=>el.style.borderColor='transparent'); this.style.borderColor='var(--color-primary)';">`).join('') +
                     `</div>`;
    }

    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} | Shah International</title>
  <link rel="shortcut icon" href="sites/default/files/favicon_v3_2024_0.png" type="image/png">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="shared-header"></div>
  <section class="page-banner" style="background-color: var(--color-bg-dark);">
    <div class="page-banner-overlay" style="background: linear-gradient(135deg, rgba(26,26,26,0.9), rgba(26,26,26,0.7));"></div>
    <div class="page-banner-content">
      <h1>${title}</h1>
      <ol class="breadcrumb"><li><a href="index.html">Home</a></li><li>${title}</li></ol>
    </div>
  </section>
  <section class="page-content">
    <div class="container">
      <div class="product-detail-layout" style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-xl); align-items: start;">
        <div class="product-info content-block">
          <h3>${title}</h3>
          <hr class="section-divider">
          <div class="product-description" style="margin-bottom: var(--space-lg);">
            ${htmlContent}
          </div>
          <div class="product-actions" style="display: flex; gap: 15px; font-size: 24px; color: var(--color-primary);">
            <a href="javascript:history.back()" style="color: inherit; transition: color 0.3s;"><i class="fa-solid fa-circle-arrow-left"></i></a>
            <a href="javascript:window.print()" style="color: inherit; transition: color 0.3s;"><i class="fa-solid fa-print"></i></a>
          </div>
        </div>
        <div class="product-image-container" style="display: flex; gap: 15px;">
          ${thumbsHtml}
          <div class="product-image" style="flex: 1;">
            <img id="main-product-image" src="${img}" alt="${title}" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--shadow-lg);">
          </div>
        </div>
      </div>
    </div>
  </section>
  <div id="shared-footer"></div>
  <script src="includes.js"></script>
</body>
</html>`;
}

async function processFile(filename) {
    if (processedFiles.has(filename)) return;
    processedFiles.add(filename);

    console.log(`Processing: ${filename}`);

    let html;
    let title;
    
    // Always download from live site to get original content
    try {
        console.log(`Downloading ${BASE_URL + filename}...`);
        html = await fetchUrl(BASE_URL + filename);
    } catch (e) {
        console.error(`Error downloading ${filename}: ${e.message}`);
        return;
    }

    const $ = cheerio.load(html);
    
    // Determine page type and revamp
    let isGrid = $('.album-list-item').length > 0;
    title = $('h1.album-title').text().trim() || filename.replace('.html', '').replace(/-/g, ' ');

    let newHtml = '';

    if (isGrid) {
        let items = [];
        $('.album-list-item').each((i, el) => {
            let href = $(el).find('a.ali-link').attr('href');
            let img = $(el).find('img.ali-img').attr('src');
            let itemTitle = $(el).find('.ali-title').text().trim() || $(el).find('.field--name-field-portfolio-title-m').text().trim();
            if (href && !href.startsWith('http')) {
                items.push({ href, img, title: itemTitle });
                if (href.endsWith('.html')) {
                    filesToProcess.add(href);
                }
            }
        });
        newHtml = generateGridPage(title, items);
    } else {
        // Detail page
        let mainImg = $('.field--name-field-portfolio-single img.zoom').attr('src') || $('.node__content img').first().attr('src') || '';
        if (!mainImg && $('.gallery-thumb').length > 0) mainImg = $('.gallery-thumb').first().attr('src');
        
        let thumbnails = [];
        $('.gallery-thumb').each((i, el) => {
            let src = $(el).attr('src');
            if (src && !thumbnails.includes(src)) {
                thumbnails.push(src);
            }
        });

        // Clean up content
        let contentDiv = $('.field--name-field-portfolio-body').clone();
        if (contentDiv.length === 0) contentDiv = $('.node__content').clone();
        contentDiv.find('img').remove(); // Remove images from text area
        let htmlContent = contentDiv.html() || '<p>Details not available.</p>';
        
        newHtml = generateDetailPage(title, mainImg, htmlContent, thumbnails);
    }

    // Save revamped file
    fs.writeFileSync(LOCAL_DIR + filename, newHtml);
    console.log(`-> Revamped and saved ${filename}`);

    // Scan html for links
    $('a[href$=".html"]').each((i, el) => {
        let href = $(el).attr('href');
        if (href && !href.startsWith('http') && !href.includes('/') && !processedFiles.has(href)) {
            filesToProcess.add(href);
        }
    });
}

async function start() {
    // Start by scanning existing key category files to discover missing ones
    const seedFiles = [
        'Decor-Collection.html', 'best-seller.html', 'New-decors.html', 
        'MFC-Range.html', 'Synchron-range.html', 'Unique-colors.html', 'decor-applications.html'
    ];

    for (let f of seedFiles) {
        filesToProcess.add(f);
    }

    // Process loop
    while (filesToProcess.size > 0) {
        const fileArr = Array.from(filesToProcess);
        const batch = fileArr.slice(0, 10); // Process in batches
        
        for (let file of batch) {
            filesToProcess.delete(file);
            await processFile(file);
        }
    }

    console.log("Completed!");
}

start();
