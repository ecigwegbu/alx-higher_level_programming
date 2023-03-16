#!/usr/bin/node
// number to given base converter

exports.converter = function (base) {
  if (!base) return function () {};
  return function (num) {
    return num.toString(base);
  };
};
