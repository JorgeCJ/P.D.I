## Exemplos de prompts: 

### Exemplo 1:
#### Prompt:
```text
Refatore o código JavaScript abaixo para melhorar a legibilidade e a clareza. Use nomes de variáveis e funções mais descritivos e remova quaisquer redundâncias. A refatoração deve seguir as melhores práticas de programação JavaScript, como evitar o uso de variáveis globais e melhorar a estrutura do código.
```
```javascript

function calc(x, y) {
    var z = x + y;
    return z;
}

var result = calc(5, 10);
console.log(result);
```

### Exemplo 2:
#### Prompt:
```text
Refatore o código JavaScript abaixo para melhorar sua performance. O código deve ser otimizado para manipular grandes volumes de dados de forma eficiente. Elimine qualquer operação desnecessária e use técnicas de otimização como caching ou reduzir o número de loops.
```
```javascript
function processData(arr) {
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr.length; j++) {
            if (arr[i] + arr[j] === 10) {
                result.push([arr[i], arr[j]]);
            }
        }
    }
    return result;
}

var numbers = [1, 2, 3, 7, 8, 9];
console.log(processData(numbers));
```

### Exemplo 3:
#### Prompt:
```text
Refatore o código JavaScript abaixo para usar práticas idiomáticas do JavaScript moderno, como funções de ordem superior, `map()`, `filter()`, e `reduce()`. O código também deve ser mais conciso e eficiente, sem perder clareza.
```
```javascript
function doubleAndFilter(arr) {
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 === 0) {
            result.push(arr[i] * 2);
        }
    }
    return result;
}

var numbers = [1, 2, 3, 4, 5, 6];
console.log(doubleAndFilter(numbers));
```

### Exemplo 4:
#### Prompt:

```text
Refatore o código JavaScript abaixo para eliminar redundâncias e melhorar a manutenção do código. O código atual contém seções duplicadas e pode ser melhorado ao evitar a repetição de lógica.
```
```javascript
function calculatePrice(price, discount) {
    var discountedPrice = price - (price * discount);
    return discountedPrice;
}

function calculateTotalPrice(price1, price2, discount) {
    var discountedPrice1 = price1 - (price1 * discount);
    var discountedPrice2 = price2 - (price2 * discount);
    return discountedPrice1 + discountedPrice2;
}

var total = calculateTotalPrice(100, 150, 0.1);
console.log(total);
```

### Exemplo 5:
#### Prompt:

```text
Refatore o código JavaScript abaixo para melhorar o tratamento de erros e adicionar verificações mais robustas para entradas inválidas. O código atual não lida corretamente com exceções e não valida as entradas de forma adequada.
```
```javascript
function divide(a, b) {
    return a / b;
}

console.log(divide(10, 0));
```

### Exemplo 6:
#### Prompt:

```text
Refatore o código JavaScript abaixo para dividir o código em módulos e funções mais pequenas, seguindo o princípio de responsabilidade única. Isso facilitará a manutenção e reutilização do código.
```
```javascript
function calculateDiscount(price) {
    if (price > 100) {
        return price * 0.9;
    }
    return price * 0.95;
}

function calculateShipping(price) {
    if (price > 50) {
        return 10;
    }
    return 5;
}

function calculateFinalPrice(price) {
    var discount = calculateDiscount(price);
    var shipping = calculateShipping(price);
    return discount + shipping;
}

console.log(calculateFinalPrice(120));
```

### Exemplo 7:
#### Prompt:

```text
Refatore o código JavaScript abaixo para usar `async/await` em vez de callbacks para lidar com funções assíncronas. Isso deve melhorar a legibilidade e tornar o código mais fácil de entender.
```
```javascript
function fetchData(callback) {
    setTimeout(() => {
        callback("Data fetched");
    }, 1000);
}

fetchData(function(result) {
    console.log(result);
});
```

### Exemplo 8:
#### Prompt:

```text
Refatore o código JavaScript abaixo para usar `Promises` em vez de callbacks, melhorando a estrutura e a clareza ao lidar com funções assíncronas.
```
```javascript
function fetchData(callback) {
    setTimeout(() => {
        callback("Data fetched");
    }, 1000);
}

fetchData(function(result) {
    console.log(result);
});
```

### Exemplo 9:
#### Prompt:

```text
Refatore o código JavaScript abaixo para tratar erros usando `try/catch` em vez de verificações `if` para garantir a manipulação correta das exceções.
```
```javascript
function fetchData(callback) {
    setTimeout(() => {
        const error = false; // Simulando erro
        if (error) {
            callback("Error occurred");
        } else {
            callback(null, "Data fetched");
        }
    }, 1000);
}

fetchData(function(error, result) {
    if (error) {
        console.log(error);
    } else {
        console.log(result);
    }
});
```

### Exemplo 10:
#### Prompt:

```text
Refatore o código JavaScript abaixo para usar o método `forEach` em vez de um loop `for` tradicional, para tornar o código mais legível e conciso.
```
```javascript
const numbers = [1, 2, 3, 4, 5];

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
```
