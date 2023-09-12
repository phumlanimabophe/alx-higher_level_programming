#!/usr/bin/node
const al = require('./100-data.js').list;
console.log(al);
console.log(al.map((item, index) => item * index));
