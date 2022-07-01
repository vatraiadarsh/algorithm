/**
 * 3.	Your friend has been kidnapped and you have received a ransom note.
 *  The note has been constructed by cutting out letters from a printed magazine.
 *  Due to the unusual font used, the police think they can find your friend if only they are sure which magazine the letters are from.
 *  Your job is to determine if the ransom note could have been constructed from the set of letters given by the police.
 *
 *  Write a function that takes in two Strings (‘note’ and ‘magazine’).
 *  Return true if the note could have been cut out from the magazine.
 *
 * Example 1) note = “ceba”; magazine = “abcde” returns true
 *  (the magazine has ≥ 1 ‘e’, ≥ 1 ‘c’, ≥ 1 ‘b’, ≥ 1 ‘a’ so the note could have been made by cutting characters out of the magazine);
 *
 * Example 2) note = “deaa”, magazine = “abcde” returns false
 * (the note has more ‘a’ characters than can be cut out of the magazine);
 *
 * Example 3) note = “aacc”, magazine = “bbccaa” returns true
 *
 *
 */

function ransomeNote(note, magazine) {
  let noteArr = note.split("");
  let magazineArr = magazine.split("");
  let magazineObj = {};
  // create a hash table of the magazine
  for (let i = 0; i < magazineArr.length; i++) {
    if (magazineObj[magazineArr[i]]) {
      magazineObj[magazineArr[i]]++;
    } else {
      magazineObj[magazineArr[i]] = 1;
    }
  }
  // check if the note can be made from the magazine
  for (let i = 0; i < noteArr.length; i++) {
    if (magazineObj[noteArr[i]]) {
      magazineObj[noteArr[i]]--;
    } else {
      return false;
    }
  }
  return true;
}

console.log(ransomeNote("ceba", "abcde"));
console.log(ransomeNote("deaa", "abcde"));
console.log(ransomeNote("aacc", "bbccaa"));