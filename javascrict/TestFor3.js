var n = Math.floor((Math.random() * 1000) + 1);
if (n) {
  var output = "";
  if (n % 3 == 0)
    output += "Divisible by 3";
  prompt(output || n);
}
