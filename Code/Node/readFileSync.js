const fs = require('fs');
const data = fs.readFileSync('../../Files/Node/lorem.txt');
console.log(data.toString());
