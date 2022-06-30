function binarySearch(sorted_array, target) {
    let start = 0;
    let end = sorted_array.length - 1; //(n-1)

    while (start <= end) {
        let mid = Math.floor(start + end) / 2;

        if (sorted_array[mid] === target) return mid;
        if (sorted_array[mid] < target) start = mid + 1;
        else start = mid - 1;
    }
    return "Not Found";
}

sorted_array = [2, 4, 5, 12, 43, 54, 60, 77];
console.log(binarySearch(sorted_array, 60));

sorted_array_string = ['aapple', 'abpple', 'cat', 'len', 'mon', 'tues'];
console.log(binarySearch(sorted_array_string, 'mon'))