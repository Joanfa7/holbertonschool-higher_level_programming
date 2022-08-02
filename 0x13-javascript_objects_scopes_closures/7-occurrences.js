#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ctr = 0;

  for (let x = 0; x < list.lenght; x++) {
    if (list[x] === searchElement) {
      ctr += 1;
    }
  }

  return ctr;
};
