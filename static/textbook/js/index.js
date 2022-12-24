window.addEventListener("load", function (){
    // 大カテゴリに連動して小カテゴリを変更する
    $("#major_category").on("change", function(){ change_minor_category( $("option:selected").val() ); });
    $(".is_youtube_chk").on("change", function(){ show_youtube_url( $(this).prop("checked") ) });
    $(".is_top_chk").on("change", function(){ show_top_order( $(this).prop("checked") ) });
    show_youtube_url( $("#is_youtube_chk").prop("checked") );
    show_top_order( $("#is_top_chk").prop("checked") );
    
});
