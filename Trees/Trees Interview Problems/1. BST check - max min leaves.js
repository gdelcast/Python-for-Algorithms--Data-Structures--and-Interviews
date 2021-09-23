class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function tree_max(node){        // check the max possible value for left branch
    if(!node)
        return Number.NEGATIVE_INFINITY;

    return Math.max(node.value, tree_max(node.left), tree_max(node.right));
}
function tree_min(node){        // check the min possible value for right branch
    if(!node)
        return Number.POSITIVE_INFINITY;

    return Math.min(node.value, tree_min(node.left), tree_min(node.right));
}
function verifyBST (node){
    if(!node)
        return true

    //check values of left & right and traverse down recursively
    if(verifyBST(node.left) && verifyBST(node.right)    
       && tree_max(node.left)<= node.value && node.value <= tree_min(node.right) ){       
        return true
    }
    else{
        return false
    }
}


//               10
//       5                   30
//   1       8         20
//         6   9     21  22  
//                   ^

let tree = new Node(10)
tree.left = new Node(5)
tree.left.left = new Node(1)
tree.left.right = new Node(8)
tree.left.right.left = new Node(6)
tree.left.right.right = new Node(9)
tree.right = new Node(30)
tree.right.left = new Node(20)
tree.right.left.left = new Node(21) // invalid
tree.right.left.right = new Node(22)

console.log(JSON.stringify(tree));

console.log(verifyBST(tree));

