function bubble_sort (arr){
    
    for (var i=0 ; i< arr.length; i++){
        for (var j=0 ; j<arr.length-1; j++){
            if(arr[j]>arr[j+1]){
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