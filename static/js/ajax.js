
function loadDoc(url, func) {

    if (window.XMLHttpRequest) {
        var xhttp = new XMLHttpRequest();
    } else {
        var xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            func(this);
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}
function startTimer() {
    loadDoc('game-status', readyToPlay);
    let reqTimer = setInterval(loadDoc, 2000, 'game-status', readyToPlay);
}
function readyToPlay(xhttp) {
    let playingStatusJson = JSON.parse(xhttp.response);
    document.getElementById("is-playing").innerHTML = playingStatusJson["crash"];
}

