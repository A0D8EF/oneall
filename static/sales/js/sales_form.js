function create_sales_data_today(){

    $("#sales_form_radio_ac").prop("checked", true);
    change_flatpickr_today();
    $(".sales_form_radio").on("change", function() { change_flatpickr_today() });

}

function create_sales_data(calender_day){

    $("#sales_form_radio_ac").prop("checked", true);
    change_flatpickr(calender_day);
    $(".sales_form_radio").on("change", function() { change_flatpickr(calender_day) });

    $("#modal_chk").prop("checked", true);
}

function change_flatpickr_today() {
    
    let today   = new Date();
    let year    = String(today.getFullYear());
    let month   = ("0" + String(today.getMonth() + 1)).slice(-2);
    let day     = ("0" + String(today.getDate())).slice(-2);
    
    let date    = year + "-" + month + "-" + day;

    let config_date = {
        locale: "ja",
        dateFormat: "Y-m-d",
        defaultDate: date
    }

    if ($("#sales_form_radio_ac").prop("checked") || $("#sales_form_radio_abc").prop("checked") || $("#sales_form_radio_interview").prop("checked") ) {
        let hour    = ("0" + String(today.getHours()) ).slice(-2);
        let minute  = "00";

        date        += " " + hour + ":" + minute;
        config_date = {
            locale: "ja",
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            defaultDate: date
    }
    }

    flatpickr(".input_date", config_date);
}

function change_flatpickr(calender_day) {
    let year    = $("[name='year'] option:selected").val();
    let month   = $("[name='month'] option:selected").val();

    month       = ("0" + String(month)).slice(-2);
    let day     = ("0" + String(calender_day)).slice(-2);
    
    let date    = year + "-" + month + "-" + day;

    let config_date = {
        locale: "ja",
        dateFormat: "Y-m-d",
        defaultDate: date
    }

    if ($("#sales_form_radio_ac").prop("checked") || $("#sales_form_radio_abc").prop("checked") || $("#sales_form_radio_interview").prop("checked") ) {
        let today   = new Date();
        let hour    = ("0" + String(today.getHours()) ).slice(-2);
        let minute  = "00";

        date        += " " + hour + ":" + minute;
        config_date = {
            locale: "ja",
            enableTime: true,
            dateFormat: "Y-m-d H:i",
            defaultDate: date
    }
    }

    flatpickr(".input_date", config_date);
}
