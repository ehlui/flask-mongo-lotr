async function get_tolkien_data(endpoint) {

    var promise = await fetch(endpoint)
        .then(response => response.json())
        .then(result => { console.log('Success:', result); return result; })
        .catch(error => { console.error('Error:', error); return error; });

    return promise
}

/*Treating DOM*/

function make_table_from_array(arr, id = "not-id") {
    /*if (arr == null)
        return arr*/
    const keys = Object.keys(arr[0])
    var data_container = document.getElementById(id)
    var table = "<table>"
    var header = "<tr>"
    var body = "";

    if (data_container == null) {
        create_html("div", id, "not-class")
        var data_container = document.getElementById(id)
    }

    data_container.innerHTML = "<p>Loading...</p>"

    for (const k of Object.values(keys)) {
        header = header.concat(`<th>${k}</th>`)
    }
    header = header.concat('</tr>')

    for (const el of arr) {
        body = body.concat('<tr>')
        for (const value of Object.values(el)) {
            body = body.concat(`<td>${value}</td>`)
        }
        body = body.concat('</tr>')
    }
    table = table.concat(header).concat(body).concat("</table>")

    data_container.innerHTML = table
}

function create_html(tag = "div", id_name = "id", class_name = "class") {
    var tag_obj = document.createElement(tag);

    tag_obj.setAttribute('id', id_name);
    tag_obj.setAttribute('class', class_name);

    document.body.append(tag_obj)
}

function fetch_api(endpoint, data_name, tag_id) {
    var data_container = document.getElementById(tag_id)

    var promise = fetch(endpoint)
        .then(response => { return response.json() })

    if (data_container == null) {
        create_html("div", tag_id, "not-class")
        var data_container = document.getElementById(tag_id)
    }

    data_container.innerHTML = "<p>Loading...</p>"


    promise.then(result => {
            make_table_from_array(result[data_name], tag_id);
        })
        .catch(error => { console.error('Error:', error); return error; });
}