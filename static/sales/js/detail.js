window.addEventListener("load", function (){
    $(".trash").on("click", function() { trash( $(this).val() ); });
    $("#submit_edit").on("click", function() { edit( $(this).data("salestype") ); });

    let sales_type = $("#submit_edit").data("salestype");
    if ( sales_type == "ac" | sales_type == "abc" | sales_type == "interview" ){
        let date_time    = $(".date_time").val();
        let config_datetime = {
            locale: "ja",
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            defaultDate: date_time
        }
        flatpickr(".date_time", config_datetime);
    }else {
        let date    = $(".date").val();
        let config_date = {
            locale: "ja",
            dateFormat: "Y-m-d",
            defaultDate: date
        }
        flatpickr(".date", config_date);
    }
});

function trash(id){

    if(!confirm("本当に削除しますか？")){
        return false;
    }

    let url = DELETE_URL.replace("1", id);

    $.ajax({
        url: url,
        type: "DELETE",
        dataType: 'json'
    }).done( function(data, status, xhr){
        if(!data.error){
            window.location.href = RETURN_URL;
        }else{
            console.log("DELETE ERROR");
        }
    }).fail( function(xhr, status, error){
        console.log(status + ":" + error );
    });
}

function edit(salestype){

    let form_elem   = "#" + salestype + "_edit_form";
    let data        = new FormData( $(form_elem).get(0) );
    let url         = $(form_elem).prop("action");
    console.log(url);

    $.ajax({
        url: url,
        type: "PUT",
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr){
        if(!data.error){
            location.reload();
        }else{
            console.log("EDIT ERROR");
        }
    }).fail( function(xhr, status, error){
        console.log(status + ":" + error );
    });
}
