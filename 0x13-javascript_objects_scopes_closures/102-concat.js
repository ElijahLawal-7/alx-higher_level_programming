#!/usr/bin/node
// Concat two files

const fs = require('fs');

const data1 = fs.readFileSync(process.argv[2], 'utf8');
const data2 = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], data1 + data2);
