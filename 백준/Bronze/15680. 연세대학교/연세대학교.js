const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (check) => {
  check = parseInt(check, 10);
  if (check === 0) {
    console.log("YONSEI");
  } else {
    console.log("Leading the Way to the Future");
  }
  rl.close();
});
