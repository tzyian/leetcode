#include <vector>

// top-down splay tree which doesn't store parent pointers
template <typename T> class SplayTree {
  private:
    struct Node {
        T key;
        Node *left, *right;
        Node() : left(nullptr), right(nullptr) {}
        Node(T k) : key(k), left(nullptr), right(nullptr) {}
    };

    Node* root;

    // Rotate right at x<--p
    void zig(Node*& p) {
        Node* x = p->left;
        p->left = x->right;
        x->right = p;
        p = x;
    }

    // Rotate left at p-->x
    void zag(Node*& p) {
        Node* x = p->right;
        p->right = x->left;
        x->left = p;
        p = x;
    }

    /**
     * Splay the node with the given key to the root of the tree.
     * If the key is not found, a key that is parent or child is splayed instead
     */
    void splay(const T& key) {
        if (!root)
            return;

        Node header; // dummy
        Node* L = &header;
        Node* R = &header;
        Node* t = root;

        while (true) {
            if (key < t->key) {
                if (!t->left)
                    break;

                // zig-zig
                if (key < t->left->key) {
                    zig(t);
                    if (!t->left)
                        break;
                }

                // link-right
                R->left = t;
                R = t;
                t = t->left;
            } else if (key > t->key) {
                if (!t->right)
                    break;

                // zag-zag
                if (key > t->right->key) {
                    zag(t);
                    if (!t->right)
                        break;
                }

                // link left
                L->right = t;
                L = t;
                t = t->right;
            } else {
                break; // Key found
            }
        }

        // reassemble
        L->right = t->left;
        R->left = t->right;
        t->left = header.right;
        t->right = header.left;
        root = t;
    }

    Node* join(Node* left_subtree, Node* right_subtree) {
        if (!left_subtree)
            return right_subtree;
        if (!right_subtree)
            return left_subtree;

        this->root = left_subtree;
        Node* max_node = find_max(left_subtree);
        splay(max_node->key);
        max_node->right = right_subtree;
        return max_node;
    }

    Node* find_max(Node* node) {
        while (node->right)
            node = node->right;
        return node;
    }

    /* Return t1, t2, where nodes in t1 <= key and nodes in t2 > key */
    std::pair<Node*, Node*> split(const T& key) {
        if (!root)
            return {nullptr, nullptr};

        splay(key);
        if (root->key <= key) {
            Node* right_subtree = root->right;
            root->right = nullptr;
            return {root, right_subtree};
        } else {
            Node* left_subtree = root->left;
            root->left = nullptr;
            return {left_subtree, root};
        }
    }

    void delete_tree(Node* node) {
        std::vector<Node*> stack;
        if (node)
            stack.push_back(node);
        while (!stack.empty()) {
            Node* curr = stack.back();
            stack.pop_back();
            if (curr->left)
                stack.push_back(curr->left);
            if (curr->right)
                stack.push_back(curr->right);
            delete curr;
        }
    }

  public:
    SplayTree() : root(nullptr){};
    ~SplayTree() { delete_tree(root); }

    // Disable copy ctor and assm
    SplayTree(const SplayTree&) = delete;
    SplayTree& operator=(const SplayTree&) = delete;

    // Allow move ctor and move assm
    SplayTree(SplayTree&& other) noexcept : root(other.root) {
        other.root = nullptr;
    }
    SplayTree& operator=(SplayTree&& other) noexcept {
        if (this != &other) {
            delete_tree(root);
            root = other.root;
            other.root = nullptr;
        }
        return *this;
    }

    void insert(const T& key) {
        auto& [t1, t2] = split(key);
        Node* new_node = new Node(key);
        new_node->left = t1;
        new_node->right = t2;
        root = new_node;
    }

    void remove(const T& key) {
        splay(key);
        if (!root || root->key != key)
            return; // Key not found

        Node* left_subtree = root->left;
        Node* right_subtree = root->right;
        delete root;

        if (!left_subtree) {
            root = right_subtree;
        } else {
            root = left_subtree;
            splay(key); // splay the max node in left subtree
            root->right = right_subtree;
        }
    }

    bool search(const T& key) {
        splay(key);
        return root && root->key == key;
    }

    const Node* get_root() const { return root; }

    bool empty() const { return root == nullptr; }

    std::vector<Node*> walk() const {
        std::vector<Node*> result;
        std::vector<Node*> stack;
        Node* current = root;
        while (current || !stack.empty()) {
            while (current) {
                stack.push_back(current);
                current = current->left;
            }
            current = stack.back();
            stack.pop_back();
            result.push_back(current);

            current = current->right;
        }
        return result;
    }
};
