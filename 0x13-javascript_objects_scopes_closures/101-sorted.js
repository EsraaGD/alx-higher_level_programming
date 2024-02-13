#!/usr/bin/node
const { dict } = require('./101-data');

const OccByUserDict = {};

for (const userId in dict) {
  const Occ = dict[userId];
  if (OccByUserDict[Occ] === undefined) {
    OccByUserDict[Occ] = [];
  }
  OccByUserDict[Occ].push(userId);
}

console.log(OccByUserDict);
