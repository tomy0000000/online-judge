/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  newArr = [];
  arr.forEach((n, i) => (fn(n, i) ? newArr.push(n) : null));
  return newArr;
};
