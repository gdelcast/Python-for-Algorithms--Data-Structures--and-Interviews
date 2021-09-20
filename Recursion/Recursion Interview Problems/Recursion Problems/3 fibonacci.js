function fib_rec(n){
    if (n<=1)
        return n

    return fib_rec(n-2) + fib_rec( n-1);
}

function fib_dyn(n){
    if (n<=1){
        cache[n] = n;
        return cache[n];
    }
    
    if(cache[n]!==undefined){
        return cache[n];
    }
    else{
        cache[n] = fib_dyn(n-2) + fib_dyn(n-1)
        return cache[n];
    }
}

function fib_iter(n){
    let a = 0
    let b = 1

    for (let i=0 ; i<n; i++){

        [a , b] = [b , a+b]
    }
    
    return a 
    
}

console.log(fib_rec(23));

cache = {}
console.log(fib_dyn(4));
console.log(cache);
console.log(fib_dyn(10));
console.log(cache);


console.log(fib_iter(23));
