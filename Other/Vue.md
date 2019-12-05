- v-for:
  指令可以绑定数组的数据来渲染一个项目列表

- v-on:（缩写@）
  指令添加一个事件监听器，通过它调用在 Vue 实例中定义的方法

- v-model:
  指令，它能轻松实现表单输入和应用状态之间的双向绑定

- v-once:
  只渲染元素和组件一次。随后的重新渲染，元素/组件及其所有的子节点将被视为静态内容并跳过。这可以用于优化更新性能。

- v-text:
  更新元素的 textContent

- v-html:
  更新元素的 innerHTML

- v-show:
  根据表达式之真假值，切换元素的 display CSS 属性,当条件变化时该指令触发过渡效果

- v-if:
  根据表达式的值的真假条件渲染元素。在切换时元素及它的数据绑定 / 组件被销毁并重建。如果元素是 <template> ，将提出它的内容作为条件块

- v-bind:（缩写:）
  动态地绑定一个或多个特性，或一个组件 prop 到表达式

- v-slot:（缩写#）
  可放置在函数参数位置的 JavaScript 表达式 (在支持的环境下可使用解构)。可选，即只需要在为插槽传入 prop 的时候使用

- v-pre:
  跳过这个元素和它的子元素的编译过程

- v-cloak:
  这个指令保持在元素上直到关联实例结束编译
  