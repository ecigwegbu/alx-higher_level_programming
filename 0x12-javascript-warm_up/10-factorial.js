#!/usr/bin/node
// Add 2 integers

const a = parseInt(process.argv[2]);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  } else if (n < 0) {
    return (-1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(a));

/* int factorial(int n)
{
if (n == 0)
return (1);
else if (n < 0)
return (-1);
return (n * factorial(n - 1));
}
*/
