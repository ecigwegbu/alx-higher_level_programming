#!/bin/node
// name = 'Ray'; // Or explictly: window.name = 'Ray';
var john = {
  name: 'John',
  greet: function(person) {
    console.log("Hi " + person + ", my name is " + this.name);
  }
};john.greet("Mark");
// => "Hi Mark, my name is Ray"
