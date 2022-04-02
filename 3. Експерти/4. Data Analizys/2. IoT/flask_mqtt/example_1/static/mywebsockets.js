var socket = io();
socket.on('connect', function() {
    console.log("Connected to flask_app...");
});

socket.on('ecg_sample', function(payload) {
    var chart = window.chart2;
    var data = chart.data.datasets[0].data;


    data.push(payload);
    data.shift();
    chart.update(0);
});

socket.on('ecg_analysis', function(payload) {

    $("#temp").text(payload +" ℃");

    if ((payload)<=45) {
        $("#temp").css("font-size", "44px");
        //$("#bpm").css("font-color", "blue");
        document.getElementById("temp").style.color = "blue";
    }
    else {
        //$("#bpm").css("font-color", "red");
        $("#temp").css("font-size", "44px");
        document.getElementById("temp").style.color = "FireBrick";
    }

    if ((payload)<=45) {
        $("#showernum").text(1);
    }
    else {
        $("#showernum").text(2);
    }
});