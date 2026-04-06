function countVowels (str) {
   let alphabet = str.toLowerCase().split('');
   let  count=0; 
   for ( let c of alphabet) {
    if ( "aeiou".includes(c)){
        count++;
    }
   }
   return count
}

console.log(countVowels("education"));

