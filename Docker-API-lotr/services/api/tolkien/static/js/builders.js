function make_table_from_array(arr, id = "not-id", data_name) {
    const keys = Object.keys(arr[0])
    var data_container = document.getElementById(id)
    var table = "<table>"
    var header = "<tr>"
    var body = "";

    //clean up all within data
    data_container.innerHTML = null

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


    var title = document.createElement("h2");
    var text_title = document.createTextNode(data_name);
    title.appendChild(text_title);

    table = table.concat(header).concat(body).concat("</table>")
    data_container.innerHTML = table

    data_container.prepend(title);

}


function create_html(tag = "div", id_name = "id", class_name = "class") {
    var tag_obj = document.createElement(tag);

    tag_obj.setAttribute('id', id_name);
    tag_obj.setAttribute('class', class_name);

    document.body.append(tag_obj)
}


function build_btn_pag(text, id, href) {
    var btn = document.createElement("button");
    text_title = document.createTextNode(text);
    btn.setAttribute('id', id);
    btn.setAttribute('href', href);
    btn.appendChild(text_title);
    return btn;
}

function build_pagination_table(result, data_name, tag_id) {
    var results = null
    try {
        results = Object.values(result["result"])
    } catch (error) {
        return;
    }

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