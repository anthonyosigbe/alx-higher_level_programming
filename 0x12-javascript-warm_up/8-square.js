#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size) {
  for (let i = 0; i < size; ++i) {
    let k = 0;

    for (; k < size; ++k) {
      process.stdout.write('X');
    }

    if (k === size) {
      console.log('');
    }
  }
} else {
  console.log('Missing size');
}
