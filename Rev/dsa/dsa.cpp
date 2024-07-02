#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

// Node structure for the binary tree
struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

// Binary Tree class
class BinaryTree {
public:
    TreeNode* root;

    BinaryTree() : root(nullptr) {}

    // Function to add a node in level order
    void addNode(int value) {
        TreeNode* newNode = new TreeNode(value);
        if (root == nullptr) {
            root = newNode;
            return;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();

            if (!temp->left) {
                temp->left = newNode;
                return;
            } else {
                q.push(temp->left);
            }

            if (!temp->right) {
                temp->right = newNode;
                return;
            } else {
                q.push(temp->right);
            }
        }
    }

    // Function to iterate all nodes in level order
    void levelOrderTraversal() {
        if (root == nullptr) return;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();

            cout << "Node: " << (char)temp->value << ", Height: " << getNodeHeight(temp) << endl;

            if (temp->left) q.push(temp->left);
            if (temp->right) q.push(temp->right);
        }
    }
    void levelOrderTraversalSimple() {
        if (root == nullptr) return;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();

            cout << (char)temp->value;
            
            if (temp->left) q.push(temp->left);
            if (temp->right) q.push(temp->right);
        }
    }
    void writeToString(string& f) {
        if (root == nullptr) return;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();

            // cout << (char)temp->value;
            f += (char)temp->value;
            if (temp->left) q.push(temp->left);
            if (temp->right) q.push(temp->right);
        }
    }

    // Function to iterate all nodes in level order
    void levelOrderEncryption() {
        if (root == nullptr) return;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();

            // cout << "Node: " << (char)temp->value << ", Height: " << getNodeHeight(temp) << endl;
            temp->value = temp->value ^ (getNodeHeight(temp)*3 + 30);
            if (temp->left) q.push(temp->left);
            if (temp->right) q.push(temp->right);
        }
    }

    // Function to get the height of a node
    int getNodeHeight(TreeNode* node) {
        if (node == nullptr) return -1;

        int leftHeight = getNodeHeight(node->left);
        int rightHeight = getNodeHeight(node->right);

        return max(leftHeight, rightHeight) + 1;
    }
};

int main(int argc, char* argv[]) {
    BinaryTree tree;
    string flag(argv[1]);

    for(char k:flag){
        tree.addNode((int)k);
    }

    cout << "Level order traversal with node heights:" << endl;
    string normalCheck = "";
    tree.writeToString(normalCheck);
    cout << normalCheck << " " << normalCheck.length() << endl;
    
    tree.levelOrderEncryption();

    string encrypted = "";
    tree.writeToString(encrypted);
    cout << encrypted << " " << encrypted.length() << endl;

    fstream file("flag", ios::out | ios::binary);
    file.write(encrypted.c_str(), encrypted.length());

    return 0;
}
