### vue加载顺序
---
#### 多层组件传值加载顺序
``` js
1. provide 和 inject

2. beforecreate(父) >  data > created(父) > beforecreate(子) > created(子) > mouted(子) > mouted(父)
```
---