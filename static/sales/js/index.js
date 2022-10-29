window.addEventListener("load", function (){

    $(".modal_label").on("click", function(){ create_sales_data_today(); });

    $(".create_sales_data").on("click", function() {
        if ( !(event.target.closest(".sales_data_label")) ){
            create_sales_data( $(this).data("day") );
        }
     });


});

function create_sales_data_today(){
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

    flatpickr(".input_date", config_date);
    $("#sales_form_radio_ac").prop("checked", true);
}


function create_sales_data(calender_day){
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

    flatpickr(".input_date", config_date);
    $("#modal_chk").prop("checked", true);
    $("#sales_form_radio_ac").prop("checked", true);
}


function draw_bar_graph(){

    let label_elems = $(".monthly_balance_label");
    let data_elems  = $(".monthly_balance_data");

    let labels      = [];
    let datas       = [];

    for (let label_elem of label_elems){
        labels.push(label_elem.innerText.replace("年", "/").replace("月", ""));
    }
    for (let data_elem of data_elems){
        let raw_data    = data_elem.innerText;
        datas.push(Number(raw_data.replace(/,/g, "").replace("\xA5", "")));
    }

    let colors      = [];
    for (let data of datas){
        if (data >= 0){
            colors.push('rgba(20,60,220,0.8)');
        }else{
            colors.push('rgba(220,20,60,0.8)');
        }
    }

    const ctx       = document.getElementById("monthly_balance_graph").getContext("2d");
    const myChart   = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "収支",
                data: datas,
                backgroundColor: colors,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                legend: {
                    display: false,
                }
            }
        }
    });
}