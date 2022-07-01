/**
 *  1.	Write a function to check whether a given string is a palindrome without using any built-in functions.
    (A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.)
*/

class Stack {
    constructor() {
      this.count = 0;
      this.storage = {};
  
      this.pushToStack = function (value) {
        this.storage[this.count] = value;
        this.count++;
      };
  
      this.popFromStack = function (value) {
        if (value == 0) {
          return "Stack is Empty";
        }
        this.count--;
        let result = this.storage[this.count];
        delete this.storage[this.count];
        return result;
      };
  
      this.sizeOfStack = function () {
        return this.count;
      };
  
      this.removePunctuationAndWhiteSpaces = function (string) {
        if (typeof string === "number") {
          return string + "";
        } else {
          return string
            .replace(/[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]/g, "") // removes punctuation in a phrase
            .replace(/\s+/g, "") // removes whitespaces in a word/string or phrases.
            .toLowerCase();
        }
      };
    }
  }
  
  const testCases = [
    "A",
    "apple",
    "ccc",
    "aabaa",
    "Eva, can I see bees in a cave?",
    "The sower Arepo holds the wheels with effort.",
    "5'-GGATCC-3'",
    "3'- C T T A A G - 5'",
    2434623468237123,
    222.22,
    8998,
    "Nucleic Acid/DNA/Palindromic Sequencing",
  ];
  
  let container = new Stack();
  
  let string = container.removePunctuationAndWhiteSpaces(
    testCases[Math.floor(Math.random() * testCases.length)]
  );
  
  container.pushToStack(string);
  //  console.log(container);
  
  let reversedString = "";
  
  // adding letters to stack
  for (i = 0; i < string.length; i++) {
    container.pushToStack(string[i]);
  }
  
  // best case.
  if (container.sizeOfStack() == 1)
    return console.log(`${string} is a palindrome`);
  
  //   poping from stack in reverse order
  for (i = 0; i < string.length; i++) {
    reversedString += container.popFromStack();
  }
  
  string === reversedString
    ? console.log(`${string} is a palindrome`)
    : console.log(`${string} is not a palindrome`);
  