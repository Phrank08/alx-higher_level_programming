#!/usr/bin/node
let myVar;

if (process.argv.length <= 2) {
  myVar = 'No argument';
} else if (process.argv.length === 3) {
  myVar = 'Aruments found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
