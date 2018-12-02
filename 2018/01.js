//get input from file
const fs = require("fs");
let input = fs
  .readFileSync("./01.txt")
  .toString()
  .split("\n");

// Quick Solution 1.1 with reduce
let output = input.reduce(
  (frequency2, element2) => frequency2 + Number(element2),
  0
);
console.log("Calibrated frequency:" + output);

//Solution 1.2
function getDoubleFrequency(input) {
  let frequency = 0;
  let frequencies = [];

  for (let i = 0; i < input.length; i++) {
    if (i === input.length - 1) i = 0;
    let currentNumber = Number(input[i]);
    frequency += currentNumber;
    if (frequencies.includes(frequency))
      return "First double frequency: " + frequency;
    frequencies.push(frequency);
  }
}

console.log(getDoubleFrequency(input));
