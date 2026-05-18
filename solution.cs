/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private void inorder(TreeNode root, IList<int> list){
        if(root == null){
            return;
        }

        inorder(root.left, list);
        list.Add(root.val);
        inorder(root.right, list);
    }

    public int GetMinimumDifference(TreeNode root) {
        List<int> list = new List<int>();
        inorder(root, list);
        int min = 999999;
        for(int i = 0; i < list.Count - 1; i++){
            min = Math.Min(min, list[i + 1] - list[i]);
        }

        return min;
    }
}
