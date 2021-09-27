function selection_sort (arr){
    
    for (var i=0 ; i< arr.length; i++){
        let min = i;

        for (var j=i ; j<arr.length; j++){
            if(arr[j]<arr[min]){
                min = j;
            }
        }
        const temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}


let arr =[5,3,4,6,8,1,2,12,41,25]
selection_sort(arr)
console.log(arr);