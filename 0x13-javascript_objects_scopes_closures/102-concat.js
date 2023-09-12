#!/usr/bin/node
const data = require('fs');
const a = data.readFileSync(process.argv[2], 'utf8');
const b = data.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], a + b);
