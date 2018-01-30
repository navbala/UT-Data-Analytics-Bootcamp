Sub Stock_Stats()
    ' Set variable for Worksheet
    Dim ws As Worksheet
  
    ' Loop through all Worksheets
    For Each ws In Worksheets
  
        ' Set an initial variable for holding the stock ticker
        Dim Stock_Ticker As String

        ' Set an initial variable for holding the total volume per stock
        Dim Stock_Volume_Total As Double
        Stock_Volume_Total = 0
  
        ' Set the initial variable for holding the openning price
        Dim Open_Price As Double
        Open_Price = ws.Cells(2, 3).Value

        ' Set the initial variable for the closing price
        Dim Close_Price As Double
  
        ' Set the initial variable for yearly change
        Dim Yearly_Change As Double
  
        ' Set the inital variable for percent change
        Dim Percent_Change As Double

        ' Keep track of the location for each stock ticker in the summary table
        Dim Summary_Table_Row As Integer
        Summary_Table_Row = 2
  
        ' Set last row value for looping in initial data set
        Dim Last_Row As Double
        Last_Row = ws.Cells(Rows.Count, 1).End(xlUp).Row
  

        ' Loop through all stock prices/volumes for every stock ticker
        For i = 2 To Last_Row
    
            ' Check if we are still within the same stock ticker, if it is not...
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
            

                ' Set the stock ticker
                Stock_Ticker = ws.Cells(i, 1).Value
      
                ' Get the closing price
                Close_Price = ws.Cells(i, 6).Value
      
                ' Calculate the Yearly Change
                Yearly_Change = Close_Price - Open_Price
      
                ' Calculate the Percent Change
                Percent_Change = Yearly_Change / Open_Price

                ' Add to the Stock Volume Total
                Stock_Volume_Total = Stock_Volume_Total + ws.Cells(i, 7).Value

                ' Print the Stock Ticker in the Summary Table
                ws.Range("I" & Summary_Table_Row).Value = Stock_Ticker
      
                ' Print the Yearly Change in the Summary Table
                ws.Range("J" & Summary_Table_Row).Value = Yearly_Change
      
                ' Set the color index for Yearly Change values
                If ws.Range("J" & Summary_Table_Row).Value > 0 Then
                    ws.Range("J" & Summary_Table_Row).Interior.ColorIndex = 4
                Else
                    ws.Range("J" & Summary_Table_Row).Interior.ColorIndex = 3
                End If
      
                ' Print the Percent Change in the Summary Table
                ws.Range("K" & Summary_Table_Row).Value = Percent_Change

                ' Print the Stock Volume Total to the Summary Table
                ws.Range("L" & Summary_Table_Row).Value = Stock_Volume_Total

                ' Add one to the summary table row
                Summary_Table_Row = Summary_Table_Row + 1
      
                ' Get the new opening price for next stock ticker (only if it's a non-zero value)
                If ws.Cells(i + 1, 3).Value <> 0 Then
                    Open_Price = ws.Cells(i + 1, 3).Value
                End If
      
                ' Reset the Stock Volume Total
                Stock_Volume_Total = 0

            ' If the cell immediately following a row is the same Stock Ticker...
            Else

                ' Add to the Brand Total
                Stock_Volume_Total = Stock_Volume_Total + ws.Cells(i, 7).Value
                
                
                ' Set Open Price only if previous opening price values were 0
                If ws.Cells(i - 1, 3).Value = 0 And ws.Cells(i, 3).Value <> 0 Then
                    Open_Price = ws.Cells(i, 3).Value
                End If

            End If

        Next i

  Next ws

End Sub

