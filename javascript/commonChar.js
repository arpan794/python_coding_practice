function mostCommonChar(str) {
    const charMap = new Map();
    let maxChar = '';
    let maxCount = 0;

    // Normalize the string
    str = str.toLowerCase().replace(/\s/g, '');

    for (let char of str) {
        const count = (charMap.get(char) || 0) + 1;
        charMap.set(char, count);

        if (count > maxCount) {
            maxCount = count;
            maxChar = char;
        }
    }

    return { character: maxChar, count: maxCount };
}

// Example usage
const input = "Hello World";
const result = mostCommonChar(input);
console.log(`The most common character is '${result.character}' and it appears ${result.count} times.`);
