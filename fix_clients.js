const fs = require('fs');
const files = fs.readdirSync('sites/default/files/2019-06').filter(f => f.endsWith('.png') || f.endsWith('.jpg'));
const cards = files.map(f => `<div class="card"><div class="card-img-wrap" style="padding: 2rem; background: #fff;"><img src="sites/default/files/2019-06/${f}" class="card-img" style="object-fit: contain;"></div></div>`).join('');
let html = fs.readFileSync('Our-Clients.html', 'utf8');
html = html.replace(/<div class="card-grid grid-cols-4">.*?<\/div>/s, '<div class="card-grid grid-cols-4">' + cards + '</div>');
fs.writeFileSync('Our-Clients.html', html);
console.log("Fixed Our-Clients.html with " + files.length + " logos.");
