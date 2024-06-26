# My Solution to Excercise 1

To replicate the solutions I provide it is sufficient to run the code 
```console
example@example:~$PATH-TO-MEV_AGENT/mev_agent/exercises/first$ python3 maximize_surplus.py input.json
```
Where `input.json` is one of the three inputs provided.

In this case the keyword `partial_fill = false` in all the user orders, thus we are in a *Fly-or-kill* situation.


In the following, I report the solutions I obtained employing my protocol and my program.

### First input
```console
luca@lime:~/programmi/mev_agent/exercises/first$ python3 maximize_surplus.py input1.json 
 
MEV Agent ready to maximize the surplus .. or at least trying :)
 
Status: 0
Message: Optimization terminated successfully
Number of Iterations: 2
Number of Function Evaluations: 4
Number of Gradient Evaluations: 2
 
 
The resulting total value sold   (via all paths) is: 1000.000000000000000000
The resulting total value bought (via all paths) is: 909.090909090909121915
The resulting gamma is: 9.090909090909121915
Total coin conservation error: 2.2737368e-13
 
The resulting total value sold via   AMM_RHO_KAPPA is: 1000.000000000000000000
The resulting total value bought via AMM_RHO_KAPPA is: 909.090909090909121915

```

With resulting JSON-file
```json
{
    "venues": {
        "AMM_RHO_KAPPA": {
            "sell_token": "KAPPA",
            "buy_token": "RHO",
            "ex_buy_amount": "1000_000000000000000000",
            "ex_sell_amount": "909_090909090909121915"
        }
    },
    "orders": {
        "0": {
            "partial_fill": false,
            "buy_amount": "900_000000000000000000",
            "sell_amount": "1000_000000000000000000",
            "buy_token": "KAPPA",
            "sell_token": "RHO",
            "ex_buy_amount": "909_090909090909121915",
            "ex_sell_amount": "1000_000000000000000000"
        }
    }
}
```
```
The surplus generated is 9_090909090909121915
```


<div align="center">
  <img src="https://github.com/nicoli-luca/mev_agent/blob/main/docs/images/graph_1_ex1.png" alt="Diagram" width="60%" height="60%">
  <p style="margin-top: 10px;">Strategy graph of the first input.</p>
</div>

### Second Input
```console
luca@lime:~/programmi/mev_agent/exercises/first$ python3 maximize_surplus.py input2.json 

MEV Agent ready to maximize the surplus .. or at least trying :)
 
Status: 0
Message: Optimization terminated successfully
Number of Iterations: 2
Number of Function Evaluations: 4
Number of Gradient Evaluations: 2
 
 
The resulting total value sold   (via all paths) is: 1000.000000000000000000
The resulting total value bought (via all paths) is: 1081.081081081081038064
The resulting gamma is: 181.081081081081038064
Total coin conservation error: 2.2737368e-13
 
The resulting total value sold via   AMM_TAU_PI -> AMM_PI_PSI is: 1000.000000000000000000
The resulting total value bought via AMM_TAU_PI -> AMM_PI_PSI is: 1081.08108108108103
```
With resulting JSON-file
```json
{
    "venues": {
        "AMM_TAU_PI": {
            "sell_token": "PI",
            "buy_token": "TAU",
            "ex_buy_amount": "1000_000000000000000000",
            "ex_sell_amount": "1818_181818181818243829"
        },
        "AMM_PI_PSI": {
            "sell_token": "PSI",
            "buy_token": "PI",
            "ex_buy_amount": "1818_181818181818243829",
            "ex_sell_amount": "1081_081081081081038064"
        }
    },
    "orders": {
        "0": {
            "partial_fill": false,
            "buy_amount": "900_000000000000000000",
            "sell_amount": "1000_000000000000000000",
            "buy_token": "PSI",
            "sell_token": "TAU",
            "ex_buy_amount": "1081_081081081081038064",
            "ex_sell_amount": "1000_000000000000000000"
        }
    }
}
```
```
The surplus generated is 181_081081081081038064
```
<div align="center">
  <img src="https://github.com/nicoli-luca/mev_agent/blob/main/docs/images/graph_2_ex1.png" alt="Diagram" width="60%" height="60%">
  <p style="margin-top: 10px;">Strategy graph of the secon input.</p>
</div>

