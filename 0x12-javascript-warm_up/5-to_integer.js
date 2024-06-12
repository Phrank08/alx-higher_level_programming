#!/usr/bin/node

const strInt = parseInt(process.argv[2]);
if (isNaN(strInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + strInt);
}
// console.log(myVar);
