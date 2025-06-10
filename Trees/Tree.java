package Trees;

import java.util.*;

public class Tree{

    Tree left;
    Tree right;
    int data;

    public Tree(int data){
        this.data = data;
    }

    public static Tree preorder(Tree tree){
        System.out.print(tree.data + " ");

        if(tree.left != null){
            preorder(tree.left);
        }
        
        if(tree.right != null){
            preorder(tree.right);
        }

        return null;
    }

    public static void postorder(Tree tree){
        if(tree.left != null){
            postorder(tree.left);
        }
        
        if(tree.right != null){
            postorder(tree.right);
        }

        System.out.print(tree.data + " ");

        return;  
    }

    public static void inorder(Tree tree){
        if(tree.left != null){
            inorder(tree.left);
        }

        System.out.print(tree.data + " ");
        
        if(tree.right != null){
            inorder(tree.right);
        }

        return;  
    }

    public static void bfs(Tree node){
        
        Queue<Tree>queue = new LinkedList<>();
        List<List<Integer>> data = new ArrayList<>();

        List<Integer> sub = new ArrayList<>();
        int queueSize = 1;
        
        while(node != null){
            if(node.left != null){
                queue.add(node.left);
            }

            if(node.right != null){
                queue.add(node.right);
            }
            
            if(sub.size() < queueSize){
                sub.add(node.data);
            }

            // Append the sub array to main
            // clear the sub array for new row
            // update the new queue size
            if(sub.size() >= queueSize){
                data.add(sub);
                sub = new ArrayList<>();
                queueSize = queue.size();
            }

            node = queue.poll();
        }

        System.out.println(data.toString());
    }

    public static void main(String[] args) {
        Tree root = new Tree(1);
        root.left = new Tree(2);
        root.right = new Tree(3);

        root.right.left = new Tree(6);
        root.right.right = new Tree(7);

        root.right.right.left = new Tree(9);
        root.right.right.right = new Tree(10);

        root.left.left = new Tree(4);
        root.left.right = new Tree(5);

        root.left.right.left = new Tree(8);

        // bfs(root);
        
        // Recursion
        preorder(root);
        // System.out.println();
        // inorder(root);
        // postorder(copy);
    }
}
