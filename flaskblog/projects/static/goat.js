"use strict";

var goats, width, height;
var parentCanvas = 'goat-canvas';
var fontSize = 32;
var t = 0;

function setup(){
    var canvasDiv = document.getElementById(parentCanvas)
    width = canvasDiv.offsetWidth;
    console.log(width);
    height = 250;
    var canvas = createCanvas(canvasDiv.offsetWidth, height);

    canvas.parent(parentCanvas);
    background(0, 0, 200);

    // goats = JSON.parse(document.getElementById('goat-js').innerHTML);
    console.log(goats);

    textSize(fontSize);

    goats.forEach( goat => {
        console.log(goat["name"], goat["score"]);
    });
}


function windowResized() {
    console.log('resized');
    var canvasDiv = document.getElementById(parentCanvas);
    width = canvasDiv.offsetWidth;
    resizeCanvas(width, height);
}


function draw() {

    clear();
    fill(50, 50, 50);
    t++;

    goats.forEach( (goat, i) => {
        var score = goat['score'];
        var name = goat['name'];
        var gtext = name + " " + score;
        var gwidth = textWidth(gtext);

        text(gtext, (20 + score * t / 10) % (width - gwidth - 20), (i + 1) * (fontSize + 2));
    });
}