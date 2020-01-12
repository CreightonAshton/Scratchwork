var http = require('http');
var uc = require('upper-case');

console.log(uc);

function handleReq(req, res) {
  res.writeHead(200, {'Content-Type' : 'text/html'});
  res.write(uc.upperCase('Hello World!'));
  res.end();
}

http.createServer(handleReq).listen(8080);
