function quick_sort(arr){
    if (arr.length<=1)
        return arr;

    pivot = (arr.length)-1;

    let i = 0
    while (i<pivot){
        const temp = arr[i];
        if(arr[i]>arr[pivot]){
            arr[i] = arr[pivot-1];
            arr[pivot-1] = arr[pivot];
            arr[pivot] = temp;
            pivot -= 1;
        }
        else{
            i +=1;
        }
    }

    let first = arr.slice(0,pivot);         // this is different than python... 
    let middle = arr[pivot]                 // NEED TO RETURN TO A VARIABLE FIRST
    let second = arr.slice(pivot+1);        // instead of doing it in one line
    
    return [...quick_sort(first), middle , ...quick_sort(second) ];
}

let arr = [5,3,4,6,8,1,2,12,41,25];

console.log(quick_sort(arr));