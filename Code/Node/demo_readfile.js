var http = require('http');
var fs = require('fs');

function handleReq(req, res) {
  fs.readFile('demofile1.html', function(err, data) {
    res.writeHead(200, {'Content-Type' : 'text/html'});
    res.write(data);
    res.end();
  });
}

http.createServer(handleReq).listen(8080);
 
