from Tkinter import *
import random

class BoardView:
    def __init__(self, boardState, viewOptions):
        self.boardState = boardState
        self.viewOptions = viewOptions

    def draw(self, canvas):
        cellSize = self.viewOptions.cellSize();
        for rowIndex in range(0, self.boardState.getNumRows()):
            for colIndex in range(0, self.boardState.getNumColumns()):
                cellX = (colIndex * cellSize) + self.viewOptions.boardLeftMargin()
                cellY = (rowIndex * cellSize) + self.viewOptions.boardTopMargin()
                cellXEnd = cellX + cellSize
                cellYEnd = cellY + cellSize
                cellColor = self.boardState.getCellColor(row=rowIndex, column=colIndex)
                canvas.create_rectangle(cellX,  cellY, cellXEnd, cellYEnd, fill=cellColor)
                print "Draw row:%d col:%d at x:%d y:%d with color:%s" % (rowIndex, colIndex, cellX, cellY, cellColor)

class ViewOptions:
    def __init__(self, numRows, numColumns):
        # For now, fix cell size and scale the rest
        self._cellSize = 10;
        # For now, fixed margin all around
        self._margin = 20;

        self._width = (2 * self._margin) + (numColumns * self._cellSize)
        self._height = (2 * self._margin) + (numRows * self._cellSize)

    def cellSize(self):
        return self._cellSize

    def boardLeftMargin(self):
        return self._margin;

    def boardRightMargin(self):
        return self._margin;

    def boardTopMargin(self):
        return self._margin;

    def boardBottonMargin(self):
        return self._margin;

    def width(self):
        return self._width

    def height(self):
        return self._height

class BoardState:
    def __init__(self, colors):
        # TODO: Validate colors
        self.colors = colors
        self.numRows = len(colors)
        self.numColumns = len(colors[0])

    def getNumRows(self):
        return self.numRows

    def getNumColumns(self):
        return self.numColumns

    def getCellColor(self, row, column):
        return self.colors[row][column]

def randomBoardState(numRows=20, numColumns=10):
    colors = ["red", "green", "blue"]
    rows = []
    for rowIndex in range(0, numRows):
        row = []
        for colIndex in range(0, numColumns):
            row.append(random.choice(colors))
        rows.append(row)
    return BoardState(rows)

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

rows = 20;
columns = 10;
viewOptions = ViewOptions(numRows=rows, numColumns=columns)
boardState = randomBoardState(numRows=rows, numColumns=columns);
boardView = BoardView(boardState, viewOptions)

master = Tk()
frame = Frame(master, width=viewOptions.width(), height=viewOptions.height())
canvas = Canvas(frame, width=viewOptions.width(), height=viewOptions.height())

frame.bind("<Key>", key)
canvas.bind("<Button-1>", callback)

frame.pack()
canvas.pack()

boardView.draw(canvas)

# mainloop()

canvas.delete(ALL)
