#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (const element of list) {
    if (element === searchElement) { occ++; }
  }
  return occ;
};
