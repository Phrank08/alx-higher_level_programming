#!/usr/bin/node

let myVar;
const strInt = parseInt(process.argv[2]);
if (isNaN(strInt)) {
  myVar = 'Not a number';
} else {
  myVar = 'My number: ' + strInt;
}
console.log(myVar);