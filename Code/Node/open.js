const fs = require('fs');

fs.open('../../Files/Node/anFile.txt', 'w', (err, file) => {
  if (err) throw err;
  console.log('Saved!');
});
