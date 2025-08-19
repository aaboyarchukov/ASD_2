package main

type SimpleTreeNode struct {
	Value    int
	Parent   *SimpleTreeNode
	Children []SimpleTreeNode
}

type SimpleTree struct {
	Root SimpleTreeNode
}

func (tree *SimpleTree) AddChlid(ParentNode SimpleTreeNode, NewChlid SimpleTreeNode) {

}