### Third input
```console
luca@lime:~/programmi/mev_agent/exercises/first$ python3 maximize_surplus.py input3.json 
 
MEV Agent ready to maximize the surplus .. or at least trying :)
 
Status: 0
Message: Optimization terminated successfully
Number of Iterations: 15
Number of Function Evaluations: 60
Number of Gradient Evaluations: 15
 
 
The resulting total value sold   (via all paths) is: 1000.000000000043769433
The resulting total value bought (via all paths) is: 1301.146505249568235740
The resulting gamma is: 401.146505249528900094
Total coin conservation error: 1.7053026e-13
 
The resulting total value sold via   AMM_MU_IOTA -> AMM_IOTA_NU is: 289.078084376014658119
The resulting total value bought via AMM_MU_IOTA -> AMM_IOTA_NU is: 357.725105722187663559
 
The resulting total value sold via   AMM_MU_RHO -> AMM_RHO_NU is: 0.000000000000000000
The resulting total value bought via AMM_MU_RHO -> AMM_RHO_NU is: 0.000000000000000000
 
The resulting total value sold via   AMM_MU_CHI -> AMM_CHI_NU is: 710.921915624029111314
The resulting total value bought via AMM_MU_CHI -> AMM_CHI_NU is: 943.421399527380685868
```

With resulting JSON-file:
```json
{
    "venues": {
        "AMM_MU_IOTA": {
            "sell_token": "IOTA",
            "buy_token": "MU",
            "ex_buy_amount": "289_078084376014658119",
            "ex_sell_amount": "561_912509566780840942"
        },
        "AMM_MU_RHO": {
            "sell_token": "RHO",
            "buy_token": "MU",
            "ex_buy_amount": "0_000000000000000000",
            "ex_sell_amount": "0_000000000000000000"
        },
        "AMM_MU_CHI": {
            "sell_token": "CHI",
            "buy_token": "MU",
            "ex_buy_amount": "710_921915624029111314",
            "ex_sell_amount": "671_160049925420935324"
        },
        "AMM_IOTA_NU": {
            "sell_token": "NU",
            "buy_token": "IOTA",
            "ex_buy_amount": "561_912509566780840942",
            "ex_sell_amount": "357_725105722187663559"
        },
        "AMM_RHO_NU": {
            "sell_token": "NU",
            "buy_token": "RHO",
            "ex_buy_amount": "0_000000000000000000",
            "ex_sell_amount": "0_000000000000000000"
        },
        "AMM_CHI_NU": {
            "sell_token": "NU",
            "buy_token": "CHI",
            "ex_buy_amount": "671_160049925420935324",
            "ex_sell_amount": "943_421399527380685868"
        }
    },
    "orders": {
        "0": {
            "partial_fill": false,
            "buy_amount": "900_000000000000000000",
            "sell_amount": "1000_000000000000000000",
            "buy_token": "NU",
            "sell_token": "MU",
            "ex_buy_amount": "1301_146505249568235740",
            "ex_sell_amount": "1000_000000000043769433"
        }
    }
}
```
```
The surplus generated is 401_146505249528900094
```
<div align="center">
  <img src="https://github.com/nicoli-luca/mev_agent/blob/main/docs/images/graph_3_ex1.png" alt="Diagram" width="60%" height="60%">
  <p style="margin-top: 10px;">Strategy graph of the third input.</p>
</div>

## Discussion
In this exercise, we are considering each venue to be a constant product AMM with zero gas-fees. The price function will thus be `b(x) = xB/(A+x)`
As reported in the previous images, the `agent` tries to optimize the amount of sold coins through a different graph for each different input.
In the first case, we only have two nodes connected by a single edge, whereas in the most complex last example we have that coin `MU` is not directly connected to coin `NU`, and thus we have to pass through venues which account for intermediate coins such as `CHI`, `IOTA`, and `RHO`.

Regarding my results, the numerical error is hindering their precision, providing a total coin conservation error in the order of 10**-13.
This is for sure an error in my procedure. Maybe I should have enforced global coin conservation, although I was concerned with the convexity of such constraint.
Another possibility would have been to try to boost numerical accuracy employing `Decimal`, although I am not aware of Python packages that allow for function minimization with Decimal objects.


The advantage of this procedure is that it is extremely fast since we are not searching for a global minimum on a rough surface, but rather we just need to find the minimum of such a convex problem. (We are minimizing -surplus).
Something that has to be noticed is that in all cases we are actually enforcing to sell the complete amount of coins (this is due to the keyword `partial_fill`). In this case, we might not hit the absolute maximum of the surplus.


Go to [Second Exercise](../second/Exercise2.md)
