const fs = require('fs');
const path = require('path');

const EXTENSIONS_TO_STRIP = ['.mdx', '.md'];
const DOCUMENT_DIRECTORY = path.join(__dirname, 'docs');
const DONT_FORMAT = ['jsx,tsx,ts,js,css,scss,html'];

function formatName(name) {
    const fileNameWithoutExtension = name.replace(/\.[^.]+$/, '');
    const formattedName = fileNameWithoutExtension
        .replace(/([a-z])([A-Z])/g, '$1 $2') // Insert space before uppercase letter in camelCase
        //
        .replace(/_/g, ' ') // Replace underscore with space
        .replace(/-/g, ' '); // Replace hyphen with space

        const fileToLowerCase = formattedName.toLowerCase();

        const capitzalizeFirstLetter = fileToLowerCase.charAt(0).toUpperCase() + fileToLowerCase.slice(1);




        // return formattedName.join(' ');
        return capitzalizeFirstLetter;
    }

function getSubdirectories(dirPath = DOCUMENT_DIRECTORY) {
    const entries = fs.readdirSync(dirPath, { withFileTypes: true });

    const directories = entries
        .filter(dirent => dirent.isDirectory())
        .map(dirent => {
            const subdirPath = path.join(dirPath, dirent.name);
            const files = fs.readdirSync(subdirPath)
                .filter(file => EXTENSIONS_TO_STRIP.some(ext => file.endsWith(ext)))
                .map(file => {
                    const fileName = path.basename(file);
                    return formatName(fileName);
                });
            const name = formatName(dirent.name); // Use formatName for directory names as well
            const iconName = dirent.name.replace(/ /g, '-').toLowerCase(); // Use formatted name for icon
            return { name, icon: `${iconName}.svg`, files };
        });

    return directories;
}

const subdirectories = getSubdirectories();
fs.writeFileSync('aaaa.json', JSON.stringify(subdirectories, null, 2));

