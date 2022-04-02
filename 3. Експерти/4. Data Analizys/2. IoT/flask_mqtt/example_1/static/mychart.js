window.onload = function() {
    var canvas2 = document.getElementById("chart2");
    canvas2.height = 400;
    var chart2 = new Chart(canvas2, {
        type: 'line',
        data: {
            labels: Array.from({length: 1000}).map(x => ""),
            datasets: [{
                label: "Boiler Temperature",
                fill: false,
                backgroundColor: "rgba(75,192,192,0.4)",
                borderColor: "#DC143C",
                borderCapStyle: 'butt',
                pointRadius: 1,
                pointHitRadius: 10,
                data: Array.from({length: 1000}).map(x => 0),
                spanGaps: false
            }]
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    gridLines: {
                        display:false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Time",
                        fontColor: "black"
                    },
                    stacked: false,
                    beginAtZero: true,
                    ticks: {
                        autoSkip: false
                    }
                }],
                yAxes: [{
                    gridLines: {
                        display:false
                    }   
                }]
            }
        }
    });

    window.chart2 = chart2;
}