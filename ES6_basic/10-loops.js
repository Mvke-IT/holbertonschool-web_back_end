export default function appendToEAchArrayValue(array, appendString) {
  const arr = [];
  for (const value of array) {
    arr.push(appendString + value);
  }
  return arr;
}
