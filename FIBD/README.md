# Rosalind Challenge: FIBD (Mortal Fibonacci Rabbits)
This repository contains my solution to the **"FIBD"** problem from the [Rosalind bioinformatics challenge](https://rosalind.info/problems/fibd/).
This program extends the classical Fibonacci rabbit problem by introducing **mortality**. Unlike the standard recurrence where rabbits live forever, here each rabbit pair survives for only `m` months.

The task is to compute the total number of rabbit pairs alive after `n` months, given:
- `n` (number of months, ≤ 100)  
- `m` (lifespan in months, ≤ 20).  

This problem requires a **dynamic programming approach**, since we must track both reproduction and mortality to correctly simulate the rabbit population over time.