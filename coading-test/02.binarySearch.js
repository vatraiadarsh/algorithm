/**
 * 2.	Given a sorted array of integers, write a recursive function to perform binary search.
 *  (Binary search algorithm compares the search value with the middle element of the array.
 *  If they match, then return its index. Otherwise, if the search value is less than the middle element,
 *  then repeat the algorithm on the sub-array to the left of the middle element or, if the search value is greater,
 *  on the sub-array to the right. If the remaining array to be searched is empty,
 *  then the search value cannot be found and return -1.)
 */

function binarySearchRecursive(sortedArray, firstElementIndex, lastElementIndex, searchValue) {
    if (lastElementIndex < firstElementIndex) {
        return "Not found"; // or returns -1.
    } else {
        mid_point = firstElementIndex + (Math.floor((lastElementIndex - firstElementIndex) / 2));
        if (sortedArray[mid_point] > searchValue) {
            // recurse on left side
            return binarySearchRecursive(sortedArray, firstElementIndex, mid_point - 1, searchValue);
        } else if (sortedArray[mid_point] < searchValue) {
            // recurse on right side
            return binarySearchRecursive(sortedArray, mid_point + 1, lastElementIndex, searchValue);
        } else {
            return mid_point;
        }
    }
}
const testCases = [
  [],
  [-367, -99, 44, 55, 66, 77, 88, 100, 900],
  [45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
  [-1, 1, 1, 1, 2, 2, 3, 4, 5, 100],
  [-34, 5, 6, 7, 8, 9, 10, 21, 65, 432],
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
];


console.log(`Index of 60 is ${binarySearchRecursive(testCases[0], 0, testCases[0].length - 1, 60)}`);
console.log(`Index of 900 is ${binarySearchRecursive(testCases[1], 0, testCases[1].length - 1, 900)}`);
console.log(`Index of 69 is ${binarySearchRecursive(testCases[2], 0, testCases[2].length - 1, 69)}`)
console.log(`Index of 100 is ${binarySearchRecursive(testCases[3], 0, testCases[3].length - 1, 100)}`)
console.log(`Index of 432 is ${binarySearchRecursive(testCases[4], 0, testCases[4].length - 1, 432)}`)
console.log(`Index of 10 is ${binarySearchRecursive(testCases[5], 0, testCases[5].length - 1, 10)}`)
;

