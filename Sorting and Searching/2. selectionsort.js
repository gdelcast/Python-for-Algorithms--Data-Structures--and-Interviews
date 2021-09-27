function selection_sort (arr){
    
    for (var i=0 ; i< arr.length; i++){         // loop all elements in array
        let min = i;

        for (var j=i ; j<arr.length; j++){      // nested loop searches the min value on the remaining portion of arr
            if(arr[j]<arr[min]){
                min = j;
            }
        }
        const temp = arr[i];                    // swaps current with min value
        arr[i] = arr[min];
        arr[min] = temp;
    }
}


let arr =[5,3,4,6,8,1,2,12,41,25]
selection_sort(arr)
console.log(arr);