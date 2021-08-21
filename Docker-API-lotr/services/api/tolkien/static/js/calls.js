const api = 'tolkien'
const endpoints = {
    'books': `/${api}/books`,
    'movies': `/${api}/movies`,
    'chapters': `/${api}/chapters`
}


for (const [k, v] of Object.entries(endpoints)) {
    fetch_api(v, k, k);
}

function addstyle() {
    document.getElementById('style').href = '/tolkien/static/css/style.css';
}