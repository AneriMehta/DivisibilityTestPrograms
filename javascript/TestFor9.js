function isDivisibleBy9(n) {
  if (typeof n !== "number") {
    return false;
  }
  const x = n / 9;
  return parseInt(x * 9) === n;
}
