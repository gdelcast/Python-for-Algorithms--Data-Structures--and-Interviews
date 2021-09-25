class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function chkmaxVal(node,maxVal){
    if(!node){
        return null
    }
    
    if(node.value <= maxVal)
        return node
    else
        return node.left
}

function chkminVal(node,minVal){
    if(!node){
        return null
    }
    
    if(node.value >= minVal)
        return node
    else
        return node.right
}

function trimBST(tree, minVal, maxVal){
    if (!tree){
        return null
    }

    tree.left = trimBST(tree.left, minVal, maxVal)
    tree.right = trimBST(tree.right, minVal, maxVal)
    

    tree.left = chkminVal(tree.left,minVal)
    tree.right = chkmaxVal(tree.right,maxVal)

    return tree

}

let tree = new Node(8)
tree.left = new Node(3)
tree.left.left = new Node(1)
tree.left.right = new Node(6)
tree.right = new Node(10)
tree.right.right = new Node(14)
tree.right.right.left = new Node(13)
tree.left.right.left = new Node(4)
tree.left.right.right = new Node(7)

console.log(tree)

trimBST(tree,5,13)
console.log("-------------------")
console.log(tree)


// function trimBST(tree, minVal, maxVal){
//     if (!tree){
//         return null
//     }
    
//     tree.left = trimBST(tree.left, minVal, maxVal)
//     tree.right = trimBST(tree.right, minVal, maxVal)
    

//     if (tree.value>=minVal && tree.value<= maxVal){
//         return tree
//     }
//     if (tree.value<minVal){
//         return tree.right
//     }
//     if (tree.value>maxVal){
//         return tree.left
//     }
    
// }
