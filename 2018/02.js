//get input from file
const fs = require("fs");
let input = fs
  .readFileSync("./02.txt")
  .toString()
  .split("\n");

let twoSum = 0;
let threeSum = 0;

for (let label of input) {
  var occurenceDict = {};
  label.replace(/\S/g, function(l) {
    occurenceDict[l] = isNaN(occurenceDict[l]) ? 1 : occurenceDict[l] + 1;
  });
  if (Object.values(occurenceDict).includes(2)) twoSum++;
  if (Object.values(occurenceDict).includes(3)) threeSum++;
}

console.log(twoSum, threeSum, twoSum * threeSum);
