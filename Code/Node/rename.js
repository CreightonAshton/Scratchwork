const fs = require('fs');
const path = '../../Files/Node/';
const oldName = 'anFile.txt';
const newName = 'anNewFile.txt';

fs.rename(path + oldName, path + newName, (err) => {
  if (err) throw err;
  console.log('File Renamed!');
});
