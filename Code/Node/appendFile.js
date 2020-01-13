const fs = require('fs');
const path = '../../Files/Node/anFile.txt';
const newData = 'This is new data.';

fs.appendFile(path, newData, (err) => {
  if (err) throw err;
  console.log('File Updated!');
});
