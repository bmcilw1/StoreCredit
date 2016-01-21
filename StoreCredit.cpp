#include "cstdlib"
#include "fstream"

struct Node {
    int i;
    int val;
};

class L
{
public:
    L (int length);
    virtual ~L ();
    bool insert(Node newNode);
    void quickSort();
    bool findC(int c);

private:
    int maxLen;
    int len;
    Node * l;
};

L::L(int length) {
    l = new Node[length];
    maxLen = length;
    len = 0;
}

L::~L() {
    delete [] l;
}

L::insert(Node newNode) {
    bool success = false;
    
    node[len] = newNode;
    success = true;

    return success;
}

L::quickSort() {

}
L::findC(int c) {

}

int main(int argc, char *argv[])
{
    
    return 0;
}
