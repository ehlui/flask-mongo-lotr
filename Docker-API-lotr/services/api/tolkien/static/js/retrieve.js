async function fetch_api(endpoint, data_name, tag_id) {
    var data_container = document.getElementById(tag_id)
    var timeout = 3000;

    if (data_container == null) {
        create_html("div", tag_id, "table-container")
        var data_container = document.getElementById(tag_id)
    }

    data_container.innerHTML = "<p>Loading...</p>"

    var data_and_timeout = []
    data_and_timeout = fetch_timeout(endpoint, timeout)


    var result = await Promise.race(data_and_timeout)
    handle_fetch(data_name, tag_id, result, data_container)
    return result
}

async function fetch_api_paginations(endpoint, data_name, tag_id) {
    console.log(endpoint)
    var data_container = document.getElementById(tag_id)
    var timeout = 3000;
    var data_and_timeout = []
    var result = null

    if (data_container == null) {
        create_html("div", tag_id, "table-container")
        var data_container = document.getElementById(tag_id)
    }

    data_container.innerHTML = "<p>Loading...</p>"

    data_and_timeout = fetch_timeout(endpoint, timeout)
    result = await Promise.race(data_and_timeout)

    handle_fetch(data_name, tag_id, result, data_container, is_pagination = true);
}



function fetch_timeout(endpoint, time_ms = 5000) {
    var abort_constroller = new AbortController();
    var signal = abort_constroller.signal; // store the signal to be use in fetch request
    var fetch_data = null
    var time_out = null

    fetch_data = fetch(endpoint, { signal })
        .then(resp => resp.json())
        .then(json => json)
        .catch(err => { throw err }) // sent error stack trace

    time_out = new Promise(resolve => {
        setTimeout(async() => {
            abort_constroller.abort() // abort fetch request
            resolve(`timeout: ${time_ms/1000} seg`)
        }, time_ms)
    })
    return [fetch_data, time_out]
}


function handle_fetch(data_name, tag_id, result, data_container, is_pagination = false) {
    const is_string = (typeof result === 'string')
    const is_timeout = is_string && result.includes("timeout")
    data_container.textContent = ''
    if (is_timeout) {
        data_container.innerHTML = `<p class="${tag_id}">Error :: <b>${result}</b></p>`
    } else {
        if (!is_pagination) {
            make_table_from_array(result[data_name], tag_id, data_name);
        } else {
            build_pagination_table(result, data_name, tag_id)
        }
    }
}