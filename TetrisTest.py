import unittest

from Tetris import *

class GridTest(unittest.TestCase):

    # def test_create(self):
    #     newGrid = Grid(3, 5)
    #     self.assertEqual(5, newGrid.height)
    #     self.assertEqual(3, newGrid.width)
    #     newGrid.createEmptyGrid()
    #     self.assertEqual(5*3, len(newGrid.gridCells))
    #     self.assertEqual(5, len(newGrid.leftBorderCells))
    #     self.assertEqual(0, len(newGrid.tetrominoCells))

        
    #       1 2 3 4 5  
    # 1                
    # 2       - -
    # 3       - -
    # 4
    # 5   
    # def test_fall1(self):
    #     self.fallingTestHelper(width = 6, height = 6, expected = 4)
    #     
        
    def rotate_T_shape(self):
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
        while newGrid.canMoveRight:
            newGrid.moveRight()
            print newGrid.prettyPrintGrid()
        newGrid.rotateRight()
        print newGrid.prettyPrintGrid()
        
        
        
    
    # def test_fall2():
    #     testTetromino = SquareTetromino()
    #     fallingTestHelper(width = 5, height = 5, x = 2, y = 2, testTetromino, 3)        
    # 
    def fallingTestHelper(self, width, height, expected):
        newGrid = Grid(width, height)
        newGrid.createEmptyGrid()
        newGrid.getNextTetromino()
        for i in range(expected):
            print i
            print newGrid.prettyPrintGrid()
            self.assertTrue(newGrid.canMoveDown())
            newGrid.moveDown()
        print newGrid.prettyPrintGrid()
        
        self.assertFalse(newGrid.isGameOver())
        newGrid.freezeTetromino()
        newGrid.getNextTetromino()
        print newGrid.prettyPrintGrid()
        for i in range(2):
            print i
            print newGrid.prettyPrintGrid()
            self.assertTrue(newGrid.canMoveDown())
            newGrid.moveDown()
            print newGrid.prettyPrintGrid()
        self.assertFalse(newGrid.canMoveDown())
        self.assertFalse(newGrid.isGameOver())
        newGrid.freezeTetromino()
        print newGrid.prettyPrintGrid()
        newGrid.getNextTetromino()
        print newGrid.prettyPrintGrid()
        self.assertFalse(newGrid.canMoveDown())
        self.assertTrue(newGrid.isGameOver())
        newGrid.freezeTetromino()
        print newGrid.prettyPrintGrid()
        
        
    #     
        
    #       1 2 3 4 5  
    # 1                
    # 2       - -
    # 3       - -
    # 4
    # 5
    # def test_moveSideways1():
    #     testTetromino = SquareTetromino()
    #     sidewaysTestHelper(width = 5, height = 5, x = 2, y = 2, testTetromino, 4, directions = ["right", "right", "left", "right", "left", "left", "left", "left"], lastdirection = "left")
    # 
    # def sidewaysTestHelper(width, height, x, y, testTetromino, expected, directions, lastdirection):
    #     newGrid = Grid(width, height)
    #     newGrid.placeTetromino(x, y, testTetromino)
    #     for i in range(expected):
    #         newGrid.debugDraw()
    #         self.assertTrue(newGrid.canMoveSideways(directions(i)))
    #         newGrid.moveSideway(directions(i))
    #     newGrid.debugDraw()
    #     self.assertFalse(newGrid.canMoveSideways(lastdirection))
    # 
    # 
    # #       1 2 3 4 5  
    # # 1                
    # # 2       - - - -
    # # 3       
    # # 4
    # # 5
    # def test_rotate1():
    #     testTetromino = BarTetromino()
    #     sidewaysTestHelper(width = 5, height = 5, x = 2, y = 2, testTetromino, 4, direction = "left")
    #     
    # #       1 2 3 4 5  
    # # 1                
    # # 2       - - - 
    # # 3         -
    # # 4
    # # 5
    # def test_rotate2():
    #     testTetromino = BarTetromino()
    #     sidewaysTestHelper(width = 5, height = 5, x = 2, y = 2, testTetromino, 4, direction = "right")
    #     
    # def rotateTestHelper(width, height, x, y, testTetromino, expected, direction):
    #     newGrid = Grid(width, height)
    #     newGrid.placeTetromino(x, y, testTetromino)
    #     self.assertTrue(newGrid.canRotate(direction))
    #     newGrid.moveRotate(direction)
    #     newGrid.debugDraw()
    #     
    #     
    # def test_gridUpdate1():
    #     pass
    #     
    # def gridUpdateHelper(width, height, blocks):
    #     newGrid = Grid(width, height)
    #     for block in blocks:
    #         newGrid.addBlock(block)
    #         newGrid.debugDraw()
    #     self.assertEqual(3, newGrid.refreshRows(block))
    #     


if __name__ == '__main__':
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
    while newGrid.canMoveLeft:
        newGrid.moveLeft()
        print newGrid.prettyPrintGrid()
    # newGrid.rotateRight()
    # print newGrid.prettyPrintGrid()
    unittest.main()