
function merge_sort(arr){
    if (arr.length<=1)
        return arr;
    
    let arr1 = merge_sort(arr.slice(0,Math.floor(arr.length/2)));
    let arr2 = merge_sort(arr.slice(Math.floor(arr.length/2)));
    
    if(arr.length==2 && arr2[0]<arr1[0]){
        //return arr2.concat(arr1);
        return [...arr2, ...arr1]
    }
    else{
        const temp = [];
        while(arr1.length && arr2.length){
            if(arr2[0]<arr1[0]){
                temp.push(arr2.shift());
            }else{
                temp.push(arr1.shift());
            }
        }
        return [...temp, ...arr1, ...arr2]; //SAME
        //return temp.concat(arr1.concat(arr2));
    }
}



let arr =[5,3,4,6,8,1,2,12,41,25]
console.log(merge_sort(arr));