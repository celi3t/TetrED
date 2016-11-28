import math


class bcolors:
    PINK = '\033[95m'
    PURPLE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Cell:
    
    emptyCellColor = bcolors.WHITE
    
    def __init__(self):
        self.cellBelow = None
        self.cellLeft = None
        self.cellRight = None
        self.cellAbove = None
        self.isFloor = False
        self.isBorderLeft = False
        # self.isBorderRight = False
        self.isOccupied = False
        self.isSpecialUpper = False  #Cell in the first two rows, hidden from public
        self.isTopRow = False
        self.color = Cell.emptyCellColor
        
    #SETTERS
    def setIsOccupied(self, color):
        self.isOccupied = True
        self.color = color
        
    def setIsFree(self):
        self.isOccupied = False
        self.color = Cell.emptyCellColor
        
    def setIsFloor(self):
        self.isFloor = True
        
    def setIsBorderLeft(self):
        self.isBorderLeft = True
    
    # def setIsBorderRight(self):
    #     self.isBorderRight = True
    
    def setIsTetrominoStart(self):
        self.isTetrominoStart = True
        
    def setIsSpecialUpper(self):
        self.isSpecialUpper = True
        
    def setIsTopRow(self):
        self.isTopRow = True
        
    def setColor(self, color):
        self.color = color
        
    def setCellBelow(self, cell):
        self.cellBelow = cell
        
    def setCellAbove(self, cell):
        self.cellAbove = cell

    def setCellLeft(self, cell):
        self.cellLeft = cell

    def setCellRight(self, cell):
        self.cellRight = cell
        
    
    #CHECKERS
    def isOccupied(self):
        return self.isOccupied
        
    def isOnRightBorder(self):
        return self.cellRight == None
        
    def isOnLeftBorder(self):
        return self.cellLeft == None
        
    def isFloor(self):
        self.cellBelow == None
        
    #GETTERS
    def getCellBelow(self):
        return self.cellBelow 
    
    def getCellLeft(self):
        return self.cellLeft 
    
    def getCellRight(self):
        return self.cellRight 
        
    def getCellAbove(self):
        return self.cellAbove
        
    def getColor(self):
        self.color
        
    #DEBUGGERS
    def prettyPrint(self):
        if self.isOccupied:
            string = self.color + "|+|" + bcolors.ENDC
        elif self.isSpecialUpper:
            string = self.color + "|-|" + bcolors.ENDC  
        else:
            string = self.color + "| |" + bcolors.ENDC
        return string
    
    def prettyPrintTetromino(self, tetrominocolor):
        string = tetrominocolor + "|*|" + bcolors.ENDC
        return string
         

class TetrominoBuilder:
    def __init__(self, buildingFunctions):
        self.instructions= buildingFunctions
        self.rotateRightBuilder = None
        self.rotateLeftBuilder = None
    
class TetrominoOConstants:    
    #For each shape, there are 4 states
    #for each state, you can move right or left and transition to a different state
    #Shapes start at state1 in the 2 upper rows
    #the "center" main cell is defined by the grid
    color = bcolors.YELLOW
    state1 = TetrominoBuilder([Cell.getCellRight, Cell.getCellBelow, Cell.getCellLeft])
    state2 = TetrominoBuilder([Cell.getCellRight, Cell.getCellBelow, Cell.getCellLeft])
    state3 = TetrominoBuilder([Cell.getCellRight, Cell.getCellBelow, Cell.getCellLeft])
    state4 = TetrominoBuilder([Cell.getCellRight, Cell.getCellBelow, Cell.getCellLeft])
    state1.rotateRightBuilder = state2
    state1.rotateLeftBuilder = state4
    state2.rotateRightBuilder = state1
    state2.rotateLeftBuilder = state3
    state3.rotateRightBuilder = state4
    state3.rotateLeftBuilder = state3
    state4.rotateRightBuilder = state3
    state4.rotateLeftBuilder = state1
    

class TetrominoTConstants:    
    #For each shape, there are 4 states
    #for each state, you can move right or left and transition to a different state
    #Shapes start at state1 in the 2 upper rows
    #the "center" main cell is defined by the grid
    color = bcolors.GREEN
    state1 = TetrominoBuilder([Cell.getCellLeft, Cell.getCellRight, Cell.getCellAbove, Cell.getCellBelow, Cell.getCellRight])
    state2 = TetrominoBuilder([Cell.getCellAbove, Cell.getCellBelow, Cell.getCellBelow, Cell.getCellAbove, Cell.getCellRight])
    state3 = TetrominoBuilder([Cell.getCellLeft, Cell.getCellRight, Cell.getCellBelow, Cell.getCellAbove, Cell.getCellRight])
    state4 = TetrominoBuilder([Cell.getCellAbove, Cell.getCellBelow, Cell.getCellBelow, Cell.getCellAbove, Cell.getCellLeft])
    state1.rotateRightBuilder = state2
    state1.rotateLeftBuilder = state4
    state2.rotateRightBuilder = state3
    state2.rotateLeftBuilder = state1
    state3.rotateRightBuilder = state4
    state3.rotateLeftBuilder = state2
    state4.rotateRightBuilder = state1
    state4.rotateLeftBuilder = state3
       


