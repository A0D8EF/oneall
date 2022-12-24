function change_minor_category(id){
    url = "add/?major_category=" + String(id);
    console.log(url)

    $.ajax({
        url: url,
        type: "GET",
        dataType: 'json'
    }).done( function(data, status, xhr ){
        if(!data.error){
            $("#minor_category").html(data.content);
        }else{
            console.log("大カテゴリバリデーションエラー");
        }
    }).fail( function(xhr, status, error ){
        console.log(status + ":" + error );
    });
}

function show_youtube_url(flag) {
    if (flag) {
        $(".youtube_url").show();
        $(".movie_file").css("display", "none");
    }else{
        $(".youtube_url").css("display", "none");
        $(".movie_file").show();
    }
}
function show_top_order(flag) {
    if (flag) {
        $(".top_order").show();
    }else{
        $(".top_order").css("display", "none");
    }
}


function add_major_news_category(){

    let form_elem = "#textbook_major_category_form";

    let data    = new FormData( $(form_elem).get(0) );
    let url     = $(form_elem).prop("action");
    let method  = $(form_elem).prop("method");

    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false, // dataに指定した内容をURLにエンコードして送信するかの指定
        contentType: false, // デフォルトではURLエンコードされた形式で送信されてしまう
        dataType: 'json'
    }).done( function(data, status, xhr ){
        
        if(data.error){
            console.log("ERROR");
        }else{
            // location.reload();
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    });
    
}