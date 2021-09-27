
function insertion_sort(arr){
    for (var i=1; i<arr.length; i++){           // loop starts in position 1
        let curr = arr[i]                       // current pointer is the value to check if it's greater
        let back = i                            // backwards pointer checks reversing back from current-1 to zero

        while (back>0 && arr[back-1]>curr){     // nested loop shifts all elements>current a place up (making space)
            arr[back] = arr[back-1];
            back--;
        }
        arr[back] = curr;                       // after space is made from shift - insert the current element.
    }
}

let arr =[5,3,4,6,8,1,2,12,41,25]
insertion_sort(arr);
console.log(arr);