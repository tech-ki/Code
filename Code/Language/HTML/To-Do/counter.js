let counter = 1;

const counterValue = document.getElementById('counter-value');
const incrementBtn = document.getElementById('increment-btn');
const decrementBtn = document.getElementById('decrement-btn');
const resetBtn = document.querySelector('#reset');

// To increment the value of counter
incrementBtn.addEventListener('click', () => {
    counter++;
    counterValue.innerHTML = this.toCommas(counter*10000000);
});

// To decrement the value of counter
decrementBtn.addEventListener('click', () => {
    counter--;
    counterValue.innerHTML = this.toCommas(counter*100);
});

// To reset the counter to zero
resetBtn.addEventListener('click', reset);

function reset() {
    this.counter = 0;
    counterValue.innerHTML = counter;
}

function toCommas(value) {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}


