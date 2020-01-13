const fs = require('fs');
const path = '../../Files/Node/lorem.txt';

fs.access(path, fs.F_OK, (err) => {
  if (err) {
    console.error(err);
    return;
  } console.log('file does exist'); // file exists
});
