= Table.AddColumn(#"Changed Type1", "Pie", each 
if [TransactionStatus] = "Completed" and [IsExpired] = "1" and [IsCancelled] = false 
    then "Expired gift cards"
else if [TransactionStatus] = "Failed" and [IsExpired] = "1" and [IsCancelled] = false
    then "Expired gift cards - failed transaction status"
else if [TransactionStatus] = "Completed" and [IsExpired] = "1" and [IsCancelled] = true
    then "Gift cards expired and cancelled - completed transaction status"
else if [TransactionStatus] = "Failed" and [IsExpired] = "1" and [IsCancelled] = true
    then "Gift cards expired and cancelled - failed transaction status"
else if [TransactionStatus] = "Completed" and [IsExpired] = "0" and [IsCancelled] = true
    then "Cancelled gift cards"
else if [TransactionStatus] = "Failed" and [IsExpired] = "0" and [IsCancelled] = false
    then "Failed transactions"
else if [TransactionStatus] = "Failed" and [IsExpired] = "0" and [IsCancelled] = true
    then "Failed transactions - gift card cancelled"
else null)