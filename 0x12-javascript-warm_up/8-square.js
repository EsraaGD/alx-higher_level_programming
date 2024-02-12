#!/usr/bin/node
const sq = parseInt(process.argv[2]);
if (isNaN(sq)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sq; i++) {
    console.log('X'.repeat(sq));
  }
}
