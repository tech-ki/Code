
var coll = document.getElementsByClassName("collapsible");
var coll2 = document.getElementsByClassName("collapsible2");
var coll3 = document.getElementsByClassName("collapsible3");
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
  for (i = 0; i < coll3.length; i++) {
    coll3[i].addEventListener("click", function() {
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
    var week = Math.ceil(day/7);

    let nIntervId;
    nIntervId = setInterval(com, 1000);
    
    s = checkTime(s);
    //document.getElementById('txt').innerHTML =  h + ":" + m + ":" + s + " am/pm";
    document.getElementById('min').innerHTML =  mm + ":" + s + " minutes spent today. "+ 
    "<br> D+" + day + " out of year" + " "+ date + com;
    setTimeout(startTime, 1000);

    document.getElementById('week').innerHTML = week;

  }

function name() {
 var name1 = Ki;
  document.getElementById('nm').innerHTML = name1 + "is the name";
}

document.getElementById("nm").innerHTML = "Ki";

  var level = 1;
   document.getElementById('lvl').innerHTML = "You are currently lvl " + level;

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

const selectElement = document.querySelector(".ice-cream");
const result = document.querySelector(".result");

selectElement.addEventListener("change", (event) => {
  result.textContent = `You like ${event.target.value}`;
});

function mod() {
/**Add modal functionality */
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
}

//Character movement LR
document.onkeydown = function(e) {
  switch (e.key.event) {
      case 37:
          alert('left'); //left
          break;
      case 38:
          alert('up'); //up
          break;
      case 39:
          alert('right'); //right
          break;
      case 40:
          alert('down'); //down
          break;
  }
};




/*Play*/
function playAudio() {
  var x = document.getElementById("myLevelUpAudio");
  x.play();
}