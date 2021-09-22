class BinHeapMaxArray{
    constructor(){
        this.heapList = new Array();
        this.size = null;
    }

    insert(value){
        this.heapList.push(value);
        this.size = this.size + 1;
        this.percolateUp(this.size-1);
        
    }
    
    percolateUp(i){
        let p = Math.floor(i/2);                                // parent is at half position
        while ( p >= 0){
            //console.log(i + ' ' + p)
            if(this.heapList[i] > this.heapList[p]){            // compare if child is max than parent and swap
                const tmp = this.heapList[p];
                this.heapList[p] = this.heapList[i];
                this.heapList[i] = tmp;
            }
                if(p==0){                                       // control when root reached
                break;
            }
            i = p;
            p = Math.floor(p/2);
        }
    }

    remove(){       // A max heap always remove the max element
        this.heapList[0] = this.heapList[this.size-1]           // swap the root with last element
        this.heapList.pop();                                    // drop the root at the end
        this.size = this.size - 1;
        this.percolateDown(0);                                       //percolate down to find max child
    }

    percolateDown(i){
        let c = i;
        while ( c * 2 < this.size){                         // this while only controls to reach to the middle of array
            let maxChild = this.__maxChild(c);              
            //console.log(c + ' ' + maxChild)
            if(this.heapList[maxChild] > this.heapList[c]){ // checks if child is max and swap 
                const tmp = this.heapList[c];
                this.heapList[c] = this.heapList[maxChild];
                this.heapList[maxChild] = tmp;
            }

            c = maxChild;
        }
    }

    __maxChild(i){
        if (i*2 + 2 > this.size){                   // control to prevent error if not children (not needed in Javascript)
            return i*2;
        }
        else{
            if (this.heapList[i*2+1] > this.heapList[i*2+2]){ // equivalent of compare left or right
                return i * 2 + 1;                             // return left
            }
            else{
                return i * 2 + 2;                            // return right 
            }
        }
    }

}

const heap = new BinHeapMaxArray();
heap.insert(5);
heap.insert(3);
heap.insert(1);
heap.insert(8);
heap.insert(7);
heap.insert(9);
heap.insert(20);
heap.insert(23);
heap.insert(17);
heap.insert(15);
console.log(heap.heapList);
//console.log(heap.size);

heap.remove();
console.log(heap.heapList);
heap.remove();
console.log(heap.heapList);
heap.remove();
console.log(heap.heapList);


