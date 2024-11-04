const express = require('express');
const path = require('path');
const app = express();

// Add CORS headers for all routes
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

app.use(express.static('public', {
    setHeaders: (res, path, stat) => {
        if (path.endsWith('.json')) {
            res.set('Content-Type', 'application/json');
            res.set('Access-Control-Allow-Origin', '*');
        }
    }
}));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
