const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question('', input => {
    const [a, b, c] = input.split(' ').map(Number);
    console.log(a * b * (1 / c));
    readline.close();
  });