/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  newArr = [];
  arr.forEach((x, i) => newArr.push(fn(x, i)));
  return newArr;
};
