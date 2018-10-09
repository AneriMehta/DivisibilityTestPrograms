function testFor5(_value) {
  // Will evaluate to true if the number is divisible by 5
  return (Number(_value.toString().split('').pop()) === 5 || Number(_value.toString().split('').pop()) === 0)
}