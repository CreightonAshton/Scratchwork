var http = require('http');
var dt = require('./myfirstmodule');

function handleReq(req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write('The current date and time is: \n' + dt.myDateTime());
  res.end('\n Hello World! \n');
}

http.createServer(handleReq).listen(8080)
