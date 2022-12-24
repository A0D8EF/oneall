function draw_bar_graph(){
    let label_elems = $(".monthly_sales_data_label");
    let value_elems = $(".monthly_sales_data_value");

    let labels      = [];
    let values      = [];

    for (let label_elem of label_elems){
        labels.push(label_elem.innerText);
    }
    for (let value_elem of value_elems){
        values.push(Number(value_elem.innerText));
    }

    let colors  = [];
    let red     = [255,255,227, 71, 71];
    let blue    = [ 99, 71,255,255,136];
    let green   = [ 71,227, 71,191,255];
    for (let i=0; i <red.length; i++){
        colors.push('rgb('+red[i]+','+blue[i]+','+green[i]+')');
    }

    const ctx       = document.getElementById("monthly_sales_data_graph").getContext("2d");
    const myChart   = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: colors,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                },
            },
            plugins: {
                legend: {
                    display: false,
                }
            }
        }
    });
}

function draw_stacked_bar_graph(){
    let label_elems = $(".yearly_sales_data_label");
    let value_elems = $(".yearly_sales_data_value");

    let labels      = [];
    let acs         = [];
    let questions   = [];
    let abcs        = [];
    let interviews  = [];
    let contracts   = [];

    for (let label_elem of label_elems){
        labels.push(label_elem.innerText);
    }
    let num = value_elems.length / label_elems.length;
    for (let i=0; i<label_elems.length; i++){
        acs.push(Number( value_elems[i*num ].innerText ));
        questions.push(Number( value_elems[i*num + 1].innerText ));
        abcs.push(Number( value_elems[i*num + 2].innerText ));
        interviews.push(Number( value_elems[i*num + 3].innerText ));
        contracts.push(Number( value_elems[i*num + 4].innerText ));
    }

    let colors  = [];
    let red     = [255,255,227, 71, 71];
    let blue    = [ 99, 71,255,255,136];
    let green   = [ 71,227, 71,191,255];
    for (let i=0; i <red.length; i++){
        colors.push('rgb('+red[i]+','+blue[i]+','+green[i]+')');
    }

    const ctx       = document.getElementById("yearly_sales_data_graph").getContext("2d");
    const myChart   = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "AC",
                    data: acs,
                    backgroundColor: colors[0],
                    borderWidth: 1
                },
                {
                    label: "質問",
                    data: questions,
                    backgroundColor: colors[1],
                    borderWidth: 1
                },
                {
                    label: "ABC",
                    data: abcs,
                    backgroundColor: colors[2],
                    borderWidth: 1
                },
                {
                    label: "面談",
                    data: interviews,
                    backgroundColor: colors[3],
                    borderWidth: 1
                },
                {
                    label: "契約",
                    data: contracts,
                    backgroundColor: colors[4],
                    borderWidth: 1
                },
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    },
                    stacked: true
                },
                x: {
                    stacked: true
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