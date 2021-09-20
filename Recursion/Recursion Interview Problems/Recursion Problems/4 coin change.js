function rec_coin(target,coins){
    if(coins.length<=1){
        return Math.floor(target/coins[0])
    }
    //coins = coins.sort(function (a, b) {  return b - a;  }); // sort tricky with reverse
    coins = coins.sort((a, b) =>  b -a )

    return Math.floor(target/coins[0]) + rec_coin( target%coins[0], coins.splice(1));
}

console.log(rec_coin(23,[1,5,10,25]));