function countOccurrences(str, char) {
    let count = 0;
    let alphabet = str.toLowerCase().split('');
    for (let c of alphabet) {
        if (c === char.toLowerCase()) {
            count++;
        }
    }
    return count;
}

console.log(countOccurrences("HELLO WORLD", "l"));  // Output: 3

