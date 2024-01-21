const express = require('express');
const fs = require('fs');
const path = require('path');
const { Readable } = require('stream');

const app = express();
const picsFolderPath = path.join(__dirname, 'pics');

app.get('/view', (req, res) => {
    const file = req.query.file;

    if (file) {
        const filePath = path.join(picsFolderPath, file);

        try {
            const stats = fs.statSync(filePath);

            if (!fs.existsSync(filePath)) {
                res.status(404).send('File not found!');
                return;
            }
            
            if (stats.isDirectory()) {
                res.status(400).send('The provided path is a directory, not a file!');
                return;
            }

            const fileStream = fs.createReadStream(filePath);
            const fileName = path.basename(filePath);

            res.setHeader('Content-Disposition', `attachment; filename=${fileName}`);
            res.setHeader('Content-Type', 'image/jpeg');

            fileStream.on('error', (err) => {
                console.error(`Error creating file stream: ${err.message}`);
                res.status(500).send('Internal Server Error');
            });

            fileStream.pipe(res);
        } catch (err) {
            if (err.code === 'ENOENT') {
                res.status(404).send('File not found!');
            } else {
                console.error(`Error accessing file: ${err.message}`);
                res.status(500).send('Internal Server Error');
            }
        }
    } else {
        res.status(400).send('No file param!');
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'index.html'));
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
