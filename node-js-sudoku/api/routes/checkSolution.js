const express = require("express");
const router = express.Router();

const spawn = require("child_process").spawn;

router.get("/", (req, res, next) => {
  res.status(200).json({
    message: "Handling GET requests to /checksolution"
  });
});

router.post("/", (req, res, next) => {

  var initialGrid = JSON.stringify(req.body.grid.initialGrid);
  var attemptGrid = JSON.stringify(req.body.grid.attemptGrid);

  const pythonProcess = spawn("python.exe", ["./api/routes/sudoku.py", initialGrid, attemptGrid]);

  pythonProcess.stdout.on("data", function(data) {
    
    console.log(data.toString());
    
    res.status(201).write(data);
    res.end('end');
  });

});

module.exports = router;
