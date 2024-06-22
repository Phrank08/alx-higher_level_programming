#!/usr/bin/node

exports.logMe = function (item)
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
