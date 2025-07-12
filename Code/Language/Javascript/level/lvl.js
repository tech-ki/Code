
// Level Ip

level = 1;
exp = 5;
exp_req = 20; //exp - exp_req per level
tm = 0;

function add_exp(exp_to_add){
    exp += exp_to_add;
    if (exp >= exp_req)
    {
        level++;
        exp - exp_req;
        exp_req += 10;
    }
}

function clocks(tm){



}

 //current day of year
var now = new Date();
var start = new Date(now.getFullYear(), 0, 0);
var diff = now - start;
var oneDay = 1000 * 60 * 60 * 24;
var day = Math.floor(diff / oneDay);
var com = ":";
var week = Math.ceil(day/7);

var hr = now.getHours();
var dy = now.getDay();
var mn = now.getMinutes();


//Time
setInterval(myTimer, 1000); //every second, 1000 ms = 1 sec

function myTimer() {
  const d = new Date();
  document.getElementById("tm").innerHTML = d.toLocaleTimeString([], {
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
});
}



add_exp(10) //15
add_exp(10) //25, 2
add_exp(100) //35
//add_exp(10) //45

document.getElementById("lvl").innerHTML = level;
document.getElementById("exp").innerHTML = exp;
document.getElementById("tm").innerHTML = mn;

