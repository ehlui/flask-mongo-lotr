const api = 'tolkien'
const endpoints = {
    'books': `/${api}/books`,
    'movies': `/${api}/movies`,
    'chapters': `/${api}/chapters`,
}
const endpoints_with_paginations = {
    'chap_test': `/${api}/chap_test`
}

for (const [k, v] of Object.entries(endpoints)) {
    fetch_api(v, k, k);
}

for (const [k, v] of Object.entries(endpoints_with_paginations)) {
    fetch_api_paginations(v, k, k);
}

function addstyle() {
    document.getElementById('style').href = '/tolkien/static/css/style.css';
}