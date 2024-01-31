/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
  return (x) => {
    functions.reverse().forEach((f) => {
      x = f(x);
    });
    return x;
  };
};
