function mergeSort(unsorted_array) {
  if (unsorted_array.length <= 1) return unsorted_array;

  let mid = Math.floor(unsorted_array.length / 2);
  //  recursive calls
  let left = mergeSort(unsorted_array.slice(0, mid));
  let right = mergeSort(unsorted_array.slice(mid));

  return merge(left, right);
}

const merge = (left, right) => {
  let sorted_array = [];


  while (left.length && right.length) {
    // inserting smallest items in sorted array
    if (left[0] < right[0]) sorted_array.push(left.shift());
    else sorted_array.push(right.shift());
  }

  return [...sorted_array, ...left, ...right];

}

unsorted_array_nums = [34, 15, 34, -345, -1, 100];
unsorted_array_strings = ['abpple', 'aapple', 'len', 'mon', 'tues', 'cat',]
unsorted_array_mixed = [...unsorted_array_nums, ...unsorted_array_strings]

console.log(mergeSort(unsorted_array_nums));
console.log(mergeSort(unsorted_array_strings));
console.log(mergeSort(unsorted_array_mixed));