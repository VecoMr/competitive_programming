#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>


typedef struct node {
    int data;
    struct node *left;
    struct node *right;
} node;

node *create_node(int data) {
    node *new_node = malloc(sizeof(node));
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

int get_nbr()
{
    int nbr;
    scanf("%d", &nbr);
    return nbr;
}

void insert_node(node *root, int data, int *c) {
    if (data > root->data) {
        if (root->right == NULL) {
            root->right = create_node(data);
            *c += 1;
        } else {
            *c += 1;
            insert_node(root->right, data, c);
        }
    } else {
        if (root->left == NULL) {
            root->left = create_node(data);
            *c += 1;
        } else {
            *c += 1;
            insert_node(root->left, data, c);
        }
    }
}

int main()
{
    int n = get_nbr();
    int c = 0;
    node *root = NULL;
    for (int i = 0; i < n; i++) {
        int data = get_nbr();
        if (i == 0) {
            root = create_node(data);
        } else {
            insert_node(root, data, &c);
        }
        printf("%d\n", c);
    }
}