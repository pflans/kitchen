
const http = require('http');

let app = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello world');
});

app.listen(8000);
console.log('Node server running on port 8080');
