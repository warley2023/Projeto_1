const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Servidor rodando com sucesso!');
});

server.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});
