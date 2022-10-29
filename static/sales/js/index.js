window.addEventListener("load", function (){

    const tab_radios = $(".tab_radio");
    $(".tab_radio").on("change", (event) => {
        for(let t of tab_radios) {
            if( t.checked ){
                document.cookie = "tab=" + decodeURIComponent(t.id);
                document.cookie = "Path=/single";
                document.cookie = "SameSite=strict";
                // console.log(document.cookie);
            }
        }
    });

    set_tab();

    $(".income_chk").on("change", function(){ change_expense_item( $(this).prop("checked"), $(this).val() ); });
    change_expense_item($("#income_chk").prop("checked"), $("#income_chk").val() );

    $("#add_income").on("click", function() { add_income(); });
    $("#modal_sw").on("click", function() { list_income(); });
    $(".modal_bg").on("click", function() {
        $("#modal_sw").prop("checked", false);
    })

    // balanceの新規登録
    $(".modal_label[for='modal_chk']").on("click", function() {
        $("#balance_form").prop("action", "");
    });

    // balanceの編集
    $(".edit_modal_chk").prop("checked", false);
    $(".submit_edit").on("click", function() { edit( $(this).val() ); });

    // balanceの削除
    $(".trash").on("click", function() { trash( $(this).val() ); });

    $(".create_day_balance").on("click", function() {
        if ( !(event.target.closest(".day_balance")) ){
            create_day_balance( $(this).data("day") );
        }
     });

    draw_bar_graph();
    draw_income_pie_graph();
    draw_spending_pie_graph();

    $(".day_balance").on("click", function() {
        $("#tab_radio_1").prop("checked", false);
        $("#tab_radio_2").prop("checked", true);
    })
});


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