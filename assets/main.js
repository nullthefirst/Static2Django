var date = new Date();
console.log(date);

var time = date.toTimeString();
console.log(time);

var timeSpan = document.getElementById('time');
timeSpan.innerText = time;
