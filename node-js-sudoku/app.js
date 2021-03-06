const express = require("express");
const app = express();
const morgan = require("morgan");
const bodyParser = require("body-parser");

const checkSolutionRoute = require("./api/routes/checkSolution");
const solveGridRoute = require("./api/routes/solveGrid");
const generateGridRoute = require("./api/routes/generateGrid");

app.use(morgan("dev"));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept, Authorization"
  );
  if (req.method === "OPTIONS") {
    res.header("Access-Control-Allow-Methods", "POST, GET");
    return res.status(200).json({});
  }
  next();
});

// Routes which should handle requests
app.use("/checkSolution", checkSolutionRoute);
app.use("/solveGrid", solveGridRoute);
app.use("/generateGrid", generateGridRoute);

app.use((req, res, next) => {
  const error = new Error("Not found");
  error.status = 404;
  next(error);
});

app.use((error, req, res, next) => {
  res.status(error.status || 500);
  res.json({
    error: {
      message: error.message,
    },
  });
});

module.exports = app;
