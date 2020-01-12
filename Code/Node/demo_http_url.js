var http = require('http');

// create a function to handle request
function handleReq(req, res) {
  res.writeHead(200, {'Content-Type' : 'text/html'});
  res.write(req.url)
  res.end(); // end the response
}

// Create a server object
http.createServer(handleReq).listen(8080); //the server object listens on port 8080