class Tetromino:
    
    def __init__(self):
        self.tetrominoShapes = ["O", "T"]
        self.buildFunctions = {}
        self.buildFunctions["O"] = TetrominoOConstants.state1
        self.buildFunctions["T"] = TetrominoTConstants.state1
        self.colors = {}
        self.colors["O"] = TetrominoOConstants.color
        self.colors["T"] = TetrominoTConstants.color
       
    # def sampleTetromino(self):
    #     self.nextShape = self.tetrominoShapes[1]
    
    def getTetrominoBuilderWithShape(self, shape):
        self.color = self.colors[shape]
        return self.buildFunctions[shape]
        
    def getNextTetrominoBuilder(self):
        self.color = self.colors["T"]
        return self.buildFunctions["T"]
        



class Grid:
    #Initialize an empty grid without any cells, empty or full
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gridCells = []
        self.originCell = []
        self.tetrominoOriginCell = None
        self.tetrominoBuilder = None
        self.leftBorderCells = []  
        self.tetrominoCells = []
        self.upperCorner = []
        self.tetromino = None  # color, shape, etc   
        
    #for debugging I guess
    def getTetrominoWithShape(self, shape):
        self.tetromino = Tetromino()
        self.tetrominoOriginCell = self.originCell[0]
        nextCell = self.originCell[0]
        self.tetrominoCells.append(nextCell)
        self.tetrominoBuilder = self.tetromino.getTetrominoBuilderWithShape(shape)
        for r in self.tetrominoBuilder.instructions:
            nextCell = r(nextCell)
            self.tetrominoCells.append(nextCell)
        
        
    #Initialize a new tetromino
    def getNextTetromino(self):
        self.tetromino = Tetromino()
        self.tetrominoOriginCell = self.originCell[0]
        nextCell = self.originCell[0]
        self.tetrominoCells.append(nextCell)
        self.tetrominoBuilder = self.tetromino.getNextTetrominoBuilder()
        for r in self.tetrominoBuilder.instructions:
            nextCell = r(nextCell)
            if nextCell is not None:
                self.tetrominoCells.append(nextCell)
          
                
    def rotateLeft(self):
        newTetrominoCells = []
        tetrominoRotateBuilder = self.tetrominoBuilder.rotateLeftBuilder
        nextCell = self.originCell[0]
        newTetrominoCells.append(nextCell)
        for r in tetrominoRotateBuilder.instructions:
            nextCell = r(nextCell)
            if nextCell is not None:
                newTetrominoCells.append(nextCell)
        if len(newTetrominoCells) == len(self.tetrominoCells):
            self.tetrominoCells = newTetrominoCells
            self.tetrominoBuilder = tetrominoRotateBuilder
            
            
    def rotateRight(self):
        newTetrominoCells = []
        tetrominoRotateBuilder = self.tetrominoBuilder.rotateRightBuilder
        nextCell = self.originCell[0]
        newTetrominoCells.append(nextCell)
        for r in tetrominoRotateBuilder.instructions:
            nextCell = r(nextCell)
            if nextCell is not None:
                newTetrominoCells.append(nextCell)
        if len(newTetrominoCells) == len(self.tetrominoCells):
            self.tetrominoCells = newTetrominoCells
            self.tetrominoBuilder = tetrominoRotateBuilder
            
    
    def getFullRowsLeftMostCells(self):
        fullRows = ()
        for leftMostCell in self.leftBorderCells:
            if self.isRowFull(leftMostCell):
                fullRows.append(leftMostCell)
        return fullRows
    
    #Checks if row is full
    def isRowFull(self, startCell):
        if startCell.isOccupied():
            nextCell = startCell.getCellRight()
            while nextCell is not None:
                if nextCell.isOccupied():
                    nextCell = nextCell.getCellRight()
                else:
                    return False
            return True
        else:
            return False
    
    #Shifts down one row
    #I don't have to worry about the tetromino cell list, because thi action happens after the grid freezes and the list containing the tetromino cells in empty
    #for each cell in the full row, get the color and the isOccupied status of the above cell
    #if there is no above cell, then set a new free cell
    def refreshColumn(self, startingCell):
        aboveCell = startingCell.getCellAbove
        currentCell = startingCell
        while aboveCell is not None:
            currentCell.color = aboveCell.color
            currentCell.isOccupied = aboveCell.isOccupied
            currentCell = aboveCell
            aboveCell = aboveCell.getCellAbove
        currentCell.setIsFree         
    
    def refreshGrid(self, fullRowsLeftMostCells):
        for leftMostCell in fullRowsLeftMostCells:
            cell = leftMostCell
            while cell is not None:
                refreshColumn(self, cell)
                cell = cell.getCellRight
        
    #CHECKS IF IT"S OK TO MOVE
    def canMoveDown(self):
        for tetrominoCell in self.tetrominoCells:
            if tetrominoCell.isFloor:
                return False
            if tetrominoCell.cellBelow.isOccupied():
                return False
        return True
        
    def canMoveLeft(self):
        for tetrominoCell in self.tetrominoCells:
            print tetrominoCell.cellLeft
            if tetrominoCell.isOnLeftBorder():
                return False
            if tetrominoCell.cellLeft.isOccupied:
                return False
        return True
        
    def canMoveRight(self):
        for tetrominoCell in self.tetrominoCells:
            if tetrominoCell.isOnRightBorder():
                print "on border"
                return False
            if tetrominoCell.cellRight.isOccupied:
                return False
        return True
        
    def isGameOver(self):
        for t in self.tetrominoCells:
            if t.isSpecialUpper:
                return True
        return False
        
    #MOVES
    def moveDown(self):    
        self.tetrominoCells = [t.cellBelow for t in self.tetrominoCells]
        self.tetrominoOriginCell = self.tetrominoOriginCell.cellBelow
        
    def moveRight(self):    
        self.tetrominoCells = [t.cellRight for t in self.tetrominoCells]
        self.tetrominoOriginCell = self.tetrominoOriginCell.cellRight
        
    def moveLeft(self):    
        self.tetrominoCells = [t.cellLeft for t in self.tetrominoCells]
        self.tetrominoOriginCell = self.tetrominoOriginCell.cellLeft
        
    #Tetromino becomes part of the grid
    def freezeTetromino(self):
        [t.setIsOccupied(self.tetromino.color) for t in self.tetrominoCells]
        self.tetrominoCells = []
        self.tetrominoOriginCell = None
        self.tetrominoBuilder = None
        
    
    #populates the grid with actual cells    
    def createEmptyGrid(self):
        allCells = {}
        tetrominoStartsX = math.ceil(self.width / 2) - 1
        # try:
        #     assert(tetrominoStartsX >= 0)
        #     assert(self.width >= 5)
        #     assert(self.height >= 3)  
        # except:
        #     print "Invalid grid coordinates: width must be > 4 and height > 2"
        #     raise
        for x in range(self.width):
            for y in range(self.height):
                newCell = Cell()
                allCells[(x, y)] = newCell
                allCells[(x, y)].setIsFree()
                if x == 0:
                    allCells[(x, y)].setIsBorderLeft()
                    self.leftBorderCells.append(allCells[(x, y)])
                # if x == self.width - 1:
                #     allCells[(x, y)].setIsBorderRight()
                if y == 0:
                    allCells[(x, y)].setIsFloor()
                if y >= self.height-2:
                    allCells[(x, y)].setIsSpecialUpper()
                if y >= self.height-1:
                    allCells[(x, y)].setIsTopRow()
                if x == tetrominoStartsX and y == (self.height - 2):
                    allCells[(x, y)].setIsTetrominoStart()
                    self.originCell.append(allCells[(x, y)])
                if x == 0 and y == (self.height - 1):
                    self.upperCorner.append(allCells[(x, y)])
                    
        self.leftBorderCells.reverse()

        for coordinates, cell in allCells.iteritems():
            
            belowCoordinates = (coordinates[0], coordinates[1] - 1)
            if belowCoordinates in allCells:
                cell.setCellBelow(allCells[belowCoordinates])
                
            aboveCoordinates = (coordinates[0], coordinates[1] + 1)
            if aboveCoordinates in allCells:
                cell.setCellAbove(allCells[aboveCoordinates])
                
            leftCoordinates = (coordinates[0] - 1, coordinates[1])
            if leftCoordinates in allCells:
                cell.setCellLeft(allCells[leftCoordinates])
                
            rightCoordinates = (coordinates[0] + 1, coordinates[1])
            if rightCoordinates in allCells:
                cell.setCellRight(allCells[rightCoordinates])
                
            self.gridCells.append(cell)
            
            
            
    def prettyPrintGrid(self):
        string = "\n"
        for leftMostCell in self.leftBorderCells:
            currCell = leftMostCell
            while currCell != None:
                if currCell in self.tetrominoCells:
                    string += currCell.prettyPrintTetromino(self.tetromino.color)
                else:
                    string += currCell.prettyPrint()
                currCell = currCell.cellRight
            string += "\n"
        print string
            
            
    

if __name__ == "__main__":
    newGrid = Grid(6, 6)
    newGrid.createEmptyGrid()
    print newGrid.prettyPrintGrid()
    newGrid.getTetrominoWithShape("T")
    for i in range(4):
        print i
        print newGrid.prettyPrintGrid()
        newGrid.rotateRight()
        print newGrid.prettyPrintGrid()
        newGrid.rotateRight()
        print newGrid.prettyPrintGrid()
        newGrid.rotateLeft()
    print newGrid.prettyPrintGrid()
    while newGrid.canMoveLeft():
        newGrid.moveLeft()
        print newGrid.prettyPrintGrid()
    
    
    
    # g = Grid(13,8)
    # g.createEmptyGrid()    
    # 
    # mg = Grid(4,4)
    # mg.createEmptyGrid()
    # tetro = Tetromino()
    #tetro.nextTetromino(mg.originCell)
    