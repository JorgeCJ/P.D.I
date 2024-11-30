function refactorCode() {
    const inputCode = document.getElementById('inputCode').value;
    const outputCode = document.getElementById('outputCode');

    if (!inputCode) {
        outputCode.textContent = 'Por favor, coloque algum código para ser refatorado.';
        return;
    }
    fetch('http://localhost:5000/refactor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_code: inputCode }),
    })
    .then(response => response.json())
    .then(data => {
        outputCode.textContent = data.refactored_code;
    })
    .catch(error => {
        console.error('Error:', error);
        outputCode.textContent = 'An error occurred while refactoring the code.';
    });
}
