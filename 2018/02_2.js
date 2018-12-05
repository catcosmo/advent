//get input from file
const fs = require("fs");
let input = fs
  .readFileSync("./02.txt")
  .toString()
  .split("\n");

//find strings that differ by only one character
for (let label of input) {
  for (let compLabel of input) {
    let diffCount = 0;
    let ID = "";
    for (let i = 0; i < compLabel.length; i++) {
      if (diffCount > 1) continue;
      if (label[i] === compLabel[i]) ID += compLabel[i];
      else diffCount++;
    }
    if (diffCount === 1) console.log(ID);
  }
}
