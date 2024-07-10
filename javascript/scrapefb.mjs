import fs from 'fs/promises';   
import cheerio from 'cheerio';
import clipboardy from 'clipboardy';

async function fetchHtml(filePath) {
    try {
        const htmlContent = await fs.readFile(filePath, 'utf-8');
        console.log("HTML fetched:", filePath); // Log when HTML is fetched
        return htmlContent;
    } catch (error) {
        console.error("Error fetching HTML:", error);
    }
}

function extractLinks(htmlContent) {
    console.log("Extracting links..."); // Log before extraction starts
    const $ = cheerio.load(htmlContent);
    const links = [];
    $('a[href]').each(function() {
        links.push($(this).attr('href'));
    });
    console.log("Found links:", links.length); // Log number of found links
    return links;
}

function filterLinks(links) {
    const filteredLinks = new Set();
    links.forEach(link => {
        if (link.includes('facebook.com') && !['photo', 'friends', 'mutual'].some(keyword => link.includes(keyword))) {
            filteredLinks.add(link);
        }
    });
    return Array.from(filteredLinks).sort();
}

async function writeToFile(links, baseFilename) {
    let i = 0;
    let filename;
    do {
        filename = `${baseFilename}${i > 0 ? i : ''}.txt`;
        i++;
    } while (await fs.stat(filename).then(() => true, () => false));

    await fs.writeFile(filename, links.join('\n'));
    return filename;
}

async function main() {
    const filePath = 'toscrape.html';
    const htmlContent = await fetchHtml(filePath);
    const links = extractLinks(htmlContent);
    const filteredLinks = filterLinks(links);
    const filename = await writeToFile(filteredLinks, 'scrape');

    clipboardy.writeSync(filteredLinks.join('\n'));

    console.log(`Filtered links written to ${filename}`);
}

main().catch(console.error);
