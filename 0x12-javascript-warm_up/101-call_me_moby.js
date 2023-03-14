#!/usr/bin/node
// function that runs x times from outside

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
