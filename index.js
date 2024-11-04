const express = require('express');
const path = require('path');
const http = require('http');
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

app.get('/frontEndData.json', (req, res) => {
    const options = {
        hostname: 'localhost',
        port: 5000,
        path: '/frontEndData.json',
        method: 'GET'
    };

    const apiReq = http.request(options, apiRes => {
        let data = '';
        apiRes.on('data', chunk => {
            data += chunk;
        });
        apiRes.on('end', () => {
            res.send(data);
        });
    });

    apiReq.on('error', error => {
        res.status(500).send(error.message);
    });

    apiReq.end();
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
