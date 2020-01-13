const fs = require('fs');

fs.readFile('../../Files/Node/lorem.txt', (err, data) => {
  if (err) {
    return console.log('Error occured while reading file');
  }
  console.log(data.toString());
});
