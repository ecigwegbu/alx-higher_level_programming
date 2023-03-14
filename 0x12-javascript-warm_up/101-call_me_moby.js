#!/usr/bin/node
// function add that is visible fom the outside

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
