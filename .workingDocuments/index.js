const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

// Database connection
const db = new sqlite3.Database('.database/data_source.db');

// Function to generate JSON file
function generateJSON() {
    return new Promise((resolve, reject) => {
        let myString = "[\n";

        db.all("SELECT * FROM extension", function (err, rows) {
            if (err) {
                reject(err);
                return;
            }

            rows.forEach((row, index) => {
                myString += `{
                    "extID": ${row.extID},
                    "name": "${row.name}",
                    "hyperlink": "${row.hyperlink}",
                    "about": "${row.about}",
                    "image": "${row.image}",
                    "language": "${row.language}"
                }${index === rows.length - 1 ? '' : ','}`;
            });

            myString += "\n]";

            fs.writeFile(path.join(__dirname, 'public', 'frontEndData.json'), myString, (err) => {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    });
}

// Generate JSON on server start
generateJSON()
    .then(() => console.log('JSON file generated successfully'))
    .catch(err => console.error('Error generating JSON:', err));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to regenerate JSON
app.get('/regenerate-json', (req, res) => {
    generateJSON()
        .then(() => res.send('JSON regenerated successfully'))
        .catch(err => res.status(500).send('Error regenerating JSON'));
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});