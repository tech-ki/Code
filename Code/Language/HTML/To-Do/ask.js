
const today = new Date();
let h = today.getHours();
 let m = today.getMinutes();
 let s = today.getSeconds();
 let date = today.getFullYear();
    //m = checkTime(m);
    mm = m +(h *60);
    
let day = date.getDate();
let month = date.getMonth() + 1;
let year = date.getFullYear();

let currentDate = `${day}-${month}-${year}`;
alert(currentDate); // "17-6-2022"
