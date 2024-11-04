// API endpoints and handlers
const API_URL = '/api';

// Fetch data from the server
async function getData() {
    const response = await fetch(`${API_URL}/data`);
    return response.json();
}

// Send data to the server
async function postData(data) {
    const response = await fetch(`${API_URL}/data`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

