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