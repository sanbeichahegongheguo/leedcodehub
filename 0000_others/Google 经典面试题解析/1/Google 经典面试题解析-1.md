# Google 经典面试题解析-1

想象一下，你在操作一个流行的搜索引擎，而且你在日志中看到了两则查询，比如说“奥巴马的支持率”和“奥巴马的流行度”。（如果我没记错的话，这些是数据库面试中实际使用的例子，虽然这个问题的日期有点过时了……）这两个查询是不同的字符串，但是我认为（相信你也会同意）从根本上说它们查找的都是同一个东西，在计数查询、显示结果等方面可以将这两个查询视作等价。**那么，我们如何才能知道两个查询是同义词呢？**

让我们用正式语言描述一下。假设你有两个输入。第一个是一个列表，其中每个元素都是成对的两个字符串，而且它们是同义词。第二个也是一个列表，每个元素都是一组成对的字符串，代表两个查询。

为了具体起见，我通过以下示例输入来说明：

```shell
SYNONYMS = [
  ('rate', 'ratings'),
  ('approval', 'popularity'),
]

QUERIES = [
  ('obama approval rate', 'obama popularity ratings'),
  ('obama approval rates', 'obama popularity ratings'),
  ('obama approval rate', 'popularity ratings obama')
]
```

第一思路：

```python
def synonym_queries(synonym_words, queries):
    '''
    synonym_words: iterable of pairs of strings representing synonymous words.
    queries: iterable of pairs of strings representing queries to be tested for synonymous-ness.
    '''
    output = []
    for q1, q2 in queries:
        q1, q2 = q1.split(), q2.split()
        if len(q1) != len(q2):
            output.append(False)
            continue
        result = True
        for i in range(len(q1)):
            w1, w2 = q1[i], q2[i]
            if w1 == w2:
                continue
            elif words_are_synonyms(w1, w2):
                continue
            result = False
            break
        output.append(result)
    return output
```



完善：

```python
def synonym_queries(synonym_words, queries):
    '''
    synonym_words: iterable of pairs of strings representing synonymous words.
    queries: iterable of pairs of strings representing queries to be tested for synonymous-ness.
    '''
    synonyms = defaultdict(set)
    for w1, w2 in synonym_words:
        synonyms[w1].add(w2)

    output = []
    for q1, q2 in queries:
        q1, q2 = q1.split(), q2.split()
        if len(q1) != len(q2):
            output.append(False)
            continue
        result = True
        for i in range(len(q1)):
            w1, w2 = q1[i], q2[i]
            if w1 == w2:
                continue
            elif ((w1 in synonyms and w2 in synonyms[w1]) 
                    or (w2 in synonyms and w1 in synonyms[w2])):
                continue
            result = False
            break
        output.append(result)
    return output
```

