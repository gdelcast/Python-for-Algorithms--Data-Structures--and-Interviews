function bubble_sort (arr){
    
    for (var i=0 ; i< arr.length; i++){                 // loop parse all elements
        for (var j=0 ; j<arr.length-1; j++){            // nested loop all elements
            if(arr[j]>arr[j+1]){                        // compare j and j+1 and swaps
                const temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}


let arr =[5,3,4,6,8,1,2,12,41,25]
bubble_sort(arr)
console.log(arr);