async function get_tolkien_data(endpoint) {
    var promise = await fetch(endpoint)
        .then(response => response.json())
        .then(result => { console.log('Success:', result); return result; })
        .catch(error => { console.error('Error:', error); return error; });
    return promise
}

/*Treating DOM*/


function fetch_api_paginations(endpoint, data_name, tag_id, has_pagination = false) {
    var data_container = document.getElementById(tag_id)
    var promise = fetch(endpoint)
        .then(response => { return response.json() })

    if (data_container == null) {
        create_html("div", tag_id, "table-container")
        var data_container = document.getElementById(tag_id)
    }

    data_container.innerHTML = "<p>Loading...</p>"

    promise
        .then(result => {
            manage_paginations(result, tag_id, data_name);
        })
        .catch(error => { console.error('Error:', error); return error; });
}

async function fetch_api(endpoint, data_name, tag_id, has_pagination = false) {
    var data_container = document.getElementById(tag_id)
    var timeout = 3000;

    if (data_container == null) {
        create_html("div", tag_id, "table-container")
        var data_container = document.getElementById(tag_id)
    }

    data_container.innerHTML = "<p>Loading...</p>"

    var data_and_timeout = []
    if (!has_pagination) {
        data_and_timeout = fetch_timeout(endpoint, tag_id, timeout)
    }


    var result = await Promise.race(data_and_timeout)
    handle_fetch(data_name, tag_id, result, data_container)
    return result
}

function fetch_timeout(endpoint, tag_id, timeout_ms = 5000) {
    var abort_constroller = new AbortController();
    var signal = abort_constroller.signal; // store the signal to be use in fetch request
    var fetch_data = null
    var time_out = null

    fetch_data = fetch(endpoint, { signal })
        .then(resp => resp.json())
        .then(json => json)
        .catch(err => { throw err }) // sent error stack trace
        // set timeout
    time_out = new Promise(resolve => {
        setTimeout(async() => {
            abort_constroller.abort() // abort fetch request
            resolve(`timeout: ${timeout_ms/1000} seg`)
        }, timeout_ms)
    })
    return [fetch_data, time_out]
}


function handle_fetch(data_name, tag_id, result, data_container) {
    const is_string = (typeof result === 'string')
    const is_timeout = is_string && result.includes("timeout")

    if (is_timeout) {
        data_container.innerHTML = `<p class="${tag_id}">Error :: <b>${result}</b></p>`
    } else {
        console.log(data_container)
        data_container.textContent = ''
        make_table_from_array(result[data_name], tag_id, data_name);
    }
}

function manage_paginations(result, tag_id, data_name) {
    const results = Object.values(result["result"])
    var data_container = document.getElementById(tag_id)
    var prev_url = result["prev_url"]
    var next_url = result["next_url"]
    var table = "<table>"
    var rows = "";

    var title = document.createElement("h2");
    var text_title = document.createTextNode(data_name);
    title.setAttribute('id', `title-${tag_id}`);
    title.appendChild(text_title);

    for (const r of results) {
        rows = rows.concat('<tr>')
        for (const k of Object.keys(r)) {
            rows = rows.concat(`<td>${r[k]}</td>`)
        }
        rows = rows.concat('</tr>')
    }

    table = table.concat(rows).concat("</table>")
    data_container.innerHTML = table
    data_container.prepend(title);

    if (next_url) {
        var btn_next = build_btn_pag("Next", "btn-next", next_url)
        data_container.append(btn_next);
    }
    if (prev_url) {
        var btn_prev = build_btn_pag("Previous", "btn-prev", prev_url)
        data_container.append(btn_prev);
    }

}