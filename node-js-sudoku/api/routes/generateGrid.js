const express = require("express");
const router = express.Router();

const spawn = require("child_process").spawn;

router.post("/", (req, res, next) => {
  res.status(200).json({
    message: "Handling POST requests to /solveGrid",
  });
});

router.get("/", (req, res, next) => {
  os = process.platform;
  interpter = "python3";

  if (os == "win32") {
    interpter = "python.exe";
  }

  const pythonProcess = spawn(interpter, ["./api/routes/sudoku.py"]);

  //10 sec upper limit
  res.setTimeout(10000, function () {
    console.log("Request has timed out. Couldnt Solve Grid");
    res.sendStatus(408);
  });

  pythonProcess.stdout.on("data", function (data) {
    console.log(data.toString());

    res.status(201).send(data);
    // res.end('end');
  });
});

module.exports = router;
