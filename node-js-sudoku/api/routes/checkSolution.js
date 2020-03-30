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

  os = process.platform
  interpter = "python3"
  
  if(os == "win32"){
    interpter = "python.exe"
  }

  const pythonProcess = spawn(interpter, ["./api/routes/sudoku.py", initialGrid, attemptGrid]);

  pythonProcess.stdout.on("data", function(data) {
    
    console.log(data.toString());
    
    res.status(201).send(data);
    // res.end('end');
  });

});

module.exports = router;
