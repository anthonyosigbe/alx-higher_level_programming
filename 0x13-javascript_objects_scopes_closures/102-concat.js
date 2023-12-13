#!/usr/bin/node
/* A script that concats 2 files. */
const fs = require('fs');
const content1 = fs.readFileSync(process.argv[2], 'utf8');
const content2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], content1 + content2);
