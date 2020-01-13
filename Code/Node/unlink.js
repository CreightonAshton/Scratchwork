const fs = require('fs');
const path = '../../Files/Node/';
const file = 'testfile.txt';

fs.unlink(path + file, (err) => {
  if (err) throw err;
  console.log('File deleted!');
});
