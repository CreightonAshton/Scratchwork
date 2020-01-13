const fs = require('fs');
const data = 'Hello World!'

fs.writeFile('../../Files/Node/anFile.txt', data, (err) => {
  if (err) throw err;
  console.log('Saved!');
});
