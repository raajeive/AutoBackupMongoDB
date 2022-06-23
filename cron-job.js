var cron = require("node-cron");
const { PythonShell } = require("python-shell");

console.log("Cron job scheduled");
cron.schedule("00 * * * *", () => {
  console.log("Cron job started");
  let options = {
    mode: "text",
    pythonPath: "/usr/bin/python2.7",
    pythonOptions: ["-u"], // get print results in real-time
    args: ["export"] // argument to the python file
  };
  PythonShell.run("DriveMongoDB.py", options, function(err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log("results: %j", results);
  });
});
