const https = require('https');
https.get('https://shahinternational.in/Kitami-Elm.html', (res) => {
    let data = '';
    res.on('data', c => data+=c);
    res.on('end', () => {
        const cheerio = require('cheerio');
        const $ = cheerio.load(data);
        console.log("Body HTML:\n", $('.node__content').html());
        console.log("Field body HTML:\n", $('.field--name-body').html());
    });
});
