
function permute(s){

    if (s.length<=1){
        return s
    }

    const list = Array.from(s);
    let out = [];

    for (const [i, key] of list.entries()){
        //console.log(i,key)

        for ( const [j, key2] of permute(s.substring(0,i) + s.substring(i+1))){

            out.push([key + j])
        }
    }
    return out

}

const s = permute('abcd');
console.log(s);