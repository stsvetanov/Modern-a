var socket = io();
socket.on('connect', function() {
    console.log("Connected to server...");
});

socket.on('ecg_sample', function(ecgSample) {
    var chart = window.chart;
    var data = chart.data.datasets[0].data;

    data.push(ecgSample);
    data.shift();
    chart.update(0);
})

socket.on('ecg_analysis', function(payload) {
    $("#bpm").text(payload.bpm);
    $("#mad").text(payload.hr_mad);
    $("#ibi").text(payload.ibi);
    $("#pnn20").text(payload.pnn20);
    $("#pnn50").text(payload.pnn50);
    $("#rmssd").text(payload.rmssd);
    $("#s").text(payload.s);
    $("#sd1").text(payload.sd1);
    $("#sd1-sd2").text(payload["sd1/sd2"]);
    $("#sd2").text(payload.sd2);
    $("#sdnn").text(payload.sdnn);
    $("#sdsd").text(payload.sdsd);
    $("#breathing-rate").text(payload.breathingrate);
})