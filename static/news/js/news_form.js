function add_news_category(){

    let form_elem = "#add_news_category_form";

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