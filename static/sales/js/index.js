window.addEventListener("load", function (){

    $(".modal_label").on("click", function(){ create_sales_data_today(); });

    $(".create_sales_data").on("click", function() {
        if ( !(event.target.closest(".sales_data_lebel")) ){
            console.log(event.target);
            create_sales_data( $(this).data("day") );
        }
     });

     const tab_radios = $(".tab_radio");
     $(".tab_radio").on("change", (event) => {
         for(let t of tab_radios) {
             if( t.checked ){
                 document.cookie = "tab=" + decodeURIComponent(t.id);
                 document.cookie = "Path=/single";
                 document.cookie = "SameSite=strict";
             }
         }
     });
     set_tab();

    if ($(".sales_top").data("is_teacher") === "True") {
        if($(".teacher_tab_radio").prop("checked")){
            console.log("console")
            console.log($(".teacher_tab_radio").data("num"));
            draw_teacher_stacked_bar_monthly_graph();
            // draw_teacher_yearly_graph(0);
        }
        $(".teacher_tab_radio").on("change", function() {
            if($(this).data("num") !== 0) {
                draw_teacher_monthly_graph($(this).data("num"));
                draw_teacher_yearly_graph($(this).data("num"));
            }// else {
            //     draw_teacher_stacked_bar_graph($(this).data("num"));
            // } 
        })
    
    }else {
        draw_bar_graph();
        draw_stacked_bar_graph();
    }
    
    
     $(".ac_label").on("click", function(){ edit_ac(); });

});

function set_tab() {

    let tab_id = "tab_radio_1";
    const tab_radios = $(".tab_radio");
    
    let cookies         = document.cookie;
    let cookiesArray    = cookies.split(';');
    for(let c of cookiesArray) {
        let cArray = c.split('=');
        if( cArray[0].trim() === "tab"){
            tab_id  = cArray[1];
            break;
        }
    }
    for(let t of tab_radios) {
        if( t.id == tab_id ){
            t.checked = true;
        }
    }
}


function edit_ac() {
    console.log("edit ac");
    $("#edit_modal_chk").prop("checked", true);

    let form_elem   = "#sales_edit_form_ac";
    let data        = new FormData( $(form_elem).get(0) );
    let url         = $(form_elem).prop("action");
    
    $.ajax({
        url: url,
        type: "PUT",
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr){
        if(!data.error){
            // let date_id = "#date_" + id;
            // let date    = $(date_id).val();
            // let config_date = {
            //     locale: "ja",
            //     dateFormat: "Y-m-d",
            //     defaultDate: date
            // }
            // flatpickr(date_id, config_date);
            location.reload();
        }else{
            console.log("EDIT ERROR");
        }
    }).fail( function(xhr, status, error){
        console.log(status + ":" + error );
    });
}