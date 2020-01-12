var fs = require('fs');

fs.rename('mynewFile.txt', 'renamedFile.txt', function (err) {
  if (err) throw err;
  console.log('File Renamed!')
});
