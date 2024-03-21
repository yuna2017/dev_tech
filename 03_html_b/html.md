<a name="EpoVd"></a>
# Web标准
<a name="xaTE5"></a>
### Web标准的构成
主要包括结构(Structure),表现(Presentation)和行为(Behavior)三个方面。<br />结构:结构用于对页面元素进行调整和分类。<br />表现:表现用于设置网页元素的版式、颜色、大小等外观样式，主要指的是CSS<br />行为:行为是指网页模型的定义一级交互的编写，现阶段主要学的是js
<a name="fHfZL"></a>
# HTML语法
![Snipaste_2022-10-16_20-50-25.png](https://cdn.nlark.com/yuque/0/2022/png/29781249/1665924659848-c42776b0-91e9-4fed-937f-610720306f6a.png#averageHue=%23d2d0c2&clientId=u8410b60b-7ecb-4&errorMessage=unknown%20error&from=ui&id=u96a6cb7b&originHeight=478&originWidth=877&originalType=binary&ratio=1&rotation=0&showTitle=false&size=131177&status=error&style=none&taskId=u73f1e2d2-d773-488d-ae31-928a8091f04&title=)<br /><!DOCTYPE> 是文档类型声明,作用就是告诉浏览器使用哪种HTML版本来显示网页。  <br /><!DOCTYPE>html>这句代码的意思：当前页面采取的是HTML5版本来显示网页<br />注意：

1. <!DOCTYPE>声明位于文档的最前面的位置，处于  标签之前 
2. <!DOCTYPE>不是一个HTML标签，它就是文档类型声明标签
<a name="dXKCF"></a>
### 标签
**标题标签**<h1></h1>     	 <br />1-6分别代表六个标题,每个标题独占一行<br />**段落标签**<p></p>    		<br />文本在一个段落会根据浏览器窗口大小自动换行，段落和段落之间有空隙<br />**换行标签**<br/><br />**加粗**<strong></strong>     或<b></b><br />_**倾斜**_<em></em>         或<i></i><br />~~**删除线**~~<del></del>           或<s></s><br />**下划线**<ins></ins>             或<u></u><br />下标H2O   <sub></sub><br />上标x2    <sup></sup><br />小于 		5&lt;10<br />大于		10&gt;5<br />小于等于	5&le;10<br />大于等于	10&ge;5<br />注册商标&reg;<br />版权符号& copy;


<div>标签 和<span>标签<br />二者没有语义，他们就是一个盒子，用来装内容的。<br />div大盒子，独占一行，大标签。span一行可以有多个，小盒子。
<a name="HU1lH"></a>
### 图像标签
<img   src ="图像URL"  alt="图片无法显示"   title="这是图片"/><br />src是<img>标签的必须属性,它用于置顶图像文件的路径和文件名<br />alt 替换文本，图片无法正常显示的时候现实的文本<br />title提示文本，鼠标放到图片上面显示的文字<br />width图像宽度  height图像高度<br />一般只修改一个属性  ，另一个自动等比例缩放<br />border设定图像边框(CSS)<br />**注：1.图像标签可以拥有多个属性，必须写在标签名的后面**<br />**2.各个属性之间无先后顺序，要有空格隔开**

1. **图像标签路径问题**

**绝对路径**：从盘符开始输入路径<br />**相对路径**：同一级文件的路径 <br />../回到上一级。

2. **超链接标签**

<a herf="跳转目标地址"    target="窗口打开方式   ——》本窗口打开(_self)    新窗口打开(_blank)">     文本或图像</a><br />链接分类:<br />1.外部链接：例如<a href="http://www.baidu.com">百度</a><br />2.内部链接：网站内部页面之间的相互连接.直接链接内部网页名称即可例如<a href="index.html">首页</a><br />3.空链接：如果当时没有确定的链接目标时，<a href="#">首页</a><br />4.下载链接：如果href里面地址是一个文件或者压缩包,会下载这个文件。<br />5.网页元素链接：在网页中的各种网页元素，如文本、图像、表格、音频、视频等都可以添加超链接<br />6.锚点链接：当我们点击链接，可以快速定位到页面中的某个位置<br />在链接文本的href属性中，设置属性值为#名字的形式，如<a href="#two">第二集</a><br />找到目标位置标签,里面添加一个id属性=刚才的名字，如:<h3 id="two">第二集介绍</h3>

3. **表格标签**

<table><br /><tr>							//该标签用于定义表格中的行<br /><td>单元格的文字</td>		//该标签用于定义表格中的单元格，必须嵌套在<tr></tr>中，<br />单元格中可以放任何元素         使用<th>替换<td>表格中的内容会加粗并居中<br /></tr><br /></table><br /><thead><tbody>时表格中的区域划分  便于人观察区分  无实际意义<br />属性要写在<table>标签里

| 属性名 | 属性值 | 描述 |
| --- | --- | --- |
| align | left、center、right | 规定表格相对周围元素的对齐方式 |
| border | 1或"" | 规定表格单元是否拥有边框，默认为""，表示没有边框 |
| cellpadding | 像素值 | 规定单元边沿与其内容之间的空白，默认1像素。 |
| cellspacing | 像素值 | 规定单元格之间的空白，默认2像素。 |
| width | 像素值或百分比 | 规定表格的宽度。 |

**合并单元格   **<br />rowspan(跨行合并)="合并单元格的个数"<br />colspan(跨列合并)="合并单元格的个数"<br />以最左上的单元格为目标单元格 ，写合并代码
<a name="BTcwr"></a>
###### 合并单元格步骤
1.先确定是跨行还是跨列<br />2.找到目标单元格，写合并方式=合并的单元格数量<br />3.删除多余的单元格

4. **列表标签**

分为无序列表 、有序列表、自定义列表<br />![Snipaste_2022-10-22_21-53-54.png](https://cdn.nlark.com/yuque/0/2022/png/29781249/1666446844258-43b66f8b-d1ab-49d8-aacd-4ceebe7054d5.png#averageHue=%23efe4da&clientId=u33165db1-fa17-4&from=ui&id=uaa138bd6&originHeight=226&originWidth=891&originalType=binary&ratio=1&rotation=0&showTitle=false&size=130445&status=done&style=none&taskId=uffa999e7-ecba-4efe-8d81-564900143b6&title=)
<a name="wjdz9"></a>
###### ①无序列表
<ul><br /><li>列表项1</li><br /><li>列表项2</li><br /><li>列表项3</li><br /></ul>
<a name="K4ZX9"></a>
###### ②有序列表
<ol><br /><li>列表项1</li><br /><li>列表项2</li><br /><li>列表项3</li><br /></ol>
<a name="tcLIV"></a>
###### ③自定义列表
<dl><br /><dt>名词1</dt>				<dt>和<dd>没有个数限制通常是一个<dt>对应多个<dd><br /><dd>名词1解释</dd>			<dt>和<dd>不是包含关系，是并列关系。<br /></dl>

5. **表单标签**

<form>标签用于定义表单域，以实现用户信息的手机和传递。<br /><form>会把它范围内的表单元素信息提交给服务器<br />常用属性:  <br />action       url地址       		用于指定接收并处理表单数据的服务器程序的url地址<br />method   get/post		用于设置表单数据的提交方式，其取值为get或post<br />name        名称			用于指定表单中的名称，以区分同一个页面中的多个表单域

**input**   输入表单元素<br />type属性的属性值

| 属性值 | 描述 |
| --- | --- |
| button | 定义可点击按钮(多数情况下，用于通过JavaScript启动脚本) |
| checkbox | 定义复选框 |
| file | 定义输入字段和浏览按钮，仅供文件上传 |
| hidden | 定义隐藏的输入字段 |
| image | 定义图像形式的提交按钮 |
| password | 定义密码字段，该字段中的字符被掩码 |
| radio | 定义单选按钮 |
| reset | 定义重置按钮，重置按钮会清楚表单中的所有数据 |
| submit | 定义提交按钮，提交按钮会把表单数据发送到服务器 |
| text | 定义单行的输入字段，用户可在其中输入文本。默认宽度为20个字符 |

input标签的其他属性

| 属性 | 属性值 | 描述 |
| --- | --- | --- |
| name | 由用户自定义 | 定义input元素的名称 |
| value | 由用户自定义 | 规定input元素的值 |
| checked | checked | 规定此input元素首次加载时应被选中 |
| maxlength | 正整数 | 规定输入字段中的字符的最大长度 |

<label>标签为input元素定义标注<br /><label>标签用于绑定一个表单元素，当点击<label>标签内的文本时，浏览器就会自动将焦点转到或者<br />选择对应的表单元素上，用来增加用户体验<br /><label   for="sex">男</label><br /><input   type="radio"  name="sex"    id="sex"/><br />核心：<label>标签的for属性应当与相关元素的id属性相同<br />**select **  下拉表单元素<br /><select><br /><option>选项1</option><br /><option>选项2</option><br /><option>选项3</option><br /></select><br /><select>中至少包含一对<option><br />在<option> 中定义select="selected"时，当前项即为默认选中项<br />**textarea     **文本域元素<br /><textarea     rows="3"   cols="20"><br />文本内容<br /></textarea><br />通过<textarea>标签可以轻松创建多行文本输入框<br />cols="每行中的字符数"，rows="显示的行数",我们在实际开发中不会使用，都是用CSS来改变大小。
