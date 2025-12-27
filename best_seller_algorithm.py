ALGORITHM FindBestSeller
    START
    INITIALIZE maxSales = 0
    INITIALIZE bestProduct = "None"
    INITIALIZE index = 0
    GET salesList

    WHILE (index < length of salesList) DO
        currentSales = salesList[index].sales
        
        IF (currentSales > maxSales) THEN
            maxSales = currentSales
            bestProduct = salesList[index].name
        ELSE
            // Keep existing max
            CONTINUE
        END IF
        
        INCREMENT index
    END WHILE

    PRINT "Best Seller: " + bestProduct
    END
