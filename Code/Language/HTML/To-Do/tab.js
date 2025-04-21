//Listen for when clicked, Select button
//querySelector - select first button only
/**
 * 1. Search doc for button
 * 2. Event Listen for type click, then run function click();

document.querySelector("button").addEventListener("click",click)
function click(){
    alert("I got clicked");

} */
alert("Welcome to To Doooo")

const todoForm = document.querySelector('form');
const todoInput = document.getElementById('todo-input');
const todoListUL = document.getElementById('todo-list');

//create an array
let allTodos = getTodos();
updateTodoList();

todoForm.addEventListener('submit', function(e){
    e.preventDefault(); //Don't reload page
    addTodo();
})

function addTodo(){
  const todoText = todoInput.value.trim();
  if(todoText.length > 0){
      const todoObject = {
          text: todoText,
          completed: false
      }
      allTodos.push(todoObject);
      updateTodoList();
      saveTodos();
      todoInput.value = "";
  }  
}
function updateTodoList(){
  todoListUL.innerHTML = "";
  allTodos.forEach((todo, todoIndex)=>{
      todoItem = createTodoItem(todo, todoIndex);
      todoListUL.append(todoItem);
  })
}
function createTodoItem(todo, todoIndex){
  const todoId = "todo-"+todoIndex;
  const todoLI = document.createElement("li");
  const todoText = todo.text;
  todoLI.className = "todo open";
  todoLI.innerHTML = `

   <!--Checkbox-->
                    <input type="checkbox" id="${todoId}">
                    <label class="custom-checkbox" for="${todoId}">
                       <!-- <img src= "/Code/Language/HTML/image/gold-star(inf-sm).gif"> -->
                    </label>
                    <label for="${todoId}"" class="todo-text c">
                    ${todoText}
                    </label>

                    <!--Project button-->
            <button class="project-button">
              <img src= "/Code/Language/HTML/image/open-folder.png" width="20" height="20">
          </button>

          <!--Tasks button-->
            <button class="up-button">
              <img src= "/Code/Language/HTML/image/tasks-up.png" width="20" height="20">
          </button>

          <!--Area button-->
          <button class="area-button">
            <img src= "/Code/Language/HTML/image/folder.png" width="20" height="20">
        </button>

         <!--Type button-->
        <button class="type-button">
          <img src= "/Code/Language/HTML/image/colour.png" width="20" height="20">
      </button>

            <!--SubTask button-->
            <button class="sub-button">
              <img src= "/Code/Language/HTML/image/tasks.png" width="20" height="20">
          </button>
            
            <!--Trash button-->
            <button class="delete-button">
                <img src= "/Code/Language/HTML/image/bin.png" width="20" height="20">
            </button>
  `
  const deleteButton = todoLI.querySelector(".delete-button");
    deleteButton.addEventListener("click", ()=>{
        deleteTodoItem(todoIndex);
    })
    
    const projectButton = todoLI.querySelector(".project-button");
    projectButton.addEventListener("click", ()=>{
        alert("Type of Project");
        todoLI.innerHTML = `
        <button type="button" class="collapsible2">${todoText}</button>
         <!--SubTask button-->
            <button class="sub-button">
              <img src= "/Code/Language/HTML/image/tasks.png" width="20" height="20">
          </button>
        `;
      
    })

    const areaButton = todoLI.querySelector(".area-button");
    areaButton.addEventListener("click", ()=>{
        alert("Area of Task");
        todoLI.innerHTML = `<li id="change" class="collapsible3 open">${todoText}</li>
        <!--SubTask button-->
            <button class="sub-button">
              <img src= "/Code/Language/HTML/image/tasks.png" width="20" height="20">
          </button>
          ;`
      
    })


    const typeButton = todoLI.querySelector(".type-button");
    typeButton.addEventListener("click", ()=>{
        alert("Type of Task");
      
    })

    const taskButton = todoLI.querySelector(".up-button");
    taskButton.addEventListener("click", ()=>{
        alert("Type of Task");
    
      
    })

    const subButton = todoLI.querySelector(".sub-button");
    subButton.addEventListener("click", ()=>{
        alert("Sub Task");
        todoLI.innerHTML = `<ol> 

         <input type="checkbox" id="${todoId}">
                    <label class="custom-checkbox" for="${todoId}">
                       <!-- <img src= "/Code/Language/HTML/image/gold-star(inf-sm).gif"> -->
                    </label>
                    <label for="${todoId}"" class="todo-text c">
                    ${todoText}
                    </label>

         <!--Tasks button-->
            <button class="up-button">
              <img src= "/Code/Language/HTML/image/tasks-up.png" width="20" height="20">
          </button>`;
      
    })
    const checkbox = todoLI.querySelector("input");
    checkbox.addEventListener("change", ()=>{
        allTodos[todoIndex].completed = checkbox.checked;

        if (checkbox.checked){
          todoLI.className = "todo done";
        }
        else
        todoLI.className = "todo open";

        
        saveTodos();
    })
    checkbox.checked = todo.completed;
    return todoLI;
}
function deleteTodoItem(todoIndex){
    allTodos = allTodos.filter((_, i)=> i !== todoIndex);
    saveTodos();
    updateTodoList();
}
function saveTodos(){
    const todosJson = JSON.stringify(allTodos);
    localStorage.setItem("todos", todosJson);
}
function getTodos(){
    const todos = localStorage.getItem("todos") || "[]";
    return JSON.parse(todos);
}

document.getElementsById("item").innerHTML = "Ki";




  function myAdd() {
    a = "Hello"

    // Create an "li" node:
    const node = document.createElement("li");
    
    // Create a text node:
    const textnode = document.createTextNode(a);
    
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
