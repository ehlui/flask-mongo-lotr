function add_btn_events() {
    var next_url = $("#btn-next").attr("href")
    var prev_url = $("#btn-prev").attr("href")

    if (next_url != null) {
        $("#btn-next").click(function() {
            fetch_api_paginations("/".concat(next_url), "chap_test", "chap_test")
        });
    }
    if (prev_url != null) {
        $("#btn-prev").click(function() {
            fetch_api_paginations("/".concat(next_url), "chap_test", "chap_test")
        });
    }
}