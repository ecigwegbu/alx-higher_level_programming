#!/usr/bin/node
// return the reversed version of a list

exports.esrever = function (list) {
  if (!list) return;

  const listReversed = [];
  const len = list.length;

  for (let i = 0; i < len; i++) {
    listReversed[i] = list[len - 1 - i];
  }

  return (listReversed);
};
