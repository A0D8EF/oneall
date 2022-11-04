window.addEventListener("load", function (){
    // 大カテゴリに連動して小カテゴリを変更する
    $("#major_category").on("change", function(){ change_minor_category( $("option:selected").val() ); });
    $(".is_youtube_chk").on("change", function(){ show_youtube_url( $(this).prop("checked") ) });
    show_youtube_url( $(this).prop("checked") );
    
});
