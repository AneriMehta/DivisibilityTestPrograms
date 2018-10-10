function isDivisibleBy9(n) {
  if (typeof n !== "number") {
    return false;
  }
  return n % 9 === 0;
}
