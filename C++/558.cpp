/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* intersect(Node* quadTree1, Node* quadTree2) {
        Node *node1, *node2, *node3, *node4;
        Node* res = new Node;
        if(quadTree1->isLeaf == true && quadTree2->isLeaf ==  true) {
            Node node(quadTree1->val | quadTree2->val, true);
            *res = node;
        }
        else if(quadTree1->isLeaf == true) {
            res = quadTree1->val == true ? quadTree1 : quadTree2;
        }  
        else if(quadTree2->isLeaf == true) {
            res = quadTree2->val == true ? quadTree2 : quadTree1;
        }
        else {
            node1 = intersect(quadTree1->topLeft, quadTree2->topLeft);
            node2 = intersect(quadTree1->topRight, quadTree2->topRight);
            node3 = intersect(quadTree1->bottomLeft, quadTree2->bottomLeft);
            node4 = intersect(quadTree1->bottomRight, quadTree2->bottomRight);
            if(node1->isLeaf == true && node2->isLeaf == true && node3->isLeaf == true &&
                node4->isLeaf == true && node1->val == node2->val && node3->val == node4->val &&
                node1->val == node3->val) {
                    Node node(node1->val, node1->isLeaf);
                    *res = node;
                }
            else {
                Node node(false, false, node1, node2, node3, node4);
                *res = node;
            }
        }
        return res;
    }
};