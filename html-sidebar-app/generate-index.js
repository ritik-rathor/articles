import fs from 'fs';
import path from 'path';

const articlesDir = path.join(process.cwd(), 'public/articles');
const outputFile = path.join(process.cwd(), 'src/articles-index.json');

try {
    if (!fs.existsSync(articlesDir)) {
        fs.mkdirSync(articlesDir, { recursive: true });
    }

    const files = fs.readdirSync(articlesDir)
        .filter(file => file.endsWith('.html'))
        .map(file => file.replace('.html', ''));

    fs.writeFileSync(outputFile, JSON.stringify(files, null, 2));
    console.log(`✅ Successfully indexed ${files.length} HTML files.`);
} catch (error) {
    console.error('❌ Error indexing files:', error);
}