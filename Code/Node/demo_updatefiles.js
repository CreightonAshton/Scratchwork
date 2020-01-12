var fs = require('fs');

fs.appendFile('mynewFile.txt', 'Updated Content!', function (err) {
  if (err) throw err;
  console.log('Updated!')
});
