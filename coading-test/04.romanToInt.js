/**
 * 4.	Write a function that converts a Roman numeral to an integer. 
 * (ex: “I” = 1, “III” = 3, “IV” = 4, “V” = 5, “VI” = 6, “X” = 10, “L” = 50,  “LX” = 60, “XLIX” = 49, “C”= 100, “CIX” = 109,  “CLX” = 160, “D” = 500, “M” = 1000, “CDXLIV” = 444, “MCMIV” = 1904, …).  The input to the function is a String and the output is an int. (5 points)
 * Assume that the given Roman numeral is valid.
 * 
 */

function romanToInt(romanNumeral) {
  // create a hash table of the roman numerals
  const romanNumeralMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let result = 0;
  let previousValue = 0;
  let currentValue = 0;
  for (let i = romanNumeral.length - 1; i >= 0; i--) {
    currentValue = romanNumeralMap[romanNumeral[i]];
    if (currentValue < previousValue) {
      result -= currentValue;
    } else {
      result += currentValue;
    }
    previousValue = currentValue;
  }
  return result;
}

console.log(romanToInt("XLIV"));
console.log(romanToInt("CDXLIV"));
console.log(romanToInt("MCMXCIX"));
console.log(romanToInt("MCMLXXXIX"));
console.log(romanToInt("MCMLXXXIX"));
console.log(romanToInt("MCMLXXXIX"));
console.log(romanToInt("CCCCCMCCC"));
console.log(romanToInt("MMMMMMMM"));
