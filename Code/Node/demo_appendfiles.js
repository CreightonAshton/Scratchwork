var fs = require('fs');

fs.appendFile('mynewFile.txt', 'Hello content!', function(err) {
  if (err) throw err;
  console.log('Saved!');
});
