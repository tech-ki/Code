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

const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

function addTask() {
  if(inputBox.value === ' '){
    alert("Enter a task.");
  }
  else{
    let li = document.createElement("li"); /**Create li type */
    li.innerHTML = inputBox.value; /**Make list the value */
    listContainer.appendChild(li); /*Add to end of list */
  }
  inputBox.value = "";
  saveData();
}

function saveData(){
  localStorage.setItem("data", listContainer.innerHTML);
}
function showTask(){
  listContainer.innerHTML = localStorage.getItem("data");
} 

//addNewlines.addEventListener("hover",addNewlines)
function addNewlines(str) {
  //var str = document.getElementById("t1");
  var str = "";
  var result = '';
  while (str.length > 0) {
    result += str.substring(0, 200) + '\n';
    str = str.substring(200);
  }
  return result;
}

function word(){
  var a = document.getElementById("t1").innerHTML;
  return a;
}
let message = `In October 1994,`;
let sentances = message.split(/[.!?]/);
document.getElementById("t1").innerHTML = "NO";
//tabs
function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}


const buttons = document.querySelectorAll("button");

for (const button of buttons) {
  button.addEventListener("click", myChange());
}

//Change star status
function myChange() {
    var element = document.getElementById("change");
    if (element.className == "open") {
      element.className = "done";
    } else {
      element.className = "open";
    } 
  }
  //1. open-done, switch statement, 

// Function to update the progress bar based on user input
function updateProgress() {
  const input = document.getElementById("input");
  const progress = parseInt(input.value);
  
  if (isNaN(progress) || progress < 0 || progress > 100) {
   alert("Please enter a number between 0 and 100.");
    return;
  }

  
  var progressBar = document.getElementById("progress-bar");
  progressBar.style.width = progress + "%";

var progressBar = document.getElementById("progress-bar1");
progressBar.style.width = progress + "%";

var progressBar = document.getElementById("progress-bar2");
progressBar.style.width = progress + "%";
}

function updateProgress3() { /*health */
  const input = document.getElementById("input3");
  var progress = parseInt(input.value);
  let count = 1;
  if (isNaN(progress) || progress < 0 || progress < 100) {
    /*alert("Please enter a number between 0 and 100.");
    return; */
  }
  else if (progress > 99 && count == 1) {
    progress %= 100;
    alert("You have leveled up! Your level is "+count);
    count++;
  }
  else if (progress > 99 && count > 0) {
    progress %= 100;
    alert("Your level is "+count);
  }
  
  var progressBar = document.getElementById("progress-bar3");
  progressBar.style.width = progress + "%";
}

  //progress bar
  var i = 0;
function move() {
  if (i == 0) {
    i = 1; //start
    var elem = document.getElementById("myBar");
    var width = 0;
    var bmax = 100;
    var wmax = bmax * 0.01;
    var id = setInterval(frame,mm); //num by count
    function frame() {
      if (width >= bmax) { //max 60 seconds
        clearInterval(id);
        i = 0; //stop
      } else {
        width++;
        elem.style.width = width / wmax +"%" ; //up by
        document.getElementById("demo-exp").innerHTML = width * 1  + ' seconds'; //show exp
      }
    }
  }
}

//Progress bar

const progressBar = document.getElementById("progress");
 let currentProgress = 50;

function increaseProgress() {
  if (currentProgress < 100) {
    currentProgress += 5;
   document.getElementById("progress").style.width = currentProgress + "px";
  }
}

function resetProgress() {
  currentProgress = 0;
  document.getElementById("progress").style.width = 0;
}
var d = 0;
var lvl = 1;
function pro() {
  /* construct manually */
  d = 1;
  var bar1 = new ldBar("#myItem1");
  /* ldBar stored in the element */
  var bar2 = document.getElementById('myItem1').ldBar;
  bar1.set(d); 
}
function add() {
  var bar2 = document.getElementById('myItem2').ldBar;
  var lvl = document.getElementById('mylvl');
  
  bar2.set(d); 
  if  (d < 100) {
   d += 5;
   bar2.set(d);
   lvl = 1; 
  }
  else {
    d -= 99;
    bar2.set(d);
    lvl = 2;
  }
}
