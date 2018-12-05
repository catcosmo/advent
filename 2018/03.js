// get input from file
const fs = require("fs");
let input = fs
  .readFileSync("./03.txt")
  .toString()
  .split("#");

// delete useless first element
input.splice(0, 1);

// fill fabric
let fabric = [];
let fabricRow = [];
for (let i = 0; i < 1000; i++) fabricRow.push(-1);
for (let j = 0; j < 1000; j++) fabric.push(fabricRow);

// calculate overlapping
let overlapping = 0;
for (let claim of input) {
  // extract numbers from claim-string to clean list
  let claimNums = claim.match(/\d+/g).map(Number);
  // add overlapping inches from this claim
  overlapping += claimFabric(fabric, claimNums);
}

function claimFabric(fabric, claim) {
  let overlapping = 0;
  // fill claim to fabric
  // claim = [elveID, leftGap, topGap, length, width]
  for (let i = claim[1]; i <= claim[1] + claim[3]; i++) {
    for (let j = claim[2]; j <= claim[2] + claim[4]; j++) {
      //check if double claimed -> dont count
      if (fabric[i][j] === -2) continue;
      //check if free -> claim for that elf
      else if (fabric[i][j] === -1) fabric[i][j] = claim[0];
      //when already taken once, overwrite and set to double-claimed
      else if (fabric[i][j] > 0) {
        overlapping++;
        fabric[i][j] = -2;
      }
    }
  }
  return overlapping;
}

console.log(overlapping);
console.log(fabric[500][2]);
