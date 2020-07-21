// functions: push, pop, peek,length

class Stack {
    constructor() {
        this.count = 0;
        this.storage = {};

        // adds a value to the end of the stack
        this.push = function (value) {
            this.storage[this.count] = value;
            this.count++;
        }

        // removes and return the value at the end of the stack
        this.pop = function (value) {
            if (value == 0) {
                return 'Stack is Empty';
            }
            this.count--;
            let result = this.storage[this.count];
            delete this.storage[this.count];
            return result;
        }

        // returns the value at the end of the stack
        this.peek = function () {
            return this.storage[this.count - 1];
        }

        this.size = function () {
            return this.count;
        }

    }


}

let stack = new Stack();

stack.push(20);
stack.push(27);
console.log(stack.peek());
console.log(stack.pop());
console.log(stack.peek());
stack.push('apple');
console.log(stack.peek());
console.log(stack.pop())
console.log(stack.peek());

// finding the palidrom word

let letters = []; // stack
let string = 'cccc';
let reversedString = '';

// put letters of string into the stack
for (i = 0; i < string.length; i++) {
    letters.push(string[i]);
    // console.log(letters);
}

// pop off stack in the reverse order
for (i = 0; i < string.length; i++) {
    reversedString += letters.pop();
    // console.log(reversedString);
}

if (string === reversedString) {
    console.log(`${string} is a palindrome word`)
} else {
    console.log(`${string} is not a palindrome word`)
}