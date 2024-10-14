//Listen for when clicked, Select button
//querySelector - select first button only
/**
 * 1. Search doc for button
 * 2. Event Listen for type click, then run function click();
 */
document.querySelector("button").addEventListener("click",click)
function click(){
    alert("I got clicked");

}

function hello(){
    
}

document.getElementsById("item").innerHTML = "Ki";




  function myAdd() {

    // Create an "li" node:
    const node = document.createElement("li");
    
    // Create a text node:
    const textnode = document.createTextNode("Water");
    
    // Append the text node to the "li" node:
    node.appendChild(textnode);
    
    // Append the "li" node to the list:
    document.getElementById("mylist").appendChild(node);
    }

function myColor() {
var myNodelist = document.getElementsByClassName("late");
for (let i = 0; i < myNodelist.length; i++) {
  myNodelist[i].style.backgroundColor = "red";
    }
var myNodelist = document.getElementsByClassName("done");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(47, 245, 123)";
  }

  var myNodelist = document.getElementsByClassName("next");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(253, 237, 14)";
  }

  var myNodelist = document.getElementsByClassName("again");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(14, 217, 253)";
  }

  var myNodelist = document.getElementsByClassName("lock");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(190, 178, 192)";
  }

  
  var myNodelist = document.getElementsByClassName("void");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(190, 178, 192)";
  }

  var myNodelist = document.getElementsByClassName("doing");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(252, 61, 134)";
  }

  var myNodelist = document.getElementsById("step");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "rgb(247, 36, 117)";
  }
}
