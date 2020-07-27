class PriorityQueue {
    constructor() {
        let collection = [];

        this.printCollection = function () {
            console.log(collection);
        }

        this.isEmpty = function () {
            return (collection.length === 0);
        }

        this.enqueue = function (element) {
            if (this.isEmpty()) {
                collection.push(element) // if the queue is empty just push the element without caring priority.
            } else {
                let added = false;
                // pq.enqueue(['rails', 4]);
                for (let i = 0; i < collection.length; i++) {
                    if (element[1] < collection[i][1]) { // checking priority && element[i] is index and element[1] is the priority
                        collection.splice(i, 0, element);
                        added = true;
                        break;
                    }
                }
                if (!added) {
                    collection.push(element);
                }
            }

        }

        this.dequque = function () {
            let value = collection.shift();
            return value[0];
        }

        this.front = function () {
            return collection[0];
        }

        this.size = function () {
            return collection.length;
        }

    }


}

let pq = new PriorityQueue();
pq.enqueue(['rails', 4]);
pq.enqueue(['python', 12]);
pq.enqueue(['java', 3]);
pq.enqueue(['javascript', 1]);
pq.enqueue(['dart', 4])

pq.printCollection();

console.log(pq.dequque());

pq.printCollection();

console.log(pq.front());