window.addEventListener("load", function (){
    $("#search").on("click", function(){ url_replace_sendform(this); });
});

function url_replace_sendform(elem){

    let form_elem   = $("#news_search_form");
    let data        = new FormData( $(form_elem).get(0) );

    // 現在のクエリストリングを取得
    param   = new URLSearchParams(window.location.search);
    console.log(param.toString());

    for (let d of data){
        param.set(d[0], d[1]);
    }
    console.log(param.toString());

    window.location.href = "?" + param.toString();
}
