import 'dart:io';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:google_fonts/google_fonts.dart';

void main() => runApp(Main());

class Main extends StatefulWidget {
  @override
  _MainState createState() => _MainState();
}

class _MainState extends State<Main> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Sudoku",
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.amberAccent[100],
        body: SafeArea(
          child: Home(),
        ),
      ),
    );
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
//  0 represents empty space
  List<List<int>> sudokuGrid;

  @override
  void initState() {
    super.initState();

    sudokuGrid = [
      [0, 5, 0, 6, 3, 2, 9, 4, 1],
      [0, 0, 4, 0, 0, 0, 3, 0, 0],
      [9, 2, 3, 0, 0, 0, 0, 0, 8],
      [0, 9, 0, 3, 2, 4, 0, 0, 0],
      [0, 0, 5, 0, 0, 0, 8, 0, 0],
      [0, 0, 0, 8, 5, 6, 0, 9, 0],
      [3, 0, 0, 0, 0, 0, 6, 8, 9],
      [0, 0, 6, 0, 0, 0, 4, 0, 0],
      [4, 8, 9, 2, 6, 1, 0, 7, 0],
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: <Widget>[
          Text(
            "Sudoku",
            style: GoogleFonts.meriendaOne(fontSize: 50, color: Colors.purple[700]),
          ),
          Card(
            elevation: 15,
            color: Colors.transparent,
            child: Container(
              height: MediaQuery.of(context).size.width,
              width: MediaQuery.of(context).size.width,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.all(Radius.circular(25)),
                color: Colors.deepOrangeAccent[100],
              ),
              child: getSudokuGrid(),
            ),
          ),
          SizedBox(
            height: MediaQuery.of(context).size.height * 0.01,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              Card(
                elevation: 4,
                color: Colors.pink[200],
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
                child: MaterialButton(
                  onPressed: () {
                    print("Resetting");
                    setState(() {
                      sudokuGrid = [
                        [0, 5, 0, 6, 3, 2, 9, 4, 1],
                        [0, 0, 4, 0, 0, 0, 3, 0, 0],
                        [9, 2, 3, 0, 0, 0, 0, 0, 8],
                        [0, 9, 0, 3, 2, 4, 0, 0, 0],
                        [0, 0, 5, 0, 0, 0, 8, 0, 0],
                        [0, 0, 0, 8, 5, 6, 0, 9, 0],
                        [3, 0, 0, 0, 0, 0, 6, 8, 9],
                        [0, 0, 6, 0, 0, 0, 4, 0, 0],
                        [4, 8, 9, 2, 6, 1, 0, 7, 0],
                      ];
                    });
                  },
                  child: Text("Reset"),
                ),
              ),
              Card(
                elevation: 4,
                color: Colors.pink[200],
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
                child: MaterialButton(
                  onPressed: () {
                    Scaffold.of(context).showSnackBar(
                      SnackBar(
                        content: Text("Under Implementation"),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.all(Radius.circular(10)),
                        ),
                      ),
                    );
                  },
                  child: Text("Check Solution"),
                ),
              ),
              Card(
                elevation: 4,
                color: Colors.pink[200],
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
                child: MaterialButton(
                  onPressed: () {
                    Scaffold.of(context).showSnackBar(
                      SnackBar(
                        content: Text("Under Implementation"),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(10))),
                      ),
                    );
                  },
                  child: Text("Auto-Solve"),
                ),
              ),
            ],
          )
        ],
      ),
    );
  }

  Widget getSudokuGrid() {
    List<TableRow> tableRows = [];
    for (int i = 0; i < sudokuGrid.length; i += 3) {
      List<Widget> rows = [];
      for (int j = 0; j < sudokuGrid.length; j += 3) {
        rows.add(getTable(sudokuGrid.sublist(i, i + 3).map((e) => e.sublist(j, j + 3)).toList(),
            [j == 0, i == 0, j == sudokuGrid.length - 3, i == sudokuGrid.length - 3], i, j));
      }
      tableRows.add(TableRow(children: rows));
    }
    return Table(
      children: tableRows,
    );
  }

  Widget getTable(List<List<int>> grid, List<bool> borders, int iBig, int jBig) {
    List<TableRow> tableRows = [];
    for (int i = 0; i < grid.length; i++) {
      List<Widget> rowWidgets = [];
      for (int j = 0; j < grid[0].length; j++) {
        rowWidgets.add(
          Container(
            width: MediaQuery.of(context).size.width / 9.5,
            height: MediaQuery.of(context).size.width / 9,
            child: MaterialButton(
              onPressed: () async {
                int newNum = await showModalBottomSheet(
                    context: context,
                    backgroundColor: Colors.transparent,
                    builder: (context) {
                      int x = 0;
                      return Container(
                        height: MediaQuery.of(context).size.height * 0.28,
                        decoration: BoxDecoration(
                          color: Colors.black54,
                          borderRadius: BorderRadius.only(
                            topLeft: Radius.circular(20),
                            topRight: Radius.circular(20),
                          ),
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: <Widget>[
                            Container(
                              height: MediaQuery.of(context).size.height * 0.2,
                              child: CupertinoPicker(
                                itemExtent: MediaQuery.of(context).size.height * 0.048,
                                onSelectedItemChanged: (i) {
                                  x = i;
                                },
                                children: List<int>.generate(10, (i) => i + 1).map((e) {
                                  e -= 1;
                                  return Text(
                                    e != 0 ? "$e" : "- -",
                                    style: TextStyle(fontSize: 35, color: Colors.white),
                                  );
                                }).toList(),
                              ),
                            ),
                            MaterialButton(
                              onPressed: () {
                                Navigator.of(context).pop(x);
                              },
                              child: Text(
                                "Submit",
                                style: TextStyle(
                                  fontSize: 15,
                                  color: Colors.blue,
                                ),
                              ),
                            ),
                          ],
                        ),
                      );
                    });
                if (newNum != null)
                  setState(() {
                    print("Updating sudikuGrid[${iBig + i}][${j + jBig}] to $newNum");
                    sudokuGrid[iBig + i][jBig + j] = newNum;
                  });
              },
              child: Text(
                grid[i][j] != 0 ? "${grid[i][j]}" : "",
                style: TextStyle(
                  fontSize: 20,
                ),
              ),
            ),
          ),
        );
      }
      tableRows.add(
        TableRow(
          children: rowWidgets,
        ),
      );
    }
    double insideOpacity = 0.1;
    double outerOpacity = 0.6;
    return Table(
      children: tableRows,
      border: TableBorder(
        left: BorderSide(
          width: 2,
          color: Colors.deepOrangeAccent[400].withOpacity(borders[0] ? 0 : outerOpacity),
        ),
        top: BorderSide(
          width: 2,
          color: Colors.deepOrangeAccent[400].withOpacity(borders[1] ? 0 : outerOpacity),
        ),
        right: BorderSide(
          width: 2,
          color: Colors.deepOrangeAccent[400].withOpacity(borders[2] ? 0 : outerOpacity),
        ),
        bottom: BorderSide(
          width: 2,
          color: Colors.deepOrangeAccent[400].withOpacity(borders[3] ? 0 : outerOpacity),
        ),
        horizontalInside: BorderSide(
          width: 2,
          color: Colors.deepOrangeAccent[400].withOpacity(insideOpacity),
        ),
        verticalInside: BorderSide(
          width: 2,
          color: Colors.deepOrangeAccent[400].withOpacity(insideOpacity),
        ),
      ),
    );
  }
}
