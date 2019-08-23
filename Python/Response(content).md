# Response.text/content
**1.response.text**
###### response.text 返回的是一个 unicode 型的文本数据 
###### response.text 则是默认”iso-8859-1”编码，服务器不指定的话是根据网页的响应来猜测编码
###### 想取文本数据可以通过response.text 

**1.response.content**
###### 返回的是 bytes 型的二进制数据想取图片，文件，则可以通过 response.content 
###### response.content 返回的是二进制响应内容 
###### response.text 则是默认”iso-8859-1”编码，服务器不指定的话是根据网页的响应来猜测编码


