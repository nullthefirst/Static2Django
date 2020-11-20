function getTime() {
    var date = new Date();
    var time = date.toTimeString();
    return time;
}

var timeSpan = document.getElementById('time');
timeSpan.innerText = getTime();

function refreshTimeDisplay() {
    location.reload();
}
