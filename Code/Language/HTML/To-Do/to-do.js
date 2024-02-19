
var coll = document.getElementsByClassName("collapsible");
var coll2 = document.getElementsByClassName("collapsible2");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
for (i = 0; i < coll2.length; i++) {
    coll2[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }

  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  let date = today.getFullYear();
  let month = today.getMonth() +1;

  

  //Get and show current time
  function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
   let date = today.getFullYear();
    let month = today.getMonth() +1;
    //m = checkTime(m);
    mm = m +(h *60);
    
    //current day of year
    var now = new Date();
    var start = new Date(now.getFullYear(), 0, 0);
    var diff = now - start;
    var oneDay = 1000 * 60 * 60 * 24;
    var day = Math.floor(diff / oneDay);
    var com = ":";

    let nIntervId;
    nIntervId = setInterval(com, 1000);
    
    s = checkTime(s);
    //document.getElementById('txt').innerHTML =  h + ":" + m + ":" + s + " am/pm";
    document.getElementById('min').innerHTML =  mm + ":" + s + " minutes spent today. "+ 
    "<br> D+" + day + " out of year" + " "+ date + com;
    setTimeout(startTime, 1000);


    
  }

  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10 for seconds
    return i;
  }

 function myFunction() {
  alert ("Hello World!");
}

function someOtherFunction() {
  alert ("This function was also executed!");
  document.getElementById("p1").innerHTML = "New text!";
}

