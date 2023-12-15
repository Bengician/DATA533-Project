# Question 2
```{r}
library(LearnBayes)
pi.func <- function(i) {
  out <- 0
  if (i > 0) 
    out <- 1 / (i + 1)^3
  out
}

N <- 20000
X <- numeric(N)
current.state <- 50 # initialize the Markov chain
for (n in 1:N) {
  i <- current.state
  P <- c(min(pi.func(i-2)/pi.func(i), 1),
         min(pi.func(i-1)/pi.func(i), 1),
         min(pi.func(i+1)/pi.func(i), 1),
         min(pi.func(i+2)/pi.func(i), 1))/6
  P0 <- 1 - sum(P)
  P <- c(P[1:2], P0, P[3:4])
  transition <- sample(seq(-2,2,1), size = 1, prob = P)
  current.state <- current.state + transition
  X[n] <- current.state
}

n <- 1000
observedDist <- table(X[-c(1:n)])
observedDist/(N-n)
k <- observedDist[2]/19000*27
k
```

# Question 5
```{r}
logNormExp <- function(sigma2, datapar) {
X <- datapar$data
lambda <- datapar$lambda
loglike <- dnorm(X, sd=sqrt(abs(sigma2)), log = TRUE)
logprior <- dexp(sigma2, rate = lambda, log = TRUE)
return(loglike + logprior)
}

data <- -25
start <- matrix(625, nrow=1)
datapar <- list(data=data, lambda=1/625)

m <- 10000
varcov <- matrix(1, nrow=1)
proposal <- list(var=varcov, scale = 50)

s <- rwmetrop(logNormExp, proposal, start, m, datapar)

par(mar=c(4, 4, 1, 1))
plot(density(s$par), main = " ")
rug(s$par)
```

# Question 6
## a)
```{r}
MoveProbs <- c(0, 1:6, 5:1)/36
P <- matrix(0, nrow=40, ncol=40)
for (i in 1:40) {
  P[i, ((i-1) + 1:12)%%40+1] <- MoveProbs
}
P[31,] <- rep(0, 40)
P[31, 11] <- 1
P[, 1:9]
```

## b)
```{r}
tP <- rbind(diag(40) - t(P), rep(1, 40))
RHS <- c(rep(0,40), 1)
PI <- qr.solve(tP, RHS)
names(PI) <- 1:40
barplot(PI)
```

## c)
```{r}
Revenue <- numeric(40)
Revenue[17] <- 950
Revenue[19] <- 950
Revenue[20] <- 1000
ERevenue <- sum(Revenue*PI)
ERevenue
```

## d)
```{r}
Cost <- numeric(40)
Cost[38] <- 1500
Cost[40] <- 2000
ECost <- sum(Cost*PI)
ECost
```

## e)
```{r}
VRevenue <- sum(Revenue^2*PI) - sum(Revenue*PI)^2
VCost <- sum(Cost^2*PI) - sum(Cost*PI)^2
VProfit <- VRevenue + VCost
SDProfit <- sqrt(VProfit)
SDProfit
```

## f)
```{r}
Revenue[22] <- 1050
Revenue[24] <- 1050
Revenue[25] <- 1100
Cost[32] <- 1275
Cost[33] <- 1275
Cost[35] <- 1400
ERevenue <- sum(Revenue*PI)
ECost <- sum(Cost*PI)
VRevenue <- sum(Revenue^2*PI) - sum(Revenue*PI)^2
VCost <- sum(Cost^2*PI) - sum(Cost*PI)^2
VProfit <- VRevenue + VCost
SDProfit <- sqrt(VProfit)
SDProfit
```

## g)
## Assumptions of c) and d)
```{r}
Revenue <- numeric(40)
Revenue[17] <- 950
Revenue[19] <- 950
Revenue[20] <- 1000
Cost <- numeric(40)
Cost[38] <- 1500
Cost[40] <- 2000

simulate_game <- function(P, Revenue, Cost) {
  cash_you <- 5000
  cash_opponent <- 5000

  while (cash_you > 0 && cash_opponent > 0) {
    state_you <- sample(1:40, 1, prob = PI)
    state_opponent <- sample(1:40, 1, prob = PI)
    
    cash_you <- cash_you + Revenue[state_you] - Cost[state_you]
    cash_opponent <- cash_opponent + Revenue[state_opponent] - Cost[state_opponent]
  }
  
  return(cash_you > 0)
}

num_simulations <- 1000
win_count <- sum(replicate(num_simulations, simulate_game(P, Revenue, Cost)))

probability_win <- win_count / num_simulations
probability_win

## Assumptions of f)
Revenue[22] <- 1050
Revenue[24] <- 1050
Revenue[25] <- 1100
Cost[32] <- 1275
Cost[33] <- 1275
Cost[35] <- 1400

simulate_game <- function(P, Revenue, Cost) {
  cash_you <- 5000
  cash_opponent <- 5000
  
  while (cash_you > 0 && cash_opponent > 0) {
    state_you <- sample(1:40, 1, prob = PI)
    state_opponent <- sample(1:40, 1, prob = PI)
    
    cash_you <- cash_you + Revenue[state_you] - Cost[state_you]
    cash_opponent <- cash_opponent + Revenue[state_opponent] - Cost[state_opponent]
  }
  
  return(cash_you > 0)
}

num_simulations <- 1000
win_count <- sum(replicate(num_simulations, simulate_game(P, Revenue, Cost)))

probability_win <- win_count / num_simulations
probability_win
```