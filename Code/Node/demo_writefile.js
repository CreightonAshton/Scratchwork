var fs = require('fs');

fs.writeFile('mynewFile3.txt', 'replaced content', function(err) {
  if (err) throw err;
  console.log('Replaced!');
});
