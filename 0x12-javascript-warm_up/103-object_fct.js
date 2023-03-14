#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// my code below
// data["PropertyD"] = 4;
// myObject.incr = '[Function]';
myObject.incr = function () {
  this.value++;
};
// mycode above
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
