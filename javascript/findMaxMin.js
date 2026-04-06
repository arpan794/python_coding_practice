function maxMin (arr) {
    let max = arr[0];
    let min = arr[0];

    for ( i=0; i<= arr.length; i++){
        if ( arr[i] > max) {
               max = arr[i]
        }
        if ( arr[i] < min ) {
            min = arr[i]
        }
    }

    return {max,min}
}

let arr = [1,2,5,78,,98,4,9]
let result = maxMin(arr);
console.log("Max:",result.max,"Min:",result.min);
