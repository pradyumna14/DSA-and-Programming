#include <iostream>

// Define a structure for a tree node
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Class for the Binary Search Tree
class BinarySearchTree {
private:
    TreeNode* root;

    // Private helper function to insert a node recursively
    TreeNode* insert(TreeNode* node, int val) {
        if (node == nullptr) {
            return new TreeNode(val);
        }

        if (val < node->data) {
            node->left = insert(node->left, val);
        } else if (val > node->data) {
            node->right = insert(node->right, val);
        }

        return node;
    }

    // Private helper function to perform an inorder traversal
    void inorderTraversal(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        inorderTraversal(node->left);
        std::cout << node->data << " ";
        inorderTraversal(node->right);
    }

public:
    BinarySearchTree() : root(nullptr) {}

    // Public function to insert a value into the tree
    void insert(int val) {
        root = insert(root, val);
    }

    // Public function to perform an inorder traversal
    void inorderTraversal() {
        inorderTraversal(root);
        std::cout << std::endl;
    }
};

int main() {
    BinarySearchTree bst;

    // Insert values into the BST
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);
    bst.insert(60);
    bst.insert(80);

    // Perform an inorder traversal to display the values
    std::cout << "Inorder Traversal:" << std::endl;
    bst.inorderTraversal();

    return 0;
}
