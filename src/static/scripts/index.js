// мат выражение
let expression = '';

// функция для заполнения мат выражения 
function appendValue(value) {
    expression += value;
    document.getElementById('result').innerText = expression;
}

// функция очисти результата
function clearResult() {
    expression = '';
    document.getElementById('result').innerText = '0';
}

// функции для вычисления значения выражения
function calculate() {
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        expression = data.result;
        document.getElementById('result').innerText = expression;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error';
    });
}

function cos() {
    fetch('/cos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        expression = data.result;
        document.getElementById('result').innerText = expression;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error';
    });
}

function sin() {
    fetch('/sin', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        expression = data.result;
        document.getElementById('result').innerText = expression;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error';
    });
}

function tan() {
    fetch('/tan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        expression = data.result;
        document.getElementById('result').innerText = expression;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error';
    });
}