class mySet {
    constructor() {
        // this collection will hold the set
        let collection = [];

        // this methods will check for the presence of elements and returns true or false
        // The indexOf() method returns the position of the first occurrence of a specified value in a string.
        // This method returns -1 if the value to search for never occurs.

        this.has = function (element) {
            return (collection.indexOf(element) !== -1);
        }

        // this method will return all the values in the set
        this.values = function () {
            return collection;
        }

        // this method will add an element to the set

        this.add = function (element) {
            if (!this.has(element)) {
                collection.push(element)
                return true;
            }
            return false;
        }

        // this method will delete/remove an element from the set

        this.delete = function (element) {
            if (this.has(element)) {
                let index = collection.indexOf(element);
                collection.splice(index, 1) // we are going to take out 1 element.
                return true;
            }
            return false;
        }

        // this method will return the size of the collection

        this.size = function () {
            return collection.length;
        }

        // this method will return the union of two sets

        this.union = function (otherSet) {
            let unionSet = new mySet();
            let firstSet = this.values();
            let secondSet = otherSet.values();
            firstSet.forEach(function (e) {
                unionSet.add(e);
            });
            secondSet.forEach(function (e) {
                unionSet.add(e);
            });
            return unionSet;
        };

        // this method will return the intersection of the two sets

        this.intersection = function (otherSet) {
            let intersectionSet = new mySet();
            let firstSet = this.values();
            firstSet.forEach(function (e) {
                if (otherSet.has(e)) {
                    intersectionSet.add(e)
                }
            });
            return intersectionSet;
        }

        // this method will return the difference between 2 sets

        this.difference = function (otherSet) {
            let differenceSet = new mySet();
            let firstSet = this.values();
            firstSet.forEach(function (e) {
                if (!otherSet.has(e)) {
                    differenceSet.add(e)
                }
            });
            return differenceSet;

        }

        // this method will test if the set is the subset of the another set

        this.subset = function (otherSet) {
            let firstSet = this.values();
            return firstSet.every(function (value) {
                return otherSet.has(value);
            });

        }

    }

}
let setA = new mySet();
let setB = new mySet();

setA.add("a");
setB.add("b");
setB.add("c");
setB.add("a");
setB.add("d");
setB.add("f");

console.log(setA.subset(setB));

console.log(setA.intersection(setB).values());

console.log(setA.union(setB).values());

console.log(setA.union(setB).size());

console.log(setB.delete("f"));

console.log(setB.has("f"));

console.log(setB.difference(setA).values());