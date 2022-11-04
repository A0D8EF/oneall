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
        $(".youtube_url").show()
    }else{
        $(".youtube_url").css("display", "none")
    }
}
