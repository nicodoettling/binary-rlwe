# Dependency graph T0

All imported claims retain their current consolidated versions and provisional boundaries. P0 v2 remains OPEN; A0 v3 remains BLOCKED. No graph is certified.

* SC0 v1 <- 
* B0 v1 <- SC0 v1, Y0 v1, X0 v2, N0 v2, U0 v2
* X0 v2 <- SC0 v1, Y0 v1
* N0 v2 <- SC0 v1, Y0 v1
* U0 v2 <- SC0 v1
* Y0 v1 <- 
* A2 v1 <- SC0 v1
* NC1 v2 <- 
* XG1 v1 <- 
* X1 v1 <- XG1 v1
* PR1 v1 <- 
* AN v2 <- A2 v1, NC1 v2, X1 v1, PR1 v1, U0 v2, Y0 v1
* P0 v2 <- A2 v1
* A0 v3 <- AN v2, B0 v1, P0 v2
* BSH v1 <- 
* BNG v1 <- N0 v2
* D0 v2 <- BSH v1, BNG v1
* NO1 v1 <- N0 v2
* DEC v1 <- 
* ATT v3 <- A2 v1
* UNIQ v1 <- A2 v1
* CHAR v2 <- A2 v1, NC1 v2
* KM v1 <- Y0 v1
* Pm v1 <- 
* MN v2 <- NC1 v2, A2 v1
* LEAK v1 <- A2 v1
* REC v1 <- 
* M0 v3 <- KM v1, MN v2, LEAK v1, Pm v1
* S0 v3 <- AN v2, B0 v1, REC v1, P0 v2
* W1 v1 <- A2 v1, P0 v2
* W2 v1 <- A2 v1, ATT v3, UNIQ v1, CHAR v2
* W3 v1 <- A2 v1, B0 v1, BNG v1
* T0-RESULT v1 <- W1 v1, W2 v1, W3 v1, A0 v3
