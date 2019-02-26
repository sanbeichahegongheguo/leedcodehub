# 0003、longest_substring_without_repeating_characters 无重复字符的最长子串

## 1、题目描述

```
给定一个字符串，找出不含有重复字符的最长子串的长度。
```

## 2、示例

```
示例 1:  
输入: "abcabcbb"   
输出: 3   
解释: 无重复字符的最长子串是 "abc"，其长度为 3。

示例 2:  
输入: "bbbbb"  
输出: 1.     
解释: 无重复字符的最长子串是 "b"，其长度为 1。

示例 3:    
输入: "pwwkew"  
输出: 3  
解释: 无重复字符的最长子串是 "wke"，其长度为 3。    
请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。
```

## 3、解答方法

### 3.1 方法一：暴力法

#### 3.1.1 思路

逐个检查所有的子字符串，判断其是否不含有重复的字符。

图示：

![](.\pic\1.gif)

#### 3.1.2 算法

假设我们有一个函数 boolean allUnique(String substring) ，如果子字符串中的字符都是唯一的，它会返回 true，否则会返回 false。 我们可以遍历给定字符串 s 的所有可能的子字符串并调用函数 allUnique。 如果事实证明返回值为 true，那么我们将会更新无重复字符子串的最大长度的答案。

现在让我们填补缺少的部分：

为了枚举给定字符串的所有子字符串，我们需要枚举它们开始和结束的索引。假设开始和结束的索引分别为 i 和 j。那么我们有 0 ≤ i < j ≤ n （这里的结束索引 j 是按惯例排除的）。因此，使用 i 从 0 到 n−1 以及 j 从 i+1 到 n 这两个嵌套的循环，我们可以枚举出 s 的所有子字符串。

要检查一个字符串是否有重复字符，我们可以使用集合。我们遍历字符串中的所有字符，并将它们逐个放入 set 中。在放置一个字符之前，我们检查该集合是否已经包含它。如果包含，我们会返回 false。循环结束后，我们返回 true。

#### 3.1.3 代码示例

##### 3.1.3.1 官网提供的参考解答Java

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j <= n; j++)
                if (allUnique(s, i, j)) ans = Math.max(ans, j - i);
        return ans;
    }

    public boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<>();
        for (int i = start; i < end; i++) {
            Character ch = s.charAt(i);
            if (set.contains(ch)) return false;
            set.add(ch);
        }
        return true;
    }
}
```

3.1.3.2 python3

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

*O*(∑*i*=0*n*−1(∑*j*=*i*+1*n*(*j*−*i*)))=*O*(∑*i*=0*n*−12(1+*n*−*i*)(*n*−*i*))=*O*(*n*3)

#### 3.1.4 复杂度分析

## 4、拓展

