window.onload = function() {
    var canvas = document.getElementById("chart");
    canvas.height = 400;
    var chart = new Chart(canvas, {
        type: 'line',
        data: {
            labels: Array.from({length: 1000}).map(x => ""),
            datasets: [{
                label: "ECG sensor data",
                fill: false,
                backgroundColor: "rgba(75,192,192,0.4)",
                borderColor: "rgba(75,192,192,1)",
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

    window.chart = chart;
}